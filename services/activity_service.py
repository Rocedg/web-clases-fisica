import json
from datetime import datetime

from flask import current_app, has_app_context

from database import db
from models import (
    UserActivityEvent,
    UserQuizAttempt,
    UserResourceAccess,
    UserTopicProgress,
)


def _warn(message, error):
    if has_app_context():
        current_app.logger.warning("%s: %s", message, error)
    else:
        print(f"Warning: {message}: {error}")


def _metadata_to_json(metadata):
    if metadata is None:
        return None

    try:
        return json.dumps(metadata, ensure_ascii=False)
    except TypeError:
        return json.dumps({"unserializable_metadata": str(metadata)}, ensure_ascii=False)


def _commit_or_none(message):
    try:
        db.session.commit()
        return True
    except Exception as error:
        db.session.rollback()
        _warn(message, error)
        return False


def record_activity_event(
    username,
    event_type,
    object_type,
    object_id=None,
    object_title=None,
    metadata=None,
    duration_seconds=None,
):
    if not username:
        return None

    event = UserActivityEvent(
        username=username,
        event_type=event_type,
        object_type=object_type,
        object_id=str(object_id) if object_id is not None else None,
        object_title=object_title,
        metadata_json=_metadata_to_json(metadata),
        duration_seconds=duration_seconds,
    )
    db.session.add(event)

    if _commit_or_none("Activity event could not be recorded"):
        return event
    return None


def mark_topic_opened(username, topic_id, topic_title=None, last_page=None):
    if not username or topic_id is None:
        return None

    topic_id = str(topic_id)

    try:
        progress = UserTopicProgress.query.filter_by(
            username=username,
            topic_id=topic_id,
        ).one_or_none()

        if progress is None:
            progress = UserTopicProgress(
                username=username,
                topic_id=topic_id,
                topic_title=topic_title,
                last_page=last_page,
                last_opened_at=datetime.utcnow(),
                total_time_seconds=0,
                open_count=1,
            )
            db.session.add(progress)
        else:
            progress.topic_title = topic_title or progress.topic_title
            progress.last_page = last_page if last_page is not None else progress.last_page
            progress.last_opened_at = datetime.utcnow()
            progress.open_count = (progress.open_count or 0) + 1

        if _commit_or_none("Topic progress could not be recorded"):
            return progress
    except Exception as error:
        db.session.rollback()
        _warn("Topic progress could not be recorded", error)

    return None


def record_resource_access(
    username,
    resource_type,
    action,
    resource_id=None,
    resource_title=None,
    path=None,
):
    if not username:
        return None

    access = UserResourceAccess(
        username=username,
        resource_type=resource_type,
        action=action,
        resource_id=str(resource_id) if resource_id is not None else None,
        resource_title=resource_title,
        path=path,
    )
    db.session.add(access)

    if _commit_or_none("Resource access could not be recorded"):
        return access
    return None


def record_quiz_attempt(
    username,
    quiz_id,
    quiz_title=None,
    score=None,
    total_questions=None,
    correct_answers=None,
    percentage=None,
    started_at=None,
    duration_seconds=None,
    metadata=None,
):
    if not username or quiz_id is None:
        return None

    attempt = UserQuizAttempt(
        username=username,
        quiz_id=str(quiz_id),
        quiz_title=quiz_title,
        score=score,
        total_questions=total_questions,
        correct_answers=correct_answers,
        percentage=percentage,
        started_at=started_at,
        submitted_at=datetime.utcnow(),
        duration_seconds=duration_seconds,
        metadata_json=_metadata_to_json(metadata),
    )
    db.session.add(attempt)

    if _commit_or_none("Quiz attempt could not be recorded"):
        return attempt
    return None


def empty_activity_snapshot():
    return {
        "latest_topic": None,
        "quiz_attempt_count": 0,
        "last_quiz_attempt": None,
        "recent_events": [],
    }


def get_user_activity_snapshot(username, recent_limit=8):
    if not username:
        return empty_activity_snapshot()

    try:
        latest_topic = (
            UserTopicProgress.query.filter_by(username=username)
            .order_by(UserTopicProgress.last_opened_at.desc())
            .first()
        )
        quiz_attempt_count = UserQuizAttempt.query.filter_by(username=username).count()
        last_quiz_attempt = (
            UserQuizAttempt.query.filter_by(username=username)
            .order_by(UserQuizAttempt.submitted_at.desc())
            .first()
        )
        recent_events = (
            UserActivityEvent.query.filter_by(username=username)
            .order_by(UserActivityEvent.created_at.desc())
            .limit(recent_limit)
            .all()
        )

        return {
            "latest_topic": latest_topic,
            "quiz_attempt_count": quiz_attempt_count,
            "last_quiz_attempt": last_quiz_attempt,
            "recent_events": recent_events,
        }
    except Exception as error:
        db.session.rollback()
        _warn("Activity snapshot could not be loaded", error)
        return empty_activity_snapshot()
