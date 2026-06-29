from aqt import gui_hooks
from .engine import Engine

engine = Engine()


    


def on_answer(*args, **kwargs):
    reviewer, card, ease = args

    print("CARD:", card)
    print("EASE:", ease)

    correct = ease >= 3
    engine.review_card(correct)
    
    


def on_reviewer_init(reviewer):
    print("REVIEWER STARTED")
    engine.start_session()


def on_reviewer_end():
    print("REVIEWER END")
    engine.end_session()


gui_hooks.reviewer_did_init.append(on_reviewer_init)
gui_hooks.reviewer_did_answer_card.append(on_answer)
gui_hooks.reviewer_will_end.append(on_reviewer_end)
