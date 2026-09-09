from app import app as flask_app
from database import db
from models import ExerciseAttempt, ExerciseResponse, UserActivityEvent
from services.exercise_attempt_service import (
    GRADE_CORRECT,
    GRADE_INCORRECT,
    GRADE_PENDING_REVIEW,
    normalize_numeric_value,
    save_draft,
    start_or_resume_attempt,
    submit_attempt,
)


EXERCISE_ID = "faraday_area_motional_001"


def login(client, username="Guest"):
    password = "studentpass" if username == "Guest" else "fisica2026"
    return client.post(
        "/login",
        data={"username": username, "password": password},
        follow_redirects=False,
    )


def sample_exercise():
    return {
        "id": "sample_mixed_001",
        "version": 1,
        "title": "Sample mixed exercise",
        "interactions": [
            {
                "id": "choice",
                "type": "single_choice",
                "correct_option_id": "a",
                "feedback_correct": "Bien",
                "feedback_incorrect": "Revisa",
            },
            {
                "id": "number",
                "type": "numeric",
                "expected_value": 8.66,
                "tolerance": 0.01,
            },
            {
                "id": "reasoning",
                "type": "short_text",
            },
        ],
    }


def test_opening_exercise_without_start_does_not_create_attempt():
    client = flask_app.test_client()
    assert login(client).status_code == 302

    response = client.get(f"/exercise/{EXERCISE_ID}")

    assert response.status_code == 200
    with flask_app.app_context():
        assert ExerciseAttempt.query.count() == 0


def test_starting_exercise_creates_attempt_and_event():
    client = flask_app.test_client()
    assert login(client).status_code == 302

    response = client.post(f"/exercise/{EXERCISE_ID}/start", follow_redirects=False)

    assert response.status_code == 302
    with flask_app.app_context():
        attempt = ExerciseAttempt.query.one()
        assert attempt.username == "Guest"
        assert attempt.exercise_id == EXERCISE_ID
        assert attempt.exercise_version == 1
        assert attempt.status == "started"
        assert UserActivityEvent.query.filter_by(event_type="exercise_started").count() == 1


def test_reopening_started_exercise_resumes_same_draft():
    client = flask_app.test_client()
    assert login(client).status_code == 302
    client.post(f"/exercise/{EXERCISE_ID}/start")

    with flask_app.app_context():
        attempt_id = ExerciseAttempt.query.one().id

    response = client.get(f"/exercise/{EXERCISE_ID}")

    assert response.status_code == 200
    assert f"attempt/{attempt_id}/draft".encode() in response.data
    with flask_app.app_context():
        assert ExerciseAttempt.query.count() == 1


def test_draft_response_persists_and_can_be_updated_with_raw_and_normalized_numeric():
    client = flask_app.test_client()
    assert login(client).status_code == 302
    client.post(f"/exercise/{EXERCISE_ID}/start")

    with flask_app.app_context():
        attempt_id = ExerciseAttempt.query.one().id

    client.post(
        f"/exercise/{EXERCISE_ID}/attempt/{attempt_id}/draft",
        data={"response_emf_magnitude": " 8,66 "},
    )
    client.post(
        f"/exercise/{EXERCISE_ID}/attempt/{attempt_id}/draft",
        data={"response_emf_magnitude": "8.67"},
    )

    with flask_app.app_context():
        response = ExerciseResponse.query.filter_by(field_id="emf_magnitude").one()
        assert response.raw_value == "8.67"
        assert response.normalized_value == "8.67"
        assert response.grading_status == "ungraded"


def test_decimal_comma_normalization():
    assert normalize_numeric_value("8,66") == "8.66"
    assert normalize_numeric_value(" 8.66 ") == "8.66"
    assert normalize_numeric_value("8,66 V") is None


def test_submission_grades_supported_fields_and_marks_open_pending_review():
    with flask_app.app_context():
        attempt, _ = start_or_resume_attempt("Guest", sample_exercise())
        submit_attempt(
            "Guest",
            attempt.id,
            sample_exercise(),
            {"choice": "a", "number": "8,665", "reasoning": "Porque si."},
        )

        saved = db.session.get(ExerciseAttempt, attempt.id)
        responses = {response.field_id: response for response in saved.responses}

        assert saved.status == "submitted"
        assert saved.submitted_at is not None
        assert saved.score == 2
        assert saved.max_score == 2
        assert responses["choice"].grading_status == GRADE_CORRECT
        assert responses["number"].grading_status == GRADE_CORRECT
        assert responses["number"].normalized_value == "8.665"
        assert responses["reasoning"].grading_status == GRADE_PENDING_REVIEW


def test_single_choice_incorrect_and_numeric_invalid_do_not_crash():
    with flask_app.app_context():
        attempt, _ = start_or_resume_attempt("Guest", sample_exercise())
        submit_attempt(
            "Guest",
            attempt.id,
            sample_exercise(),
            {"choice": "b", "number": "no es numero", "reasoning": ""},
        )

        responses = {response.field_id: response for response in attempt.responses}
        assert responses["choice"].grading_status == GRADE_INCORRECT
        assert responses["number"].grading_status == GRADE_INCORRECT
        assert responses["number"].normalized_value is None


def test_submitted_attempt_cannot_be_edited_and_new_start_creates_later_attempt():
    client = flask_app.test_client()
    assert login(client).status_code == 302
    client.post(f"/exercise/{EXERCISE_ID}/start")

    with flask_app.app_context():
        attempt_id = ExerciseAttempt.query.one().id

    submit_response = client.post(
        f"/exercise/{EXERCISE_ID}/attempt/{attempt_id}/submit",
        data={"response_identify_flux_change": "area"},
    )
    assert submit_response.status_code == 302

    edit_response = client.post(
        f"/exercise/{EXERCISE_ID}/attempt/{attempt_id}/draft",
        data={"response_identify_flux_change": "b_field"},
    )
    assert edit_response.status_code == 403

    client.post(f"/exercise/{EXERCISE_ID}/start")
    with flask_app.app_context():
        assert ExerciseAttempt.query.filter_by(username="Guest", exercise_id=EXERCISE_ID).count() == 2


def test_history_contains_own_attempts_and_excludes_other_users():
    with flask_app.app_context():
        guest_attempt, _ = start_or_resume_attempt("Guest", sample_exercise())
        paul_attempt, _ = start_or_resume_attempt("Paul", {**sample_exercise(), "id": "sample_other_001"})
        guest_attempt_id = guest_attempt.id
        paul_attempt_id = paul_attempt.id

    client = flask_app.test_client()
    assert login(client).status_code == 302
    response = client.get("/practice/history")

    assert response.status_code == 200
    assert f"Intento #{guest_attempt_id}".encode() in response.data
    assert f"Intento #{paul_attempt_id}".encode() not in response.data


def test_direct_access_to_another_users_attempt_is_rejected():
    with flask_app.app_context():
        attempt, _ = start_or_resume_attempt("Paul", {"id": EXERCISE_ID, "version": 1, "title": "Owned"})
        attempt_id = attempt.id

    client = flask_app.test_client()
    assert login(client, "Guest").status_code == 302
    response = client.get(f"/exercise/{EXERCISE_ID}/attempt/{attempt_id}")

    assert response.status_code == 403


def test_unknown_exercise_and_unknown_field_are_handled_cleanly():
    client = flask_app.test_client()
    assert login(client).status_code == 302

    assert client.get("/exercise/unknown").status_code == 404

    client.post(f"/exercise/{EXERCISE_ID}/start")
    with flask_app.app_context():
        attempt_id = ExerciseAttempt.query.one().id

    response = client.post(
        f"/exercise/{EXERCISE_ID}/attempt/{attempt_id}/draft",
        data={"response_not_a_real_field": "x"},
    )

    assert response.status_code == 404
    with flask_app.app_context():
        assert ExerciseResponse.query.count() == 0
