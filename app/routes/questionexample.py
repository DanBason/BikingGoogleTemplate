from flask import Flask, render_template, request, redirect
from classes import Question, Answer
from forms import AnswerForm

app = Flask(__name__)

@app.route('/question/<int:question_id>')
def question(question_id):
    question = Question.get_by_id(question_id)
    answers = Answer.select().where(Answer.question == question).order_by(Answer.timestamp.desc())
    form = AnswerForm()

    return render_template('question.html', question=question, answers=answers, form=form)

@app.route('/question/<int:question_id>/answer', methods=['POST'])
def answer_question(question_id):
    form = AnswerForm(request.form)
    question = Question.get_by_id(question_id)

    if form.validate():
        Answer.create(
            question=question,
            content=form.content.data,
            user='user123' # replace with actual user id or username
        )

    return redirect(f'/question/{question_id}')

if __name__ == '__main__':
    app.run(debug=True)

# This code defines a route for a question page which displays the question and any existing answers to the question. It also provides a form for users to submit new answers to the question. Note that this code assumes the existence of a Question model and an Answer model. You'll need to define these models yourself (and any necessary database tables) based on your specific needs. The AnswerForm referenced in the code is also assumed to be defined elsewhere.