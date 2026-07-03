import random

def generate_mission(player):
    base = 20
    mi=base+random.randint(10,15)
    print("mission générée")
    return {
        "objective": f"Réviser {mi} cartes",
        "target": mi
    }