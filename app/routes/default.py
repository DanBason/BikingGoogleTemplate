from app import app, User
from flask import render_template


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
    users = User.query.all()
    return render_template('users.html', users=users)


@app.route('/test')
def test():
    users = User.objects.all()
    for user in users:
        print(user.fname, user.lname, user.email)

    return render_template("index.html")


