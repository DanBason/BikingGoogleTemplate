from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('messageroom.html')

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)
    emit('response', message, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
