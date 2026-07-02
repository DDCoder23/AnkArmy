from aqt import mw
from aqt.qt import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QApplication,
)
from PyQt6.QtMultimedia import QSoundEffect
from PyQt6.QtCore import QUrl
import os
from .grades import get_next_grade
from .terminal_ui import TerminalDialog
_sound = None

def play_sound(filename):
    global _sound

    path = os.path.join(os.path.dirname(__file__), "assets", "sounds", filename)

    if not os.path.exists(path):
        return

    _sound = QSoundEffect()
    _sound.setSource(QUrl.fromLocalFile(path))
    _sound.setVolume(0.8)
    _sound.play()
def show_terminal(title, content):
    dialog = TerminalDialog(title, content)

    dialog.exec()
def show_session(player, mission):
    content = f"""


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
    show_terminal("""
====================================
🪖 ANKARMY AIR COMMAND - TERMINAL SYSTEM
====================================
""", content)



def show_end_session(player):
    session_xp = player.cards_correct
    bar = render_progress_bar(
        player.xp,
        get_next_grade(player.grade).xp_required
    ) 
    
    
    session_wrong = player.cards_wrong
    total = session_xp + session_wrong
    accuracy = (session_xp / total) * 100 if total > 0 else 0
    état= "complète" if player.mission_completed else "incomplète"
    content = f"""

📊 RÉSULTATS
XP TOTAL: {player.xp}
DISCIPLINE: {player.discipline}

📈 SESSION
✔ Correctes: {player.cards_correct}
✘ Erreurs: {player.cards_wrong}
Accuracy : {accuracy} 
Etat de la mission : {état}
PROGRESSION: {bar}
 




------------------------------------
🪖 STATUT
Grade: {player.grade.name}
Nombre total de mission : {player.total_mission}
Mission réussie : {player.mission_réussie}
Pourcentage de réussite : {player.pourcentage_de_réussite}% 
====================================
"""
    show_terminal("""
====================================
🪖 ANKARMY AIR COMMAND - 📦 RAPPORT DE MISSION
====================================
""", content)



def show_boot(player):
     username = mw.pm.name
     
     bar = render_progress_bar(
        player.xp,
        get_next_grade(player.grade).xp_required
    ) 
     discipline="STABLE" if player.discipline >= 75 else "WARNING"
     content = f"""

Connexion au Commandement...
Vérification du dossier...
Accès autorisé.
Bienvenue, {player.grade.name}.
STATUS : CONNECTED
USER   : {username}
RANK   : {player.grade.name}
DISCIPLINE  : {discipline}
------------------------------------
📊 STATUS
XP: {player.xp}
PROGRESSION DANS LE GRADE: {bar}
DISCIPLINE: {player.discipline}
Nombre total de mission : {player.total_mission}
Mission réussie : {player.mission_réussie}
Pourcentage de réussite : {player.pourcentage_de_réussite}% 
Tous les systèmes sont opérationnels.
En attente des ordres...
====================================
"""
     show_terminal("""
====================================
🪖 ANKARMY AIR COMMAND - TERMINAL SYSTEM
====================================
""", content)
def show_promo(player, old_grade):
    play_sound("promotion.wav")

    content = f"""


       ★★★★★★★★★★★★★★★★

      PROMOTION OFFICIELLE

Félicitations Soldat !

Ancien grade :
    {old_grade}

Nouveau grade :
    {player.grade.name.name}

Votre efficacité a été reconnue
par le Haut Commandement.

Continuez votre progression.

       ★★★★★★★★★★★★★★★★

====================================
"""

    show_terminal("""
====================================
🪖 ANKARMY AIR COMMAND - PROMOTION
====================================
""", content)
     
def render_progress_bar(current: int, total: int, length: int = 20) -> str:
    if total == 0:
        return "[--------------------] 0%"

    percent = int((current / total) * 100)
    filled_length = int(length * current // total)

    bar = "█" * filled_length + "-" * (length - filled_length)

    return f"[{bar}] {percent}%"


    
    