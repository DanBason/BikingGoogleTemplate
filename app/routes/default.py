from app import app
from flask import render_template
from app.classes.data import User


# This is for rendering the home page
@app.route('/aboutus')
def AboutUs():
    return render_template('aboutus.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/question')
def questionpage():
    return render_template('questions.html')
    
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
    users = User.objects.all()
    for user in users:
        print(user.fname, user.lname, user.email, user_id)

    return render_template("index.html")

@app.route('/users/<userID>')
def user_profile(userID):
    user = User.query.filter_by(id=userID).first()
    return render_template('user_profile.html', user=user)


