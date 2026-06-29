from .state import load_state, save_state
from .mission import generate_mission
from .terminal import show_header, show_mission, show_status, show_footer


def end_session(self):
    
    save_state(self.state)

    

class Engine:
    def __init__(self):
        self.state = load_state()
        self.mission = None

    # START SESSION
    def start_session(self):
        self.state["cards_correct"] = 0
        self.state["cards_wrong"] = 0

        self.mission = generate_mission(self.state)
        show_header()
        show_mission(self.mission)
        show_status(self.state)
        show_footer()

    # CARD RESULT
    def review_card(self, correct: bool):
        if correct:
            self.state["xp"] += 1
            self.state["cards_correct"] += 1
        else:
            self.state["discipline"] -= 1
            self.state["cards_wrong"] += 1

        save_state(self.state)   # 🔥 IMPORTANT

    # END SESSION
    def end_session(self):
        xp_gain=self.state["cards_correct"]
        self.state["xp"]+=xp_gain
        

        

        # discipline simple
        if self.state["cards_wrong"] == 0:
            self.state["discipline"] += 2

        show_header()
        print("📦 SESSION TERMINÉE")
        show_status(self.state)
        show_footer()


        save_state(self.state)