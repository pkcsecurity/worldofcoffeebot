from websocket_server import WebsocketServer
from threading import Thread
import time


# Called for every client connecting (after handshake)
def new_client(client, server):
    print("New client connected and was given id %d" % client['id'])
    server.send_message_to_all("Hey all, a new client has joined us")


# Called for every client disconnecting
def client_left(client, server):
    print("Client(%d) disconnected" % client['id'])


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


def game_loop():
    global server
    while True:
        print('Clients currently connected: {}'.format(server.clients))
        time.sleep(2)


game_loop_thread = Thread(target=game_loop)
game_loop_thread.start()

server.run_forever()
