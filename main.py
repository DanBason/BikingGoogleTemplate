from app import app
from flask_socketio import SocketIO
import os



# if __name__ == "__main__":
    
#     os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'
    
    
#     app.run(debug="True", ssl_context='adhoc')
#     app.run(debug="True",use_reloader=True, ssl_context=('cert.pem', 'key.pem'))


socketio = SocketIO(app)

if __name__ == "__main__":
    socketio.run(app, debug=True, use_reloader=True, ssl_context=('cert.pem', 'key.pem'))