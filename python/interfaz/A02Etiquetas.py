from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap

import sys
from pathlib import Path

def abs_path(nombre):
    return str(Path(__file__).parent.absolute() / nombre)

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        print("Dentro de ventana")
    
        ruta = abs_path("tierra-png-3.jpg")
        imagen = QPixmap(ruta)

        fuente = QFont("AdLib BT", 20, QFont.Weight.Bold, italic=True)

        mi_etiqueta = QLabel("bienvenido")
        mi_etiqueta.setAlignment(Qt.AlignmentFlag.AlignHCenter |
                                 Qt.AlignmentFlag.AlignBottom)
        mi_etiqueta.setFont(fuente)
        mi_etiqueta.setPixmap(imagen)
        self.setCentralWidget(mi_etiqueta)
        self.resize(400, 300)

def main():
    print("Iniciando el programa")
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
