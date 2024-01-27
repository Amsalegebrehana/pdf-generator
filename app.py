from flask import Flask, render_template, request, jsonify
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
    print(answers)
    json_answers = jsonify(answers)
    print(json_answers)

    return f"Answers collected: {answers}"


def generate_pdf(user_response):
    canvas = Canvas('user_response.pdf')
    horizontal = vertical = 72
    for qn, ans in user_response:
        if ans == 'yes':
            canvas.drawString(horizontal, vertical, f"${qn} - ${ans}")
            vertical -= 1
    canvas.save()



if __name__ == '__main__':
    app.run(debug=True)

