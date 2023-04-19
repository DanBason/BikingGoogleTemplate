from app import app
from flask_socketio import SocketIO
import os
from app import socketio


if __name__ == "__main__":
    
    os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'
    socketio.run(app)
    
    # app.run(debug="True", ssl_context='adhoc')
    app.run(debug="True",use_reloader=True, ssl_context=('cert.pem', 'key.pem'))