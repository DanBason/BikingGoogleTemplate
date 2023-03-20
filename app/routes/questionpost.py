from flask import render_template, request, redirect, url_for
from app import app, db
from classes import Question, Answer
from forms import QuestionForm, AnswerForm

@app.route('question/new', methods=['GET', 'POST'])
def new_question():
    form = QuestionForm()
    if form.validate_on_submit():
        question = Question(title=form.title.data, content=form.content.data)
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('question', question_id=question.id))
    return render_template('new_question.html', form=form)

@app.route('/question/<int:question_id>/answer', methods=['GET', 'POST'])
def new_answer(question_id):
    form = AnswerForm()
    if form.validate_on_submit():
        answer = Answer(content=form.content.data, question_id=question_id)
        db.session.add(answer)
        db.session.commit()
        return redirect(url_for('question', question_id=question_id))
    return render_template('new_answer.html', form=form)
