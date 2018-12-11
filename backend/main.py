from websocket_server import WebsocketServer
from threading import Thread
import time
from board import Board
from player import Player
import json
import pprint
import utils

pprint = pprint.PrettyPrinter(indent=4)
players = {}
bullets = []


# Called for every client connecting (after handshake)
def new_client(client, server):
    cid = client['id']
    print("New player connected and was given id %d" % cid)
    players[cid] = Player(x=5, y=5, pid=cid)


# Called for every client disconnecting
def client_left(client, server):
    cid = client['id']
    print("Client(%d) disconnected" % cid)
    del players[cid]


# Called when a client sends a message
def message_received(client, server, message):
    if len(message) > 200:
        message = message[:200]+'..'
    print("Client(%d) said: %s" % (client['id'], message))


PORT = 9001
server = WebsocketServer(PORT)
server.set_fn_new_client(new_client)
server.set_fn_client_left(client_left)
server.set_fn_message_received(message_received)

# init board
game_board = Board(n=10, m=10)
game_board.add_wall_borders()
print(game_board)


def update_all_players():
    for player in players.values():
        player.tick(game_board)


def game_loop():
    global server
    while True:
        print('Clients currently connected: {}'.format(server.clients))

        update_all_players()

        server.send_message_to_all(json.dumps(list(players.values()), default=utils.serialize))
        time.sleep(0.5)


game_loop_thread = Thread(target=game_loop)
game_loop_thread.start()

server.run_forever()
