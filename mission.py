import random

def generate_mission(player):
    base = 20

    if player.discipline < 80:
        base -= 5

    return {
        "objective": f"Réviser {base} cartes",
        "target": base
    }