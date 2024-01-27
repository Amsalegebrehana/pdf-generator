from flask import Flask, render_template, request, jsonify

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

if __name__ == '__main__':
    app.run(debug=True)

