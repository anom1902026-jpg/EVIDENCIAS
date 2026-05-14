from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QLabel
import sys

class Caja(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f"background-color:{color}")

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        print("Dentro de ventana")
        contenedor = QWidget()
        mi_layaut = QHBoxLayout ()
        mi_layaut.setContentsMargins(10,5,20,0)
        mi_layaut.setSpacing(0)
        
        contenedor.setLayout(mi_layaut)

        caja = Caja("Blue")
        caja1 = Caja ("Green")
        caja3 = Caja("#C40769")

        mi_layaut.addWidget(caja)
        mi_layaut.addWidget(caja1)
        mi_layaut.addWidget(caja3)

        
        self. setCentralWidget(contenedor)

def main():
    print("Iniciando el programa")
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
