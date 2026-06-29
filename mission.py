import random

def generate_mission(state):
    base = 20

    if state["discipline"] < 80:
        base -= 5

    return {
        "objective": f"Réviser {base} cartes",
        "target_cards": base
    }