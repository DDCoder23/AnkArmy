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
    print("REVIEWER STARTED")
  
    engine.start_session()


def on_end_session(*args, **kwargs):
    print("REVIEWER END")
    
    engine.end_session()
    engine.current_mission = None


gui_hooks.reviewer_did_init.append(engine.start_session)
gui_hooks.reviewer_did_answer_card.append(on_answer)
gui_hooks.reviewer_will_end.append(engine.end_session)
