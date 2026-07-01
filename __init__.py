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
    global session_started

    if session_started:
        return

    session_started = True
    engine.start_session()


def on_end_session(*args, **kwargs):
    print("REVIEWER END")
    global session_started

    if not session_started:
        return
    engine.end_session()
    engine.current_mission = None


gui_hooks.reviewer_did_init.append(on_start_session)
gui_hooks.reviewer_did_answer_card.append(on_answer)
gui_hooks.reviewer_will_end.append(on_end_session)
