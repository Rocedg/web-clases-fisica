from flask import Flask, render_template, request, redirect, url_for, session
from functools import wraps
import os
import json

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# Hardcoded users (username: [password, role])
USERS = {
    'Paul': ['fisica2026', 'student'],
    'Guest': ['studentpass', 'student']
}

# Security decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Load topics data from JSON
def load_topics():
    try:
        with open('data/topics.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # Return empty structure if file doesn't exist or is invalid
        return {"topics": []}

# Load quiz data from JSON
def load_quizzes():
    try:
        if not os.path.exists('data/quizzes.json'):
            with open('data/quizzes.json', 'w') as f:
                json.dump({"quizzes": []}, f)
                
        with open('data/quizzes.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            
            # Validate quizzes structure
            valid_quizzes = []
            for quiz in data.get('quizzes', []):
                if all(key in quiz for key in ['id', 'title', 'question_count', 'correct_answers', 'pdfs']):
                    valid_quizzes.append(quiz)
                else:
                    print(f"⚠️ Quiz inválido omitido: {quiz.get('title', 'Sin título')}")
                    
            return {"quizzes": valid_quizzes}
            
    except Exception as e:
        print(f"❌ Error cargando quizzes: {str(e)}")
        return {"quizzes": []}

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
    topics_data = load_topics()
    return render_template('user/topics.html', pdfs=topics_data['topics'])

# === 3) EXERCISES INFRASTRUCTURE ===
@app.route('/homework')
@login_required
def homework():
    quiz_data = load_quizzes()
    return render_template('user/homework.html', quizzes=quiz_data['quizzes'])

@app.route('/quiz/<quiz_id>')
@login_required
def take_quiz(quiz_id):
    try:
        quiz_data = load_quizzes()
        quiz = next((q for q in quiz_data['quizzes'] if q.get('id') == quiz_id), None)
        
        if not quiz:
            return render_template('errors/404.html', 
                                message=f"Quiz ID {quiz_id} no encontrado"), 404
            
        # Validate quiz structure
        required_fields = ['id', 'title', 'question_count', 'correct_answers', 'pdfs']
        for field in required_fields:
            if field not in quiz:
                return render_template('errors/500.html',
                                    error=f"Campo requerido faltante: {field}"), 500
                
        # Validate PDF files exist
        if not all(os.path.exists(path) for path in quiz['pdfs'].values()):
            return render_template('errors/404.html',
                                message="Archivos PDF asociados no encontrados"), 404
            
        return render_template('user/quiz.html', quiz=quiz)
        
    except Exception as e:
        return render_template('errors/500.html', error=str(e)), 500

@app.route('/submit-quiz/<quiz_id>', methods=['POST'])
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
    
    # Calculate score as percentage (0-100)
    score_percentage = (correct_count / quiz['question_count']) * 100
    
    # Store results in session for immediate display
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

# === 4) MISCELLANEOUS INFORMATION ===
@app.route('/miscellaneous')
@login_required
def miscellaneous():
    return render_template('user/miscellaneous.html')

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