import sys

from src.server import Server

port = sys.argv[1]

Server.run(port)
