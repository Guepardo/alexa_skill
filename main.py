import sys
from server import Server
from client import Client

start_mode = sys.argv[1]

print(sys.argv)

if "__main__" == __name__:
    if start_mode == 'server':
        Server().run()

    if start_mode == 'client':
        Client().run()
