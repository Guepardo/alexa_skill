from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask import request

class Server:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config['SECRET_KEY'] = 'secret!'
        self.socketio = SocketIO(self.app)

        self.register_socket_events()
        self.register_views()

    def register_views(self):
        self.app.add_url_rule("/tasks", "handle_create_task",
                              view_func=self.handle_create_task, methods=['POST'])

    def handle_create_task(self):
        print(request.json)
        self.socketio.emit('new_task', request.json)
        return '', 204

    def register_socket_events(self):
        self.socketio.on_event('connect', self.on_connect)
        self.socketio.on_event('disconnect', self.on_disconnect)

    def on_connect(self, message):
        emit('my_response', {'data': 'Connected'})

    def on_disconnect(self, message):
        print('Client disconnected')

    def run(self):
        self.socketio.run(self.app, host='0.0.0.0', allow_unsafe_werkzeug=True)
