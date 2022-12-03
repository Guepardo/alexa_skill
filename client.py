from utils import shell
from commands.locator import Locator

import socketio


class Client:
    def __init__(self):
        self.socket = socketio.Client()
        self.register_socket_events()

        self.socket.connect("https://alexa.pokefat.ml")

    def register_socket_events(self):
        self.socket.on('connect', handler=self.on_connect)
        self.socket.on('disconnect', handler=self.on_disconnect)
        self.socket.on('new_task', handler=self.on_new_task)

    def on_new_task(self, data):
        locator = Locator()

        kind = data['kind']
        command_number = data['command_number']

        command = locator.find(command_number)

        command.execute()

        shell(
            f"""notify-send -t 0 "Alexa: kind: {kind}, command number: {command_number}" """)

    def on_connect(self):
        print("Connected")

    def on_disconnect(self):
        print('Disconnected')

    def run(self):
        self.socket.wait()
