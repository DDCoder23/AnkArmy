class Player:
    def __init__(
        self,
        xp=0,
        discipline=100,
        cards_correct=0,
        cards_wrong=0,
        grade="Recrue"
    ):
        self.xp = xp
        self.discipline = discipline
        self.cards_correct = cards_correct
        self.cards_wrong = cards_wrong
        self.grade = grade

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
        "grade": self.grade
    }
    @classmethod
    def from_dict(cls, data):
        return cls(
        xp=data.get("xp", 0),
        discipline=data.get("discipline", 100),
        cards_correct=data.get("cards_correct", 0),
        cards_wrong=data.get("cards_wrong", 0),
        grade=data.get("grade", "Soldat")
    )
    def gain_discipline(self, amount):
        self.discipline = min(100, self.discipline + amount)