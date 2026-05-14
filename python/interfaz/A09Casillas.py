from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QCheckBox, \
    QRadioButton, QGroupBox, QPushButton, QHBoxLayout

from PyQt6.QtCore import Qt
import sys
from Utils import Caja

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        print("Dentro de ventana")
        layout_horizontal_1 = QHBoxLayout ()
        layout_vertical_1 = QVBoxLayout ()
        contenedor = QWidget ()
        contenedor.setLayout (layout_horizontal_1)

        caja1 = Caja ("red")
        caja2 = Caja ("Green")

        group_hobbys = QGroupBox("Hobbys")
        group_hobbys.setLayout(layout_vertical_1)

        hobby_guitarra = QCheckBox("tocar guitarra")
        hobby_musica = QCheckBox ("Escuchar musica")
        hobby_peliuculas = QCheckBox("ver peliculas")
        hobby_leer = QCheckBox ("leer")
        hobby_coleccionar = QCheckBox ("coleccionar")

        layout_vertical_1.addWidget(hobby_guitarra)
        layout_vertical_1.addWidget(hobby_musica)
        layout_vertical_1.addWidget(hobby_peliuculas)
        layout_vertical_1.addWidget(hobby_leer)
        layout_vertical_1.addWidget(hobby_coleccionar)

        group_materia = QGroupBox("Materia")
        layout_vertical_2 = QVBoxLayout()
        group_materia.setLayout(layout_vertical_2)

        materia_programacion = QRadioButton("programacion")
        materia_taller = QRadioButton("taller de seguridad")
        materia_seguridad = QRadioButton("seguridad")
        materia_microcontroladores = QRadioButton ("micro")
        materia_hidraulica = QRadioButton ("hidraulica")

        layout_vertical_2.addWidget(materia_programacion)
        layout_vertical_2.addWidget(materia_taller)
        layout_vertical_2.addWidget(materia_seguridad)
        layout_vertical_2.addWidget(materia_microcontroladores)
        layout_vertical_2.addWidget(materia_hidraulica)

        layout_horizontal_1.addWidget(group_hobbys)
        layout_horizontal_1.addWidget(group_materia)
        self.setCentralWidget(contenedor)

        hobby_guitarra
        hobby_musica
        hobby_peliuculas
        hobby_leer
        hobby_coleccionar

        #estableciendo eventos

        hobby_guitarra.stateChanged.connect(self.casilla_modificada)
        hobby_musica.stateChanged.connect(self.casilla_modificada)
        hobby_peliuculas.stateChanged.connect(self.casilla_modificada)
        hobby_leer.stateChanged.connect(self.casilla_modificada)
        hobby_coleccionar.stateChanged.connect(self.casilla_modificada)

        materia_programacion.toggled.connect(self.radio_seleccionado)
        materia_taller.toggled.connect(self.radio_seleccionado)
        materia_seguridad.toggled.connect(self.radio_seleccionado)
        materia_microcontroladores.toggled.connect(self.radio_seleccionado)
        materia_hidraulica.toggled.connect(self.radio_seleccionado)

      

        self.resize(300, 200)
    
    def radio_seleccionado(self, seleccionado):
        radio= self.sender()
        print(f"{radio.text()}, {seleccionado}")

    def casilla_modificada (self, estado):
        casilla = self.sender()
        print (casilla.text(), estado)
        valor = Qt.CheckState(estado)
        print(casilla.text(), valor.name)

def main():
    print("Iniciando el programa")
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
