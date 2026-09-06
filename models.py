from datetime import datetime

from database import db


def utc_now():
    return datetime.utcnow()


class UserActivityEvent(db.Model):
    __tablename__ = "user_activity_events"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), nullable=False)
    event_type = db.Column(db.String(80), nullable=False)
    object_type = db.Column(db.String(80), nullable=False)
    object_id = db.Column(db.String(120), nullable=True)
    object_title = db.Column(db.String(255), nullable=True)
    metadata_json = db.Column(db.Text, nullable=True)
    duration_seconds = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=utc_now)


class UserTopicProgress(db.Model):
    __tablename__ = "user_topic_progress"
    __table_args__ = (
        db.UniqueConstraint(
            "username",
            "topic_id",
            name="uq_user_topic_progress_username_topic_id",
        ),
    )

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), nullable=False)
    topic_id = db.Column(db.String(120), nullable=False)
    topic_title = db.Column(db.String(255), nullable=True)
    last_page = db.Column(db.Integer, nullable=True)
    last_opened_at = db.Column(db.DateTime, nullable=False, default=utc_now)
    total_time_seconds = db.Column(db.Integer, nullable=False, default=0)
    open_count = db.Column(db.Integer, nullable=False, default=1)


class UserResourceAccess(db.Model):
    __tablename__ = "user_resource_access"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), nullable=False)
    resource_type = db.Column(db.String(80), nullable=False)
    resource_id = db.Column(db.String(120), nullable=True)
    resource_title = db.Column(db.String(255), nullable=True)
    action = db.Column(db.String(40), nullable=False)
    path = db.Column(db.String(500), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=utc_now)


class UserQuizAttempt(db.Model):
    __tablename__ = "user_quiz_attempts"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), nullable=False)
    quiz_id = db.Column(db.String(120), nullable=False)
    quiz_title = db.Column(db.String(255), nullable=True)
    score = db.Column(db.Integer, nullable=True)
    total_questions = db.Column(db.Integer, nullable=True)
    correct_answers = db.Column(db.Integer, nullable=True)
    percentage = db.Column(db.Float, nullable=True)
    started_at = db.Column(db.DateTime, nullable=True)
    submitted_at = db.Column(db.DateTime, nullable=False, default=utc_now)
    duration_seconds = db.Column(db.Integer, nullable=True)
    metadata_json = db.Column(db.Text, nullable=True)
