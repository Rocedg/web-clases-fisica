from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# === 1) HOME PAGE ===
@app.route('/')
def home():
    return render_template('home.html')

# === 2) TOPICS/LESSONS PAGE ===
@app.route('/topics')
def topics():
    # This page could list your PDF notes, formula summaries, etc.
    # You can either host the PDFs directly in static or link them from OneDrive.
    # Example (just passing a list of PDFs to the template):
    pdfs = [
        {'title': 'Movimiento Rectilíneo', 'url': 'static/pdfs/movimiento_rectilineo.pdf'},
        {'title': 'Fuerzas y Leyes de Newton', 'url': 'static/pdfs/fuerzas_leyes_newton.pdf'},
        # ...
    ]
    return render_template('topics.html', pdfs=pdfs)

# === 3) HOMEWORK/QUIZZES ===
@app.route('/homework', methods=['GET', 'POST'])
def homework():
    # If GET: show quiz form
    # If POST: evaluate answers, show score, let user download correction PDF
    if request.method == 'POST':
        # Evaluate answers logic
        # ...
        score = 0  # Example
        # Show results:
        return render_template('homework.html', score=score, submitted=True)
    else:
        return render_template('homework.html', submitted=False)

# === 4) RECORDED CLASSES ===
@app.route('/recorded')
def recorded():
    # embed OneDrive or YouTube videos here
    # example list:
    videos = [
        {'title': 'Clase 1: Introducción', 'embed_url': 'https://onedrive.live.com/embed?resId=XXXX'},
        # ...
    ]
    return render_template('recorded.html', videos=videos)

# === 5) SOLVED EXAMS ===
@app.route('/solved_exams')
def solved_exams():
    # Similar to topics, might just be a list of PDF solutions
    solutions = [
        {'title': 'Examen 1 (2023)', 'url': 'static/pdfs/solucion_examen_1.pdf'},
        # ...
    ]
    return render_template('solved_exams.html', solutions=solutions)

if __name__ == '__main__':
    # For local dev
    app.run(debug=True)
