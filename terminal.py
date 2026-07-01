from aqt.qt import QDialog, QVBoxLayout, QLabel


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
🪖 ANKARMY COMMAND CENTER
====================================

📡 MISSION
{mission['objective']}

------------------------------------
📊 STATUS
XP: {player.xp}
DISCIPLINE: {player.discipline}
CORRECT: {player.cards_correct}
WRONG: {player.cards_wrong}
====================================
"""
    show_terminal("AnkArmy", content)



def show_end_session(player):
    session_xp = player.cards_correct
    
    session_wrong = player.cards_wrong
    total = session_xp + session_wrong
    accuracy = (session_xp / total) * 100 if total > 0 else 0

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



------------------------------------
🪖 STATUT
Grade: {player.grade}
====================================
"""

    

    show_terminal("AnkArmy - Rapport de mission", content)