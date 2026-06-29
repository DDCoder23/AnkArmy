def show_header():
    print("\n" + "=" * 40)
    print("🪖 ANKARMY COMMAND CENTER")
    print("=" * 40)


def show_mission(mission):
    print("\n📡 MISSION ACTIVE")
    print(mission["objective"])


def show_status(state):
    print("\n📊 STATUS")
    print(f"XP: {state['xp']}")
    print(f"DISCIPLINE: {state['discipline']}")
    print(f"CORRECT: {state['cards_correct']} | WRONG: {state['cards_wrong']}")


def show_footer():
    print("\n" + "=" * 40 + "\n")