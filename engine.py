from .state import load_player, save_player
from .mission import generate_mission
from .terminal import show_header, show_mission, show_status, show_footer




    

class Engine:
    def __init__(self):
        self.player = load_player()
        self.mission = None

    # START SESSION
    def start_session(self):
        self.player.reset_session()

        self.mission = generate_mission(self.player)
        show_header()
        show_mission(self.mission)
        show_status(self.player)
        show_footer()

    # CARD RESULT
    def review_card(self, correct: bool):
        if correct:
            self.player.add_xp(1)
            self.player.add_correct_card()
        else:
            self.player.lose_discipline(1)
            self.player.add_wrong_card()

        save_player(self.player)   # 🔥 IMPORTANT

    # END SESSION
    def end_session(self):
        xp_gain = self.player.cards_correct
        self.player.add_xp(xp_gain)
        

        

        # discipline simple
        if self.player.cards_wrong == 0:
            self.player.gain_discipline(2)

        show_header()
        print("📦 SESSION TERMINÉE")
        show_status(self.player)
        show_footer()


        save_player(self.player)