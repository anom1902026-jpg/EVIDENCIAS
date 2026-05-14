from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        print("Dentro de ventana")
        mi_boton = QPushButton("presioname")
        mi_boton.clicked.connect(self.boton_clikeado)
        mi_boton.pressed.connect(self.boton_presionado)
        mi_boton.released.connect(self.boton_liberado)

        self.setCentralWidget(mi_boton)

    def boton_clikeado(self):
        print("se clikeo el boton")
    
    def boton_presionado(self):
        print("se presiono el boton")
    
    def boton_liberado(self):
        print("se ha libero el boton")

def main():
    print("Iniciando el programa")
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
