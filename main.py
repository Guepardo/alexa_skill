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
        self.app.add_url_rule("/", "index", lambda: render_template("index.html"))

    def register_socket_events(self):
        self.socketio.on_event('my_event', self.on_my_event)
        self.socketio.on_event('my_broadcast_event', self.on_broadcast_event)
        self.socketio.on_event('connect', self.onConnect)
        self.socketio.on_event('disconnect', self.onDisconnect)

    def on_my_event(self, message):
      emit('my_response', {'data': message['data']})

    def on_broadcast_event(self, message):
      emit('my_response', {'data': message['data']}, broadcast=True)

    def onConnect(self, message):
      emit('my_response', {'data': 'Connected'})

    def onDisconnect(self, message):
      print('Client disconnected')

    def run(self):
        self.socketio.run(self.app, host='0.0.0.0')
