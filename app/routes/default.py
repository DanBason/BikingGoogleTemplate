from app import app
from flask import render_template, Flask, redirect, url_for
from app.classes.data import User, Question, College
from app.classes.forms import QuestionForm, CollegeForm


# This is for rendering the home page
@app.route('/aboutus')
def AboutUs():
    return render_template('aboutus.html')

@app.route('/')
def index():
    return render_template('index.html')





    
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/parents')
def parents():
    return render_template('parents.html')

# the route to all the displayed alumni data
@app.route('/student_view')
def college_students():
    students = User.objects(role='college student')
    return render_template('student_view.html', students=students)


@app.route('/test')
# this was just to figure out a error, it can be deleted
def test():
    questions = Question.objects.all()
    for question in questions:
        print(question.author.fname, question.subject)

    return render_template("index.html")






