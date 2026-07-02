import random

def generate_mission(player):
    base = 20

    print("mission générée")
    return {
        "objective": f"Réviser {base+random.randint(10,15} cartes",
        "target": base
    }