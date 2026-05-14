from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QStackedLayout
from PyQt6.QtCore import Qt
import sys
from Utils import Caja

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.layout:QStackedLayout = QStackedLayout()
        contenedor = QWidget()
        contenedor.setLayout(self.layout)
        self.setCentralWidget(contenedor)

        caja1 = Caja ("re")
        caja2 = Caja ("Blue")
        caja3 = Caja ("blue")
        caja4 = Caja ("Cyan")

        self.layout.addWidget(caja1)
        self.layout.addWidget(caja2)
        self.layout.addWidget(caja3)
        self.layout.addWidget(caja4)

        self.layout.setCurrentIndex(2)

        print("Dentro de ventana")
    
    def keyPressEvent(self, event):
        indice = self.layout.currentIndex()
        indice_maximo = self.layout.count() -1
        if event.key() == Qt.Key.Key_Left:
            print("se oprimio la tecla izquierda")
            indice +=1
        if event.key() == Qt.Key.Key_Right:
            print("se oprimio la tecla derecha")
            indice -=1
        if indice > indice_maximo:
            indice = 0
        if indice < 0:
            indice = indice_maximo
        self.layout.setCurrentIndex(indice)
        event.accept()

def main():
    print("Iniciando el programa")
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
