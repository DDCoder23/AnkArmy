from .state import load_player, save_player
from .mission import generate_mission
from .terminal import show_session,show_end_session




    

class Engine:
    def __init__(self):
        self.player = load_player()
        self.mission = None

    # START SESSION
    def start_session(self):
        self.player.reset_session()

        self.mission = generate_mission(self.player)

        show_session(self.player,self.mission)


    # CARD RESULT
    def review_card(self, correct: bool):
        self.player.process_result(correct)

        save_player(self.player)   # 🔥 IMPORTANT

    # END SESSION
    def end_session(self):
        xp_gain = self.player.cards_correct
        self.player.add_xp(xp_gain)
        

        

        # discipline simple
        if self.player.cards_wrong == 0:
            self.player.gain_discipline(2)
        show_end_session(self.player)
        


        save_player(self.player)