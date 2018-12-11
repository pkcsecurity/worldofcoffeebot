from websocket_server import WebsocketServer
from threading import Thread
import time
from board import Board
from player import Player
import json
import pprint
import utils

pprint = pprint.PrettyPrinter(indent=4)

TICK_FREQ = 5

players = {}
bullets = []


# Add player to the player list.
def new_client(client, server):
    cid = client['id']
    print("New player connected and was given id %d" % cid)
    players[cid] = Player(x=5, y=5, pid=cid)


# Remove player from the players list
def client_left(client, server):
    cid = client['id']
    print("Client(%d) disconnected" % cid)
    del players[cid]


# Update player data based on what client is sending
def message_received(client, server, message):
    cid = client['id']
    print("Client(%d) sent: %s" % (cid, message))
    m = json.loads(message)

    players[cid].update(m['move'], m['face'], m['attacking'])


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
        player.tick(game_board, bullets)


def update_all_bullets():
    global bullets

    for b in bullets:
        b.tick(game_board)

    bullets = [b for b in bullets if b.exists]


def send_state_to_all_players():
    for client in server.clients:
        server.send_message(client, json.dumps({'pid': client['id'],
                                                'players': list(players.values()),
                                                'bullets': list(bullets),
                                                'board': game_board.board, },
                                               default=utils.serialize))


def game_loop():
    global server, players, bullets

    while True:
        print('Clients currently connected: {}'.format(server.clients))

        update_all_players()

        update_all_bullets()

        send_state_to_all_players()

        # server.send_message_to_all(json.dumps({'players': list(players.values()),'bullets': list(bullets),'board': game_board.board, },default=utils.serialize))

        time.sleep(1/TICK_FREQ)


game_loop_thread = Thread(target=game_loop)
game_loop_thread.start()

server.run_forever()
