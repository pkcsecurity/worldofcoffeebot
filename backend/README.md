# World of Coffee Backend

## How to run

1. Make sure you have python3 installed
1. Run `$ pip3 install -r requirements.txt`
1. Run `$ python3 main.py`

## To talk to the backend
```json
{
   "move":[
      1,
      0
   ],
   "face":[
      -1,
      0
   ],
   "attacking":true
}
```

* Send JSON that is formatted like above in the websocket message. 
* This will update your player's current action in the backend.
* `move` is a unit vector describing which direction the player will move.
** `[0, 0]` should be sent if the player should be standing still.
* `face` is a unit vector describing the direction in which projectiles will move when shot by the player.
** `[0, 0]` is not a valid direction here.
* `attacking` is a boolean that tells the backend if the player is attacking.
