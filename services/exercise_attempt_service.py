from __future__ import annotations

from decimal import Decimal, InvalidOperation
import re

from database import db
from models import ExerciseAttempt, ExerciseResponse, utc_now
from services.activity_service import record_activity_event


ATTEMPT_STARTED = "started"
ATTEMPT_SUBMITTED = "submitted"
ATTEMPT_REVIEWED = "reviewed"

GRADE_UNGRADED = "ungraded"
GRADE_CORRECT = "correct"
GRADE_INCORRECT = "incorrect"
GRADE_PENDING_REVIEW = "pending_review"

OPEN_RESPONSE_TYPES = {
    "short_text",
    "written_upload",
    "open_text",
    "text",
    "textarea",
    "numeric_or_expression_placeholder",
}

NUMERIC_RE = re.compile(r"^[+-]?\d+(?:[\.,]\d+)?(?:[eE][+-]?\d+)?$")


class ExerciseAttemptError(ValueError):
    pass


class ExerciseAttemptForbidden(PermissionError):
    pass


def exercise_version(exercise):
    value = exercise.get("version", 1)
    try:
        return int(value)
    except (TypeError, ValueError):
        return 1


def response_fields(exercise):
    interactions = exercise.get("interactions")
    if isinstance(interactions, list) and interactions:
        return [field for field in interactions if isinstance(field, dict) and field.get("id")]

    fields = exercise.get("response_fields")
    if isinstance(fields, list) and fields:
        normalized_fields = []
        for index, field in enumerate(fields, start=1):
            if not isinstance(field, dict):
                continue
            field_id = field.get("id") or f"response_{index}"
            response_type = field.get("type") or _response_mode_to_type(exercise.get("response_mode"))
            normalized_field = dict(field)
            normalized_field["id"] = field_id
            normalized_field["type"] = response_type
            normalized_fields.append(normalized_field)
        return normalized_fields

    response_mode = exercise.get("response_mode")
    if response_mode:
        return [
            {
                "id": "response",
                "type": _response_mode_to_type(response_mode),
                "label": exercise.get("response_prompt") or "Respuesta",
                "prompt": exercise.get("response_prompt") or "Escribe tu respuesta.",
            }
        ]

    return []


def _response_mode_to_type(response_mode):
    if response_mode == "numeric_multi":
        return "numeric"
    if response_mode in {"short_text", "written_upload"}:
        return response_mode
    return "open_text"


def field_map(exercise):
    return {str(field["id"]): field for field in response_fields(exercise)}


def response_map(attempt):
    return {response.field_id: response for response in attempt.responses}


def normalize_numeric_value(raw_value):
    value = (raw_value or "").strip()
    if not value:
        return None

    compact = value.replace(" ", "")
    if not NUMERIC_RE.match(compact):
        return None

    normalized = compact.replace(",", ".")
    try:
        number = Decimal(normalized)
    except InvalidOperation:
        return None

    return format(number.normalize(), "f")


def normalize_response(raw_value, response_type):
    if response_type == "numeric":
        return normalize_numeric_value(raw_value)
    if raw_value is None:
        return ""
    return str(raw_value).strip()


def start_or_resume_attempt(username, exercise):
    if not username:
        raise ExerciseAttemptForbidden("Authentication is required.")

    version = exercise_version(exercise)
    attempt = (
        ExerciseAttempt.query.filter_by(
            username=username,
            exercise_id=str(exercise["id"]),
            exercise_version=version,
            status=ATTEMPT_STARTED,
        )
        .order_by(ExerciseAttempt.updated_at.desc())
        .first()
    )
    if attempt:
        return attempt, False

    attempt = ExerciseAttempt(
        username=username,
        exercise_id=str(exercise["id"]),
        exercise_version=version,
        status=ATTEMPT_STARTED,
        started_at=utc_now(),
        updated_at=utc_now(),
    )
    db.session.add(attempt)
    db.session.commit()
    record_activity_event(
        username,
        "exercise_started",
        "exercise",
        object_id=exercise["id"],
        object_title=exercise.get("title"),
        metadata={"attempt_id": attempt.id, "exercise_version": version},
    )
    return attempt, True


def get_owned_attempt(username, attempt_id):
    attempt = db.session.get(ExerciseAttempt, attempt_id)
    if attempt is None:
        raise ExerciseAttemptError("Attempt not found.")
    if attempt.username != username:
        raise ExerciseAttemptForbidden("Attempt belongs to another user.")
    return attempt


def latest_started_attempt(username, exercise):
    return (
        ExerciseAttempt.query.filter_by(
            username=username,
            exercise_id=str(exercise["id"]),
            exercise_version=exercise_version(exercise),
            status=ATTEMPT_STARTED,
        )
        .order_by(ExerciseAttempt.updated_at.desc())
        .first()
    )


def save_draft(username, attempt_id, exercise, submitted_values):
    attempt = _validate_editable_attempt(username, attempt_id, exercise)
    _save_response_values(attempt, exercise, submitted_values, grade=False)
    attempt.status = ATTEMPT_STARTED
    attempt.updated_at = utc_now()
    db.session.commit()
    record_activity_event(
        username,
        "exercise_draft_saved",
        "exercise",
        object_id=attempt.exercise_id,
        object_title=exercise.get("title"),
        metadata={"attempt_id": attempt.id, "exercise_version": attempt.exercise_version},
    )
    return attempt


def submit_attempt(username, attempt_id, exercise, submitted_values):
    attempt = _validate_editable_attempt(username, attempt_id, exercise)
    _save_response_values(attempt, exercise, submitted_values, grade=True)

    graded = [
        response
        for response in attempt.responses
        if response.grading_status in {GRADE_CORRECT, GRADE_INCORRECT}
    ]
    attempt.score = float(sum(1 for response in graded if response.grading_status == GRADE_CORRECT))
    attempt.max_score = float(len(graded))
    attempt.status = ATTEMPT_SUBMITTED
    attempt.submitted_at = utc_now()
    attempt.updated_at = attempt.submitted_at
    db.session.commit()
    record_activity_event(
        username,
        "exercise_submitted",
        "exercise",
        object_id=attempt.exercise_id,
        object_title=exercise.get("title"),
        metadata={
            "attempt_id": attempt.id,
            "exercise_version": attempt.exercise_version,
            "score": attempt.score,
            "max_score": attempt.max_score,
        },
    )
    return attempt


def get_student_attempt_history(username):
    if not username:
        return []
    return (
        ExerciseAttempt.query.filter_by(username=username)
        .order_by(ExerciseAttempt.updated_at.desc(), ExerciseAttempt.id.desc())
        .all()
    )


def _validate_editable_attempt(username, attempt_id, exercise):
    attempt = get_owned_attempt(username, attempt_id)
    if attempt.exercise_id != str(exercise["id"]):
        raise ExerciseAttemptError("Attempt does not match this exercise.")
    if attempt.exercise_version != exercise_version(exercise):
        raise ExerciseAttemptError("Attempt version does not match this exercise.")
    if attempt.status != ATTEMPT_STARTED:
        raise ExerciseAttemptForbidden("Submitted attempts cannot be edited.")
    return attempt


def _save_response_values(attempt, exercise, submitted_values, grade):
    fields = field_map(exercise)
    response_by_field = response_map(attempt)

    unknown_fields = set(submitted_values) - set(fields)
    if unknown_fields:
        raise ExerciseAttemptError("Unknown response field.")

    for field_id, field in fields.items():
        raw_value = submitted_values.get(field_id, "")
        response_type = field.get("type") or "open_text"
        normalized_value = normalize_response(raw_value, response_type)

        response = response_by_field.get(field_id)
        if response is None:
            response = ExerciseResponse(attempt=attempt, field_id=field_id)
            db.session.add(response)

        response.response_type = response_type
        response.raw_value = raw_value
        response.normalized_value = normalized_value
        response.updated_at = utc_now()

        if grade:
            _grade_response(response, field)
        else:
            response.grading_status = GRADE_UNGRADED
            response.auto_score = None
            response.feedback = None


def _grade_response(response, field):
    response_type = response.response_type

    if response_type == "single_choice" and field.get("correct_option_id"):
        expected = str(field.get("correct_option_id"))
        is_correct = response.normalized_value == expected
        response.grading_status = GRADE_CORRECT if is_correct else GRADE_INCORRECT
        response.auto_score = 1.0 if is_correct else 0.0
        response.feedback = field.get("feedback_correct" if is_correct else "feedback_incorrect")
        return

    if response_type == "numeric" and field.get("expected_value") is not None:
        expected = _decimal_or_none(field.get("expected_value"))
        given = _decimal_or_none(response.normalized_value)
        tolerance = _decimal_or_none(
            field.get("tolerance", field.get("absolute_tolerance", field.get("abs_tolerance", 0)))
        )
        if expected is not None and given is not None and tolerance is not None:
            is_correct = abs(given - expected) <= tolerance
        else:
            is_correct = False
        response.grading_status = GRADE_CORRECT if is_correct else GRADE_INCORRECT
        response.auto_score = 1.0 if is_correct else 0.0
        response.feedback = field.get("feedback_correct" if is_correct else "feedback_incorrect")
        return

    response.grading_status = GRADE_PENDING_REVIEW
    response.auto_score = None
    response.feedback = None


def _decimal_or_none(value):
    if value is None:
        return None
    try:
        return Decimal(str(value))
    except InvalidOperation:
        return None
