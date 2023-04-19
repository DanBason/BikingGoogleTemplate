from app import app
from flask_login.utils import login_required
from flask import render_template, redirect, flash, url_for, request
from app.classes.data import User, College, Blog, Question
from app.classes.forms import ProfileForm, CollegeForm, SearchForm, BlogForm, QuestionForm
from flask_login import current_user

@app.route('/message/<recipient_id>')
def message_user(recipient_id):
    sender = User.objects.get(id=recipient_id)
    
    return render_template('privatemessage.html', sender=sender)