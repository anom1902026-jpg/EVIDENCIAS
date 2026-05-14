from PyQt6.QtWidgets import QApplication, QMainWindow, QComboBox
import sys

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        print("Dentro de ventana")
        combo = QComboBox()
        combo.addItems(['opcion 1', 'opcion 2', 'opcion 3', 'opcion 4'])
        combo.currentIndexChanged.connect(self.indice_selecionado)
        combo.currentTextChanged.connect(self.texto_seleccionado)
        self.setCentralWidget(combo)
        self.resize(400, 50)

    def indice_selecionado(self, indice):
        print(f"se selecciono el indice {indice}")
    def texto_seleccionado(self, texto):
        print(f"se selecciono el texto {texto}")

def main():
    print("Iniciando el programa")
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
