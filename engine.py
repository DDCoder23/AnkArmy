from .state import load_player, save_player
from .mission import generate_mission
from .terminal import show_session,show_end_session,show_boot, show_promo
from .rewards import end_session_rewards
from .grades import check_promotion


    

class Engine:
    def __init__(self):
        self.player = load_player()
        print('player loaded')
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
        global current_streak
        current_streak=0

            # 🖥️ affichage
        show_session(self.player, self.current_mission)

        print("🟢 SESSION STARTED")
       
  

    
    
    # CARD RESULT
    def review_card(self, correct: bool):
        
        self.player.process_result(correct)
        if correct:
            current_streak+=1
        else:
            current_streak=0
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
        self.check_end_session_mission()
        end_session_rewards(self.player)
        old=self.player.grade
        if check_promotion(self.player): 
            show_promo(self.player,old)
        
        
        show_end_session(self.player)
        save_player(self.player)
        

    def complete_mission(self):
        self.player.mission_completed = True
        

        print("🎯 Mission accomplie !")
        
    def check_mission_progress(self):
        mission = self.current_mission

   
        if self.player.mission_completed:
            return

        mission_type = mission["type"]

        if mission_type == "cards":
            if self.player.cards_correct >= mission["target"]:
                self.complete_mission()


        elif mission_type == "streak":
            if current_streak >= mission["target"]:
                self.complete_mission()
    def check_end_session_mission(self):
        if self.player.mission_completed:
            return

        mission = self.current_mission

        if mission["type"] == "no_mistake":
            if self.player.cards_wrong == 0:
                self.complete_mission()

        elif mission["type"] == "accuracy":
            total = self.player.cards_correct + self.player.cards_wrong

            if total == 0:
                return

            accuracy = self.player.cards_correct / total * 100

            if accuracy >= mission["target"]:
                self.complete_mission()
    def accueil (self):
        self.player = load_player()
        print('player loaded')

        show_boot(self.player)
        
