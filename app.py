from datetime import datetime
from functools import wraps
import json
import os

import click
from flask import Flask, redirect, render_template, request, session, url_for

from database import db, init_app as init_database
from services.activity_service import (
    get_user_activity_snapshot,
    mark_topic_opened,
    record_activity_event,
    record_quiz_attempt,
    record_resource_access,
)


app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
init_database(app)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')

USERS = {
    'Paul': ['fisica2026', 'student'],
    'Guest': ['studentpass', 'student']
}

NAV_ITEMS = [
    {
        'endpoint': 'topics',
        'label': 'Apuntes',
        'description': 'Lecciones en PDF',
        'icon': 'fa-book-open'
    },
    {
        'endpoint': 'homework',
        'label': 'Ejercicios',
        'description': 'Cuestionarios autocorregibles',
        'icon': 'fa-pen-ruler'
    },
    {
        'endpoint': 'exams',
        'label': 'Exámenes',
        'description': 'Simulacros y correcciones',
        'icon': 'fa-file-circle-check'
    },
    {
        'endpoint': 'miscellaneous',
        'label': 'PAU',
        'description': 'Criterios, currículum y resúmenes',
        'icon': 'fa-compass'
    }
]


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


def data_path(filename):
    return os.path.join(DATA_DIR, filename)


def load_json(filename, fallback):
    try:
        with open(data_path(filename), 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return fallback


def load_topics():
    return load_json('topics.json', {'topics': []})


def load_quizzes():
    quizzes_path = data_path('quizzes.json')

    try:
        if not os.path.exists(quizzes_path):
            with open(quizzes_path, 'w', encoding='utf-8') as f:
                json.dump({'quizzes': []}, f)

        with open(quizzes_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        valid_quizzes = []
        for quiz in data.get('quizzes', []):
            required = ['id', 'title', 'question_count', 'correct_answers', 'pdfs']
            if all(key in quiz for key in required):
                valid_quizzes.append(quiz)
            else:
                print(f"Quiz inválido omitido: {quiz.get('title', 'Sin título')}")

        return {'quizzes': valid_quizzes}
    except Exception as e:
        print(f"Error cargando quizzes: {str(e)}")
        return {'quizzes': []}


def load_exams():
    return load_json('exams.json', {'exams': []})


def load_summaries():
    return load_json('summaries.json', {'summaries': []})


def asset_url(path):
    if not path:
        return ''
    if path.startswith(('http://', 'https://', '/')):
        return path
    if path.startswith('static/'):
        return url_for('static', filename=path.replace('static/', '', 1))
    return url_for('static', filename=path)


def current_username():
    return session.get('username')


def find_by_id(items, item_id):
    item_id = str(item_id)
    return next((item for item in items if str(item.get('id')) == item_id), None)


def find_tracked_resource(resource_type, resource_id):
    if resource_type == 'topic_pdf':
        item = find_by_id(load_topics().get('topics', []), resource_id)
        object_type = 'topic'
    elif resource_type == 'summary_pdf':
        item = find_by_id(load_summaries().get('summaries', []), resource_id)
        object_type = 'summary'
    elif resource_type == 'exam_pdf':
        item = find_by_id(load_exams().get('exams', []), resource_id)
        object_type = 'exam'
    elif resource_type in {'quiz_question_pdf', 'solution_pdf'}:
        quiz = find_by_id(load_quizzes().get('quizzes', []), resource_id)
        if not quiz:
            return None

        pdf_key = 'solutions' if resource_type == 'solution_pdf' else 'questions'
        item = {
            'id': quiz.get('id'),
            'title': quiz.get('title'),
            'url': quiz.get('pdfs', {}).get(pdf_key),
        }
        object_type = 'quiz'
    else:
        return None

    if not item or not item.get('url'):
        return None

    return {
        'id': str(item.get('id')) if item.get('id') is not None else str(resource_id),
        'title': item.get('title'),
        'path': item.get('url'),
        'object_type': object_type,
    }


def store_quiz_start_time(quiz_id):
    quiz_id = str(quiz_id)
    quiz_start_times = session.get('quiz_start_times', {})
    quiz_start_times[quiz_id] = datetime.utcnow().isoformat()
    session['quiz_start_times'] = quiz_start_times


def pop_quiz_start_time(quiz_id):
    quiz_id = str(quiz_id)
    quiz_start_times = session.get('quiz_start_times', {})
    start_value = quiz_start_times.pop(quiz_id, None)
    session['quiz_start_times'] = quiz_start_times

    if not start_value:
        return None, None

    try:
        started_at = datetime.fromisoformat(start_value)
    except ValueError:
        return None, None

    duration_seconds = max(0, int((datetime.utcnow() - started_at).total_seconds()))
    return started_at, duration_seconds


@app.context_processor
def inject_layout_context():
    return {
        'asset_url': asset_url,
        'nav_items': NAV_ITEMS
    }


@app.cli.command('init-db')
def init_db_command():
    with app.app_context():
        db.create_all()
    database_uri = app.config['SQLALCHEMY_DATABASE_URI']
    if database_uri.startswith('sqlite:///') and database_uri.endswith('web_clases_rocedg.sqlite'):
        database_location = 'instance/web_clases_rocedg.sqlite'
    else:
        database_location = 'configured DATABASE_URL'
    click.echo(f"Database tables created at {database_location}")


@app.route('/')
def home():
    topics_data = load_topics()
    quiz_data = load_quizzes()
    exams_data = load_exams()
    summaries_data = load_summaries()
    stats = {
        'topics': len(topics_data['topics']),
        'quizzes': len(quiz_data['quizzes']),
        'exams': len(exams_data['exams']),
        'summaries': len(summaries_data['summaries'])
    }

    return render_template(
        'home.html',
        featured_quizzes=quiz_data['quizzes'][:3],
        recent_topics=topics_data['topics'][-3:],
        stats=stats
    )


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in USERS and USERS[username][0] == password:
            session['username'] = username
            session['role'] = USERS[username][1]
            return redirect(url_for('home'))
        return render_template('login.html', error='Credenciales incorrectas')
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))


@app.route('/topics')
@login_required
def topics():
    topics_data = load_topics()
    y1_topics = [t for t in topics_data['topics'] if t.get('year') == 'y1']
    y2_topics = [t for t in topics_data['topics'] if t.get('year') == 'y2']
    record_activity_event(
        current_username(),
        'topics_page_view',
        'page',
        object_id='topics',
        object_title='Apuntes',
    )
    return render_template('user/topics.html', y1_pdfs=y1_topics, y2_pdfs=y2_topics)


@app.route('/homework')
@login_required
def homework():
    quiz_data = load_quizzes()
    return render_template('user/homework.html', quizzes=quiz_data['quizzes'])


@app.route('/quiz/<quiz_id>')
@login_required
def take_quiz(quiz_id):
    try:
        quiz_id_str = str(quiz_id)
        quiz_data = load_quizzes()
        quiz = next((q for q in quiz_data['quizzes'] if str(q.get('id')) == quiz_id_str), None)

        if not quiz:
            return render_template(
                'errors/404.html',
                message=f"Quiz ID {quiz_id} no encontrado"
            ), 404

        required_fields = ['id', 'title', 'question_count', 'correct_answers', 'pdfs']
        for field in required_fields:
            if field not in quiz:
                return render_template(
                    'errors/500.html',
                    error=f"Campo requerido faltante: {field}"
                ), 500

        questions_pdf = quiz['pdfs'].get('questions')
        if questions_pdf and not os.path.exists(os.path.join(BASE_DIR, questions_pdf)):
            return render_template(
                'errors/404.html',
                message='Archivo PDF de preguntas no encontrado'
            ), 404

        store_quiz_start_time(quiz_id_str)
        record_activity_event(
            current_username(),
            'quiz_started',
            'quiz',
            object_id=quiz_id_str,
            object_title=quiz['title'],
        )

        return render_template('user/quiz.html', quiz=quiz)
    except Exception as e:
        print(f"Error en take_quiz: {str(e)}")
        return render_template('errors/500.html', error=str(e)), 500


@app.route('/submit-quiz/<quiz_id>', methods=['POST'])
@login_required
def submit_quiz(quiz_id):
    quiz_id_str = str(quiz_id)
    quiz_data = load_quizzes()
    quiz = next((q for q in quiz_data['quizzes'] if str(q.get('id')) == quiz_id_str), None)

    if not quiz:
        return render_template('errors/404.html'), 404

    user_answers = []
    correct_count = 0

    for q_num in range(1, quiz['question_count'] + 1):
        user_answer = request.form.get(f'answer_{q_num}', '')
        correct_answer = quiz['correct_answers'][q_num - 1]
        is_correct = user_answer == correct_answer

        if is_correct:
            correct_count += 1

        user_answers.append({
            'question_num': q_num,
            'user_answer': user_answer,
            'correct_answer': correct_answer,
            'is_correct': is_correct
        })

    score_percentage = (correct_count / quiz['question_count']) * 100
    started_at, duration_seconds = pop_quiz_start_time(quiz_id_str)
    attempt = record_quiz_attempt(
        current_username(),
        quiz_id_str,
        quiz_title=quiz['title'],
        score=round(score_percentage),
        total_questions=quiz['question_count'],
        correct_answers=correct_count,
        percentage=score_percentage,
        started_at=started_at,
        duration_seconds=duration_seconds,
        metadata={'user_answers': user_answers},
    )
    record_activity_event(
        current_username(),
        'quiz_submitted',
        'quiz',
        object_id=quiz_id_str,
        object_title=quiz['title'],
        metadata={
            'attempt_id': attempt.id if attempt else None,
            'correct_answers': correct_count,
            'total_questions': quiz['question_count'],
            'percentage': score_percentage,
        },
        duration_seconds=duration_seconds,
    )

    session['quiz_results'] = {
        'quiz_id': quiz['id'],
        'quiz_title': quiz['title'],
        'user_answers': user_answers,
        'score': score_percentage,
        'correct_count': correct_count,
        'question_count': quiz['question_count'],
        'solutions_pdf': quiz['pdfs']['solutions'],
        'attempt_id': attempt.id if attempt else None
    }

    return redirect(url_for('quiz_results'))


@app.route('/quiz-results')
@login_required
def quiz_results():
    if 'quiz_results' not in session:
        return redirect(url_for('homework'))

    return render_template('user/quiz_results.html', results=session['quiz_results'])


@app.route('/resource/<resource_type>/<resource_id>/<action>')
def tracked_resource(resource_type, resource_id, action):
    if action not in {'open', 'download'}:
        return render_template('errors/404.html'), 404

    resource = find_tracked_resource(resource_type, resource_id)
    if not resource:
        return render_template('errors/404.html'), 404

    username = current_username()
    if username:
        record_resource_access(
            username,
            resource_type,
            action,
            resource_id=resource['id'],
            resource_title=resource['title'],
            path=resource['path'],
        )

        if resource_type == 'topic_pdf':
            mark_topic_opened(username, resource['id'], resource['title'])
            event_type = 'topic_view' if action == 'open' else 'resource_download'
        elif resource_type == 'solution_pdf' and action == 'open':
            event_type = 'solution_viewed'
        else:
            event_type = 'resource_open' if action == 'open' else 'resource_download'

        record_activity_event(
            username,
            event_type,
            resource['object_type'],
            object_id=resource['id'],
            object_title=resource['title'],
            metadata={'resource_type': resource_type, 'action': action},
        )

    return redirect(asset_url(resource['path']))


@app.route('/progress')
@login_required
def progress():
    snapshot = get_user_activity_snapshot(current_username())
    return render_template('user/progress.html', snapshot=snapshot)


@app.route('/miscellaneous')
@login_required
def miscellaneous():
    summaries_data = load_summaries()
    y1_summaries = [s for s in summaries_data['summaries'] if s.get('year') == 'y1']
    y2_summaries = [s for s in summaries_data['summaries'] if s.get('year') == 'y2']
    return render_template(
        'user/miscellaneous.html',
        y1_summaries=y1_summaries,
        y2_summaries=y2_summaries
    )


@app.route('/exams')
def exams():
    exams_data = load_exams()
    y1_exams = [e for e in exams_data['exams'] if e.get('year') == 'y1']
    y2_exams = [e for e in exams_data['exams'] if e.get('year') == 'y2']
    return render_template('user/exams.html', y1_exams=y1_exams, y2_exams=y2_exams)


@app.errorhandler(403)
def forbidden(e):
    return render_template('errors/403.html'), 403


@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def internal_error(e):
    return render_template('errors/500.html'), 500


if __name__ == '__main__':
    os.makedirs(DATA_DIR, exist_ok=True)
    app.run(debug=True)
