from PyQt6.QtWidgets import QLabel

from pathlib import Path

def abs_path(nombre):
    return str(Path(__file__).parent.absolute() / nombre)

class Caja(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f"background-color:{color}")
