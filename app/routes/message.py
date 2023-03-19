
from app import app
import mongoengine.errors
from flask import render_template, flash, redirect, url_for
from flask_login import current_user
from app.classes.data import Blog, Comment
from app.classes.forms import BlogForm, CommentForm
from flask_login import login_required
import datetime as dt
from flask import Flask, render_template, request
from flask_socketio import SocketIO, send, emit 

current_username = []

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
# need to connect the logged in user to users


@app.route('/')
def index():
    return render_template('message.html')

@socketio.on('connect')
def handle_connect():
    print(f"User connected with session id: {request.sid}")

@socketio.on('disconnect')
def handle_disconnect():
    for user in users:
        if user['sid'] == request.sid:
            users.remove(user)
            print(f"User {user['username']} disconnected")
            break
    print(f"User disconnected with session id: {request.sid}")

@socketio.on('login')
def handle_login(data):
    username = data['username']
    user = {'sid': request.sid, 'username': username}
    users.append(user)
    emit('login_successful', {'username': username})
    print(f"User {username} logged in with session id: {request.sid}")

@socketio.on('send_message')
def handle_message(data):
    sender_username = data['sender_username']
    recipient_username = data['recipient_username']
    message = data['message']
    for user in users:
        if user['username'] == recipient_username:
            emit('message', {'sender_username': sender_username, 'message': message}, room=user['sid'])
            break

if __name__ == '__main__':
    socketio.run(app)
