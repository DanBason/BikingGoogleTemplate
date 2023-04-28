from app import app
from flask import render_template, Flask, redirect, url_for
from flask_login import current_user
from app.classes.data import User, Question, College
from app.classes.forms import QuestionForm, CollegeForm



# This is for rendering the home page
@app.route('/aboutus')
def AboutUs():
    return render_template('aboutus.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inbox')
def inbox():
    return render_template('inboxmy.html', fname = current_user.fname)





    
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/parents')
def parents():
    return render_template('parents.html')

# the route to all the displayed alumni data
@app.route('/student_view')
def college_students():
    students = User.objects(role='College Student').all()
    for student in students:
        student.colleges = College.objects(author=student).all()
    return render_template('student_view.html', students=students)



@app.route('/test')
# this was just to figure out a error, it can be deleted
def test():
    questions = Question.objects.all()
    for question in questions:
        print(question.author.fname, question.subject)

    return render_template("index.html")




@app.route('/socket/<user_username>')
def user_messaging(user_id):
    user = User.objects.get(id=user_id)
    
    
    return render_template('privatemessage.html', user_username = user.username, )

    

