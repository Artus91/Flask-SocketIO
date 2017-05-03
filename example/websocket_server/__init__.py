from flask import Flask, render_template
from flask_socketio import SocketIO, emit

async_mode = None
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)