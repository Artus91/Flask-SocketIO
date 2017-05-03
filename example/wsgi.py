from websocket_server import app, socketio
from websocket_server import main_http, main_socket

if __name__ == '__main__':
    socketio.run(app, debug=True)
