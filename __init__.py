from aqt import gui_hooks
from .engine import Engine

engine = Engine()


    


def on_answer(*args, **kwargs):
    reviewer, card, ease = args

    print("CARD:", card)
    print("EASE:", ease)

    correct = ease >= 3
    engine.review_card(correct)
    
    


def on_start_session(*args, **kwargs):
    
  
    engine.start_session()


def on_end_session(*args, **kwargs):
    print("REVIEWER END")
    
    engine.end_session()
    


def on_profile_open(*args, **kwargs):
    print("🟢 PROFILE READY → AnkArmy enabled")
    engine.accueil()

def on_state_change(new_state, old_state):
    print(f"STATE: {old_state} -> {new_state}")

    if new_state == "review":
        print(">>> START SESSION")
        engine.start_session()

    elif old_state == "review":
        print(">>> END SESSION")
        engine.end_session()





gui_hooks.reviewer_did_init.append(on_start_session)
gui_hooks.reviewer_did_answer_card.append(on_answer)
gui_hooks.reviewer_will_end.append(on_end_session)
gui_hooks.profile_did_open.append(on_profile_open)
