from app import app

from flask import render_template
from flask_login import (
    current_user,
    login_required,
    login_user,
    logout_user,
)
from oauthlib.oauth2 import WebApplicationClient


# This is for rendering the home page
app.route('/new_question')
@login_required
def new_question():
    return render_template('new_question.html')

app.route('/new_answer')
@login_required
def new_answer():
    return render_template('new_answer.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profilemy')
@login_required
def profile():
    return render_template('profilemy.html')

@app.route('/college')
def college():
    return render_template('college.html')

@app.route('/collegeq')
def collegeq():
    return render_template('collegeq.html')

@app.route('/message')
@login_required
def message():
    
    return render_template('message.html')

@app.route('/collegelist')
def collegelist():
    return render_template('collegelist.html')

@app.route('/questionpage')
def questionpage():
    return render_template('questionpage.html')


