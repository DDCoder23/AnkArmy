class Grade:
    def __init__(self, name: str, xp_required: int):
        self.name = name
        self.xp_required = xp_required

    def is_reached(self, xp: int) -> bool:
        return xp >= self.xp_required

    def __repr__(self):
        return f"Grade(name='{self.name}', xp_required={self.xp_required})"
Grades = [
    Grade("Recrue", 0),
    Grade("Aviateur confirmé", 50),
    Grade("Aviateur de 1ère classe", 150),
    Grade("Caporal", 300),
    Grade("Caporal-chef", 600),
    Grade("Sergent", 1000),
    Grade("Sergent-chef", 1500),
    Grade("Adjudant", 2200),
    Grade("Adjudant-chef", 3000),
    Grade("Major", 3900),
    Grade("Aspirant",4900 ),
    Grade("Sous-lieutenant", 6000),
    Grade("Lieutenant", 7200),
    Grade("Capitaine", 8500),
    Grade("Commandant", 9900),
    Grade("Lieutenant-colonel", 11400),
    Grade("Colonel", 13000),
    Grade("Général de brigade aérienne", 14700),
    Grade("Général de division aérienne", 16500),
    Grade("Général de corps aérien", 18400),
    Grade("Général d'armée aérienne", 20400),
    
]
def get_next_grade(current_grade):
    for i, grade in enumerate(GRADES):
        if grade.name == current_grade:
            if i + 1 < len(GRADES):
                return GRADES[i + 1]
            return None

    return GRADES[0]
def check_promotion(player) -> bool:
    next_grade = get_next_grade(player.grade)

    if next_grade is None:
        return False

    if player.xp >= next_grade.xp_required:
        player.grade = next_grade
        player.xp = 0   
        return True

    return False