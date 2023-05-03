from app import app, socketio
from flask_login.utils import login_required
from flask import render_template, redirect, flash, url_for, request 
from app.classes.data import User, College, Blog, Question, Message
from app.classes.forms import ProfileForm, CollegeForm, SearchForm, BlogForm, QuestionForm, MessageForm
from flask_login import current_user
from flask_socketio import join_room, leave_room, emit, SocketIO
from datetime import datetime




# @app.route('/message_page', methods=['GET', 'POST'])
# @login_required
# def message_new():
#     form = MessageForm()
#     college_students = User.objects(role='college student')
#     college_student_usernames = [user.username for user in college_students]

#     form.recipient.choices = [(username, username) for username in college_student_usernames]
#     return render_template('privatemessage.html', form=form)


from flask_login import current_user, login_required
from app.classes.data import Message
from datetime import datetime

@app.route('/message', methods=['GET', 'POST'])
@login_required
def message():
    if request.method == 'POST':
        recipient_id = request.form['recipient']
        message = request.form['message']
        new_message = Message(
            message=message,
            recipient_id=recipient_id,
            author=current_user.id,
            create_date=datetime.utcnow()
        )
        new_message.save()
        socketio.emit('private_message', {'message': message}, room=recipient_id)
        flash('Your message has been sent!', 'success')
        return redirect(url_for('index'))
    else:
        college_students = User.objects(role='College Student')
        return render_template('message.html', college_students=college_students)

