from flask import Flask, render_template, request, redirect, url_for, session
from functools import wraps
import os
import json
import uuid
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'
app.config.update(
    QUIZZES_FILE='data/quizzes.json',
    UPLOAD_FOLDER='static/pdfs/quizzes',
    ALLOWED_EXTENSIONS={'pdf'}
)

# Load quiz data from JSON
def load_quizzes():
    try:
        with open('data/quizzes.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # Return empty structure if file doesn't exist or is invalid
        return {"quizzes": []}

# Hardcoded users (username: [password, role])
USERS = {
    'admin': ['adminpass', 'admin'],
    'Paul': ['fisica2026', 'student'],
    'Guest': ['studentpass', 'student']
}

# Security decorators
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('role') != 'admin':
            return render_template('errors/403.html'), 403
        return f(*args, **kwargs)
    return decorated_function

# Routes
# === 1) ENTRY MENU ===
@app.route('/')
def home():
    return render_template('home.html')

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

# === 2) LESSONS REPOSITORY ===
@app.route('/topics')
@login_required
def topics():
    pdfs = [
        {
            'title': 'TEMA 0: Temas introductorios',
            'url': 'static/pdfs/T0-Introducción.pdf',
            'description': 'Bases de conceptos dimensionales y cálculo vectorial'
        },
        {
            'title': 'TEMA 1: Movimiento rectilínea',
            'url': 'static/pdfs/T1-Movimiento-rectilíneo.pdf',
            'description': 'Movimiento uniforme, definiendo velocidad y aceleración, MRUA y comprensión gráfica básica'
        },
        {
            'title': 'TEMA 2: Movimiento en el plano',
            'url': 'static/pdfs/T2-Movimiento-en-el-plano.pdf',
            'description': 'Composición de movimiento, tiros parabólicos, MCU y MCUA',
        },
        {
            'title': 'TEMA 3: Leyes de Newton',
            'url': 'static/pdfs/T3-Leyes-de-Newton.pdf',
            'description': 'Diagramas de cuerpos libres, esquema de interacciones, principio de inercia, principio fundamental de la dinámica y principio de acción-reacción'
        },
        {
            'title': 'TEMA 4: Fuerzas centrales',
            'url': 'static/pdfs/T4-Fuerzas-centrales.pdf',
            'description': 'Fundamentos del movimiento en una dimensión'
        },
        {
            'title': 'TEMA 5: Energía y trabajo',
            'url': 'static/pdfs/T5-Energía-y-trabajo.pdf',
            'description': 'Energía cinética, energía potencial, trabajo, fuerzas conservativas, conservación de energía'
        },
        {
            'title': 'TEMA 6: Momento lineal',
            'url': 'static/pdfs/T6-Momento-lineal.pdf',
            'description': 'Cantidad de movimiento, impulso mecánico, conservación momento lineal, colisiones (choques elásticos e inelásticos'
        }
    ]
    
    return render_template('user/topics.html', pdfs=pdfs)

# === 3) EXERCISES INFRASTRUCTURE ===
@app.route('/homework')
@login_required
def homework():
    quiz_data = load_quizzes()
    return render_template('user/homework.html', quizzes=quiz_data['quizzes'])

@app.route('/quiz/<int:quiz_id>')
@login_required
def take_quiz(quiz_id):
    quiz_data = load_quizzes()
    quiz = next((q for q in quiz_data['quizzes'] if q['id'] == quiz_id), None)
    
    if not quiz:
        return render_template('errors/404.html'), 404
        
    return render_template('user/quiz.html', quiz=quiz)

@app.route('/submit-quiz/<int:quiz_id>', methods=['POST'])
@login_required
def submit_quiz(quiz_id):
    quiz_data = load_quizzes()
    quiz = next((q for q in quiz_data['quizzes'] if q['id'] == quiz_id), None)
    
    if not quiz:
        return render_template('errors/404.html'), 404
    
    # Process user answers
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
    
    # Calculate score
    score = (correct_count / quiz['question_count']) * 10
    
    # Store results in session
    session['quiz_results'] = {
        'quiz_id': quiz_id,
        'quiz_title': quiz['title'],
        'user_answers': user_answers,
        'score': score,
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

@app.route('/admin/dashboard')
@login_required
@admin_required
def admin_dashboard():
    quiz_data = load_quizzes()
    return render_template('admin/dashboard.html', quizzes=quiz_data['quizzes'])
    
    
# Helper functions
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def get_quizzes():
    if os.path.exists(app.config['QUIZZES_FILE']):
        with open(app.config['QUIZZES_FILE'], 'r') as f:
            return json.load(f)
    return {"quizzes": []}

def save_quizzes(data):
    with open(app.config['QUIZZES_FILE'], 'w') as f:
        json.dump(data, f, indent=2)

# Admin quiz management
@app.route('/add-quiz', methods=['POST'])
@login_required
@admin_required
def add_quiz():
    try:
        quizzes_data = get_quizzes()
        new_id = str(uuid.uuid4())[:8]  # Generate short unique ID
        
        # Validate form data
        title = request.form.get('title')
        question_count = int(request.form.get('question_count'))
        avg_time = int(request.form.get('avg_time'))
        answers = [a.strip().upper() for a in request.form.get('correct_answers').split(',')]
        
        if not all(a in ['A', 'B', 'C', 'D'] for a in answers):
            raise ValueError("Solo se permiten respuestas A, B, C o D")
            
        if len(answers) != question_count:
            raise ValueError("El número de respuestas debe coincidir con el número de preguntas")

        # Handle file uploads
        questions_pdf = request.files['questions_pdf']
        solutions_pdf = request.files['solutions_pdf']
        
        if not (allowed_file(questions_pdf.filename) and allowed_file(solutions_pdf.filename)):
            raise ValueError("Solo se permiten archivos PDF")

        # Create quiz directory
        quiz_folder = os.path.join(app.config['UPLOAD_FOLDER'], new_id)
        os.makedirs(quiz_folder, exist_ok=True)

        # Save PDFs
        questions_path = os.path.join(quiz_folder, 'preguntas.pdf')
        solutions_path = os.path.join(quiz_folder, 'soluciones.pdf')
        questions_pdf.save(questions_path)
        solutions_pdf.save(solutions_path)

        # Add to JSON
        new_quiz = {
            "id": new_id,
            "title": title,
            "question_count": question_count,
            "avg_time": avg_time,
            "correct_answers": answers,
            "pdfs": {
                "questions": questions_path,
                "solutions": solutions_path
            }
        }
        
        quizzes_data['quizzes'].append(new_quiz)
        save_quizzes(quizzes_data)
        
        return redirect(url_for('admin_dashboard'))
        
    except Exception as e:
        return render_template('admin/dashboard.html',
                            error=str(e),
                            quizzes=get_quizzes()['quizzes'])

# === *) RECORDED CLASSES ===
@app.route('/recorded')
def recorded():
    # Instead of actual content, return a 404 error page since this section is under construction
    return render_template('errors/404.html'), 404

# === *) SOLVED EXAMS ===
@app.route('/solved')
def solved():
    # Instead of actual content, return a 404 error page since this section is under construction
    return render_template('errors/404.html'), 404

# Error handlers
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
    # Create data directory if it doesn't exist
    os.makedirs('data', exist_ok=True)
    app.run(debug=True)