import json
import os

SAVE_PATH = os.path.join(os.path.dirname(__file__), "data", "save.json")


def load_state():
    if not os.path.exists(SAVE_PATH):
        return {
            "xp": 0,
            "discipline": 100,
            "cards_correct": 0,
            "cards_wrong": 0
        }
    try:
        with open(SAVE_PATH, "r") as f:
            return json.load(f)

    except:
        save_state(DEFAULT_STATE)
        return DEFAULT_STATE.copy()

    

def save_state(state):
    os.makedirs(os.path.dirname(SAVE_PATH), exist_ok=True)

    with open(SAVE_PATH, "w") as f:
        json.dump(state, f, indent=4)