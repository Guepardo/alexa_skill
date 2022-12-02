import sys
from server import Server
from client import Client

server = Server()
server.run()

start_mode = sys.agv[1]

if "__main__" == __name__:
    if start_mode == 'server':
        Server().run()

    if start_mode == 'client':
        Client().run()
