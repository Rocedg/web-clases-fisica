from functools import wraps
import json
import os

from flask import Flask, redirect, render_template, request, session, url_for


app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key')

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


@app.context_processor
def inject_layout_context():
    return {
        'asset_url': asset_url,
        'nav_items': NAV_ITEMS
    }


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
    session['quiz_results'] = {
        'quiz_id': quiz['id'],
        'quiz_title': quiz['title'],
        'user_answers': user_answers,
        'score': score_percentage,
        'correct_count': correct_count,
        'question_count': quiz['question_count'],
        'solutions_pdf': quiz['pdfs']['solutions']
    }

    return redirect(url_for('quiz_results'))


@app.route('/quiz-results')
@login_required
def quiz_results():
    if 'quiz_results' not in session:
        return redirect(url_for('homework'))

    return render_template('user/quiz_results.html', results=session['quiz_results'])


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
