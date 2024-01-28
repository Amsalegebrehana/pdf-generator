import random
from flask import Flask, render_template, request, jsonify, redirect, url_for, send_from_directory
from reportlab.pdfgen.canvas import Canvas

app = Flask(__name__)

@app.route('/')
def form_page():
    return render_template('index.html')

@app.route('/process_form', methods=['POST'])
def process_form():
    answers = []
    for question_number in range(1, 5):
        answer = request.form.get(f'answer{question_number}')
        answers.append({
            "questionnumber": question_number,
            "answer": answer
        })

    # You can now use 'answers' as a list of dictionaries containing question and answer pairs
    # Convert answers to JSON format if needed
    file_directory = generate_pdf(answers)
    # return f"Answers collected: {answers}"
    return redirect(url_for('pdfviewer', directory=file_directory))

@app.route('/<directory>')
def pdfviewer(directory):
    path = app.root_path
    return send_from_directory(path,directory,mimetype='application/pdf')

def generate_pdf(user_response):
    name_int = random.randint(1, 1000000) 
    name = f"{name_int}.pdf"
    canvas = Canvas(name)
    horizontal, vertical = 72, 800
    for data in user_response:
        qn, ans = data['questionnumber'], data['answer']
        if ans == 'yes':
            canvas.drawString(horizontal, vertical, f"{qn} - {ans}")
            vertical -= 18
        if vertical < 20:
            canvas.showPage()
    canvas.showPage()
    canvas.save()
    return name



if __name__ == '__main__':
    app.run(debug=True)

