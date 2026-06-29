from aqt import gui_hooks
from .engine import Engine

engine = Engine()


def on_session_start():
    engine.start_session()


def on_card_answer(reviewer, card, ease):
    correct = ease > 1
    engine.review_card(correct)


def on_session_end():
    engine.end_session()


gui_hooks.session_will_start.append(on_session_start)
gui_hooks.reviewer_did_answer_card.append(on_card_answer)
gui_hooks.session_will_end.append(on_session_end)