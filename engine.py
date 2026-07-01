from .state import load_player, save_player
from .mission import generate_mission
from .terminal import show_session,show_end_session,show_boot




    

class Engine:
    def __init__(self):
        self.player = load_player()
        self.session_active = False
        
        self.current_mission={}


    
    # START SESSION
    def start_session(self):
        
        if self.session_active :
            return
        


            
        self.session_active = True

        self.player.reset_session()

            # 🪖 lock deck actuel
        

            # 🎯 génération mission
        self.current_mission = generate_mission(self.player)
        print(self.current_mission)
        self.player.total_mission += 1
        self.player.mission_completed = False

            # 🖥️ affichage
        show_session(self.player, self.current_mission)

        print("🟢 SESSION STARTED")
       
  

    
    
    # CARD RESULT
    def review_card(self, correct: bool):
        
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
        
        mission = self.current_mission
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
        save_player(self.player)
        show_end_session(self.player)
        


        
    def check_mission_progress(self):
        mission = self.current_mission

        if self.player.cards_correct >= mission["target"]:
            self.player.mission_completed = True
            self.player.mission_réussie+=1
    def accueil (self):
        show_boot(self.player)
        
