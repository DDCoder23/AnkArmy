from aqt.qt import (
    QDialog,
    QVBoxLayout,
    QLabel,Qt
)
from PyQt6.QtCore import QTimer
from aqt import mw


class TerminalDialog(QDialog):
    def __init__(self, title, text):
        super().__init__(mw)

        self.setWindowTitle(title)
        self.resize(750, 500)

        self.full_text = text
        self.current_text = ""
        self.index = 0
        self.cursor_visible = True
        layout = QVBoxLayout()
        title = QLabel("🪖 ANKARMY AIR COMMAND")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label = QLabel("")
        self.label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        self.label.setWordWrap(True)

        self.label.setStyleSheet("""
            QLabel{
                background:#101010;
                color:#00ff66;
                font-family:Consolas;
                font-size:14px;
                padding:15px;
            }
        """)

        layout.addWidget(self.label)
        self.setLayout(layout)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.write_next_character)
        self.timer.start(15)

    def write_next_character(self):
        if self.index >= len(self.full_text):
            self.timer.stop()
            return

        self.current_text += self.full_text[self.index]
        self.label.setText(self.current_text)

        self.index += 1
        if self.index >= len(self.full_text):
            self.timer.stop()

            self.cursor_timer = QTimer(self)
            self.cursor_timer.timeout.connect(self.blink_cursor)
            self.cursor_timer.start(500)

            return
    def blink_cursor(self):
        if self.cursor_visible:
            self.label.setText(self.current_text + "█")
        else:
            self.label.setText(self.current_text)

        self.cursor_visible = not self.cursor_visible