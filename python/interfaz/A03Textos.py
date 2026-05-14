from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit
import sys

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        print("Dentro de ventana")
        self.mi_texto = QLineEdit()
        self.mi_texto.textChanged.connect(self.texto_cambiado)
        self.mi_texto.returnPressed.connect(self.texto_presionado)
        self.setCentralWidget(self.mi_texto)

        self.resize(400,60)

    def texto_cambiado(self, texto):
        print(texto)
        
    def texto_presionado(self):
        self.setWindowTitle (self.mi_texto.text())

def main():
    print("Iniciando el programa")
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
