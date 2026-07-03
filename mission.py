import random

def generate_mission(player):
    mission_type = random.choice([
        "cards",
        "accuracy",
        "no_mistake",
        "streak",
    ])

    if mission_type == "cards":
        target = random.randint(20, 35)
        return {
            "type": "cards",
            "when": "during",
            "objective": f"Réviser {target} cartes",
            "target": target,
        }

    elif mission_type == "accuracy":
        return {
            "type": "accuracy",
            "when": "end",
            "objective": "Atteindre 90 % de réussite",
            "target": 90,
        }

    elif mission_type == "no_mistake":
        return {
            "type": "no_mistake",
            "when": "end",
            "objective": "Terminer la session sans erreur",
        }

    elif mission_type == "streak":
        target = random.randint(10, 20)
        return {
            "type": "streak",
            "when": "during",
            "objective": f"Réussir {target} cartes d'affilée",
            "target": target,
        }