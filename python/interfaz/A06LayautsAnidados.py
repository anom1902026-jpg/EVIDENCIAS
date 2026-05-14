from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton
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
        layaut_vertical_01 = QVBoxLayout ()
        #layaut_vertical_01.setContentsMargins(10,5,20,0)
        #layaut_vertical_01.setSpacing(0)
        layaut_horizontal_01 = QHBoxLayout ()
        layaut_horizontal_02 = QHBoxLayout ()
        layaut_vertical_02 = QVBoxLayout()
        layaut_vertical_03 = QVBoxLayout()

        caja = Caja("Blue")
        caja1 = Caja ("Green")
        caja2 = Caja("#C40769")
        caja3 = Caja("Orange")
        caja4 = Caja("Pink")
        caja5 = Caja("Red")
        caja6 = Caja("Yellow")
        titulo = QLabel("¿quieres andar conmigo?")
        txt_si = QLabel("Si")
        txt_no = QLabel("No")
        btn_si = QPushButton("si quiere")
        btn_no = QPushButton("no quiere")
        btn_aceptar = QPushButton("aceptar")
        btn_cancelar = QPushButton("cancelar")

        contenedor.setLayout(layaut_vertical_01)

        layaut_vertical_02.addWidget(txt_si)
        layaut_vertical_02.addWidget(txt_no)

        layaut_vertical_03.addWidget(btn_si)
        layaut_vertical_03.addWidget(btn_no)

        layaut_horizontal_01.addLayout(layaut_vertical_02)
        layaut_horizontal_01.addLayout(layaut_vertical_03)

        layaut_vertical_01.addWidget(titulo)
        layaut_horizontal_02.addWidget(btn_aceptar)
        layaut_horizontal_02.addWidget(btn_cancelar)
        layaut_vertical_01.addLayout(layaut_horizontal_01)
        layaut_vertical_01.addLayout(layaut_horizontal_02)
      
        self. setCentralWidget(contenedor)

def main():
    print("Iniciando el programa")
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
