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


@app.route('/message', methods=['GET', 'POST'])
@login_required
def message():
    form = MessageForm()

    college_students = list(User.objects(role='College Student'))
    college_student_choices = [(str(user.id), f"{user.fname} {user.lname}") for user in college_students]

    form.recipient.choices = college_student_choices

    if form.validate_on_submit():
        recipient_id = form.recipient.data
        newMessage = Message(
            message=form.message.data,
            recipient_id=recipient_id,
            author=current_user.id,
            create_date=datetime.utcnow()
        )

        newMessage.save()
        socketio.emit('private_message', {'message': form.message.data}, room=recipient_id)
        flash('Your message has been sent!', 'success')
        return redirect(url_for('index'))

    return render_template('privatemessage.html', form=form)



@socketio.on('private_message')
def handle_private_message(data):
    message = data['message']
    recipient_username = request.sid  
    socketio.emit('private_message', {'message': message}, room=recipient_username)
