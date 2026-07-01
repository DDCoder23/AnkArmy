from .state import load_player, save_player
from .mission import generate_mission
from .terminal import show_session,show_end_session
from aqt import mw



    

class Engine:
    def __init__(self):
        self.player = load_player()
        self.session_active = False
        self.active_deck = None
        self.locked_deck_id = None
        self._starting = False


    
    # START SESSION
    def start_session(self):
        print("REVIEWER STARTED")
        print(self.session_active)
        print(self._starting)
        if self.session_active or self._starting:
            return
        self._starting = True
        if mw.col is None :
            print("⚠️ Collection not ready yet")
            self._starting=False
            return


            
        self.session_active = True

        self.player.reset_session()

            # 🪖 lock deck actuel
        self.locked_deck_id = mw.col.decks.current()["id"]

            # 🎯 génération mission
        self.current_mission = generate_mission(self.player)
        print(self.current_mission)
        self.player.total_mission += 1
        self.player.mission_completed = False

            # 🖥️ affichage
        show_session(self.player, self.current_mission)

        print("🟢 SESSION STARTED")
        print(f"📦 Deck locked: {self.locked_deck_id}")
        


        
        

        

        show_session(self.player,self.player.current_mission)

    
    def check_deck_integrity(self):
        current_deck = mw.col.decks.current()["id"]

        if self.locked_deck_id is None:
            self.locked_deck_id = current_deck
            return True

        if current_deck != self.locked_deck_id:
            return False

        return True
    # CARD RESULT
    def review_card(self, correct: bool):
        if not self.check_deck_integrity():
            self.end_session()
            return
        self.player.process_result(correct)
        self.check_mission_progress()
        save_player(self.player)   # 🔥 IMPORTANT

    # END SESSION
    def end_session(self):
        print("REVIEWER END")
        print(self.session_active)
        if not self.session_active:
            return
        self.session_active = False
        print(self.session_active)
        
        mission = self.player.current_mission
        xp_gain = self.player.cards_correct
        self.player.add_xp(xp_gain)
        if self.player.mission_completed and  self.player.cards_wrong == 0 :
            self.player.gain_discipline(4)
            self.player.add_xp(10)
        elif self.player.mission_completed:
            self.player.gain_discipline(2)
        
        else:
            self.player.lose_discipline(1)
        self.player.pourcentage_de_réussite=self.player.mission_réussie//self.player.total_mission
        show_end_session(self.player)
        


        save_player(self.player)
    def check_mission_progress(self):
        mission = self.player.current_mission

        if self.player.cards_correct >= mission["target"]:
            self.player.mission_completed = True
            self.player.mission_réussie+=1
        
