from .state import load_state, save_state
from .mission import generate_mission
from .terminal import show


class Engine:
    def __init__(self):
        self.state = load_state()
        self.mission = None

    # START SESSION
    def start_session(self):
        self.state["cards_correct"] = 0
        self.state["cards_wrong"] = 0

        self.mission = generate_mission(self.state)
        show(f"MISSION:\n{self.mission['objective']}")

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

        show(
            f"SESSION TERMINÉE\n"
            f"XP gagné: {xp_gain}\n"
            f"Discipline: {self.state['discipline']}"
        )

        save_state(self.state)