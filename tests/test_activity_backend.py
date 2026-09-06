from app import app as flask_app
from database import db
from models import (
    UserActivityEvent,
    UserQuizAttempt,
    UserResourceAccess,
    UserTopicProgress,
)
from services.activity_service import (
    mark_topic_opened,
    record_activity_event,
    record_quiz_attempt,
)


def login(client):
    return client.post(
        "/login",
        data={"username": "Guest", "password": "studentpass"},
        follow_redirects=False,
    )


def test_database_can_initialize_in_temporary_sqlite():
    with flask_app.app_context():
        db.create_all()
        assert UserActivityEvent.query.count() == 0


def test_record_activity_event_creates_row():
    with flask_app.app_context():
        record_activity_event(
            "Guest",
            "topic_view",
            "topic",
            object_id="1",
            object_title="Introduccion",
            metadata={"source": "test"},
        )

        event = UserActivityEvent.query.one()
        assert event.username == "Guest"
        assert event.event_type == "topic_view"
        assert event.metadata_json is not None


def test_mark_topic_opened_creates_and_updates_one_row():
    with flask_app.app_context():
        mark_topic_opened("Guest", "1", "Tema 1")
        mark_topic_opened("Guest", "1", "Tema 1")

        progress = UserTopicProgress.query.one()
        assert progress.username == "Guest"
        assert progress.topic_id == "1"
        assert progress.open_count == 2


def test_record_quiz_attempt_creates_row():
    with flask_app.app_context():
        record_quiz_attempt(
            "Guest",
            "1",
            quiz_title="Introduccion",
            score=80,
            total_questions=5,
            correct_answers=4,
            percentage=80.0,
            metadata={"answers": ["A", "B"]},
        )

        attempt = UserQuizAttempt.query.one()
        assert attempt.quiz_id == "1"
        assert attempt.correct_answers == 4
        assert attempt.percentage == 80.0


def test_existing_routes_and_quiz_submission_still_work():
    client = flask_app.test_client()
    assert login(client).status_code == 302

    assert client.get("/topics").status_code == 200
    assert client.get("/homework").status_code == 200
    assert client.get("/quiz/1").status_code == 200

    answers = {
        "answer_1": "C",
        "answer_2": "C",
        "answer_3": "A",
        "answer_4": "A",
        "answer_5": "A",
        "answer_6": "B",
        "answer_7": "A",
        "answer_8": "B",
        "answer_9": "A",
        "answer_10": "A",
        "answer_11": "A",
        "answer_12": "C",
        "answer_13": "B",
        "answer_14": "A",
        "answer_15": "B",
    }
    response = client.post("/submit-quiz/1", data=answers, follow_redirects=False)
    assert response.status_code == 302
    assert "/quiz-results" in response.headers["Location"]

    results = client.get("/quiz-results")
    assert results.status_code == 200

    with flask_app.app_context():
        attempt = UserQuizAttempt.query.filter_by(username="Guest", quiz_id="1").one()
        assert attempt.correct_answers == 15
        assert attempt.total_questions == 15
        assert attempt.percentage == 100.0


def test_tracked_resource_route_records_logged_in_access():
    client = flask_app.test_client()
    assert login(client).status_code == 302

    response = client.get("/resource/topic_pdf/1/open", follow_redirects=False)
    assert response.status_code == 302

    with flask_app.app_context():
        assert UserResourceAccess.query.filter_by(
            username="Guest",
            resource_type="topic_pdf",
            action="open",
        ).count() == 1
        assert UserTopicProgress.query.filter_by(username="Guest", topic_id="1").count() == 1


def test_progress_page_requires_login_and_renders_for_user():
    client = flask_app.test_client()
    assert client.get("/progress").status_code == 302

    assert login(client).status_code == 302
    response = client.get("/progress")
    assert response.status_code == 200
