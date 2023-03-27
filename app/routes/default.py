from app import app
from flask import render_template
from app.classes.data import User, Question
from app.classes.forms import QuestionForm


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

@app.route('/users')
def users():
    users = User.objects(college_roles="College Student")
    return render_template('users.html', users=users)


@app.route('/test')
# this was just to figure out a error, it can be deleted
def test():
    questions = Question.objects.all()
    for question in questions:
        print(question.author.fname, question.subject)

    return render_template("index.html")

@app.route('/users/<userID>')
def user_profile(userID):
    user = User.query.filter_by(id=userID).first()
    return render_template('user_profile.html', user=user)


