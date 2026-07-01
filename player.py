from .grades import Grades
class Player:
    def __init__(
        self,
        xp=0,
        discipline=100,
        cards_correct=0,
        cards_wrong=0,
        grade=Grades[0]
    ):
        self.xp = xp
        self.discipline = discipline
        self.cards_correct = cards_correct
        self.cards_wrong = cards_wrong
        self.grade = grade
        self.current_mission = None
        self.mission_completed = False
        self.total_mission=0
        self.mission_réussie=0
        self.pourcentage_de_réussite=0

    def add_xp(self, amount):
        self.xp += amount

    def lose_discipline(self, amount):
        self.discipline = max(0, self.discipline - amount)

    def add_correct_card(self):
        self.cards_correct += 1

    def add_wrong_card(self):
        self.cards_wrong += 1

    def reset_session(self):
        self.cards_correct = 0
        self.cards_wrong = 0
    def to_dict(self):
        return {
        "xp": self.xp,
        "discipline": self.discipline,
        "cards_correct": self.cards_correct,
        "cards_wrong": self.cards_wrong,
        "grade": self.grade,
        "total des missions" : self.total_mission,
         "missions reussies": self.mission_réussie,
        "pourcentage de reussite" : self.pourcentage_de_réussite
    }
    @classmethod
    def from_dict(cls, data):
        return cls(
        xp=data.get("xp", 0),
        discipline=data.get("discipline", 100),
        cards_correct=data.get("cards_correct", 0),
        cards_wrong=data.get("cards_wrong", 0),
        grade=data.get("grade", "Soldat"),
        total_mission=data.get("total des missions", 0),
        mission_réussie=data.get("missions reussies", 0),
        pourcentage_de_réussite=data.get("pourcentage de reussite",0)
    )
    def gain_discipline(self, amount):
        self.discipline = min(100, self.discipline + amount)
    def process_result(self, correct: bool):
        if correct:
            self.add_xp(1)
            self.add_correct_card()
        else:
            self.lose_discipline(1)
            self.add_wrong_card()
    def get_status(self):
        return {
        "xp": self.xp,
        "discipline": self.discipline,
        "grade": self.grade,
        "correct": self.cards_correct,
        "wrong": self.cards_wrong
    }