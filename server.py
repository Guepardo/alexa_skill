from flask import Flask, render_template
from flask_socketio import SocketIO, emit


class Server:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config['SECRET_KEY'] = 'secret!'
        self.socketio = SocketIO(self.app)

        self.register_socket_events()
        self.register_views()

    def register_views(self):
        self.app.add_url_rule("/tasks", "handle_create_task",
                              self.handle_create_task, methods=['POST'])

    def handle_create_task(self, data=None,):
        self.socketio.emit('new_task', {'data': data})
        return '', 204

    def register_socket_events(self):
        self.socketio.on_event('connect', self.on_connect)
        self.socketio.on_event('disconnect', self.on_disconnect)

    def on_connect(self, message):
        emit('my_response', {'data': 'Connected'})

    def on_disconnect(self, message):
        print('Client disconnected')

    def run(self):
        self.socketio.run(self.app, host='0.0.0.0', debug=True)
