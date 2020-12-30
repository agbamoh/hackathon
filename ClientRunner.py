import sys

from src.client import Client

port = sys.argv[1]
server_ip = sys.argv[2]
team_name = sys.argv[3]


Client.run(port, server_ip, team_name)
