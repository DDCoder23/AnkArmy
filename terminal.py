from aqt.qt import QDialog, QVBoxLayout, QLabel
from aqt import mw

def show_terminal(title, content):
    dialog = QDialog()
    dialog.setWindowTitle(title)

    layout = QVBoxLayout()

    label = QLabel(content)
    label.setStyleSheet("""
        font-family: monospace;
        background-color: black;
        color: #00ff00;
        padding: 10px;
    """)

    layout.addWidget(label)
    dialog.setLayout(layout)

    dialog.exec()
def show_session(player, mission):
    content = f"""
====================================
🪖 ANKARMY AIR COMMAND - TERMINAL SYSTEM
====================================

📡 MISSION
{mission['objective']}

------------------------------------
📊 STATUS
XP: {player.xp}
DISCIPLINE: {player.discipline}
Nombre total de mission : {player.total_mission}
Mission réussie : {player.mission_réussie}
Pourcentage de réussite : {player.pourcentage_de_réussite}% 
====================================
"""
    show_terminal("AnkArmy", content)



def show_end_session(player):
    session_xp = player.cards_correct
    
    session_wrong = player.cards_wrong
    total = session_xp + session_wrong
    accuracy = (session_xp / total) * 100 if total > 0 else 0
    état= "complète" if player.mission_completed else "incomplète"
    content = f"""
====================================
📦 RAPPORT DE MISSION
====================================

📊 RÉSULTATS
XP TOTAL: {player.xp}
DISCIPLINE: {player.discipline}

📈 SESSION
✔ Correctes: {player.cards_correct}
✘ Erreurs: {player.cards_wrong}
Accuracy : {accuracy} 
Etat de la mission : {état}  




------------------------------------
🪖 STATUT
Grade: {player.grade}
Nombre total de mission : {player.total_mission}
Mission réussie : {player.mission_réussie}
Pourcentage de réussite : {player.pourcentage_de_réussite}% 
====================================
"""
    show_terminal("AnkArmy", content)


def show_boot(player):
     username = mw.pm.name
     discipline="STABLE" if player.discipline >= 75 else "WARNING"
     content = f"""
====================================
🪖 ANKARMY AIR COMMAND - TERMINAL SYSTEM
====================================
Connexion au Commandement...
Vérification du dossier...
Accès autorisé.
Bienvenue, {player.grade}.
STATUS : CONNECTED
USER   : {username}
RANK   : {player.grade}
DISCIPLINE  : {discipline}
------------------------------------
📊 STATUS
XP: {player.xp}
DISCIPLINE: {player.discipline}
Nombre total de mission : {player.total_mission}
Mission réussie : {player.mission_réussie}
Pourcentage de réussite : {player.pourcentage_de_réussite}% 
Tous les systèmes sont opérationnels.
En attente des ordres...
====================================
"""
     show_terminal("AnkArmy", content)
    
    