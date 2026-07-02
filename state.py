import json
import os
from .player import Player
SAVE_PATH = os.path.join(os.path.dirname(__file__), "data", "save.json")
DEBUG_PATH = os.path.join(os.path.dirname(__file__), "debug.log")

def load_player()-> Player:
    if not os.path.exists(SAVE_PATH) or os.path.getsize(SAVE_PATH) == 0:
        print(os.path.getsize(SAVE_PATH))
        print('fichier inexistant ou vide')
        return Player()
    
    try:
        with open(SAVE_PATH, "r") as f:
            data = json.load(f)
            return Player.from_dict(data)

    except Exception as e:
        with open(DEBUG_PATH, "a") as f:
            f.write(str(e)+"\n")
        print(str(e))
        return Player()

    

def save_player(player:Player):
    os.makedirs(os.path.dirname(SAVE_PATH), exist_ok=True)

    with open(SAVE_PATH, "w") as f:
        json.dump(player.to_dict(), f, indent=4)