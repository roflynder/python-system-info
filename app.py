import json

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

from utils.controller import get_all_info

app = Flask(__name__)
socketio = SocketIO(app)


@app.route("/")
def index():
    return render_template("index.html")


@socketio.on("connect")
def handle_connect():
    socketio.start_background_task(target=send_system_info)


@socketio.on('disconnect')
def handle_disconnect():
    print("Client disconnected")


def send_system_info():
    while True:
        socketio.emit('system info', json.dumps(get_all_info()))
        socketio.sleep(1)


if __name__ == "__main__":
    socketio.run(app, allow_unsafe_werkzeug=True)