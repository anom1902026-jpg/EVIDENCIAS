from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QInputDialog, QColorDialog, QFontDialog, \
    QPushButton
import sys

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        print("Dentro de ventana")
        self.boton = QPushButton("Presioname")
        self.setCentralWidget(self.boton)
        self.boton.clicked.connect(self.mostrar_dialog)
    
    def mostrar_dialog(self):
        print("se presiono el boton")
        #archivo, _ =QFileDialog.getOpenFileName(self, "Abrir Archivo", ".")
        #archivo, _ =QFileDialog.getSaveFileName(self, "guardar Archivo", ".")
        #print(archivo)

        #valor, confirmado = QInputDialog.getText(self, "se leera texto", "texto")
        #valor, confirmado = QInputDialog.getInt(self, "se leera un entero", "numero")
        #valor, confirmado = QInputDialog.getDouble(self, "se leera un numero decimal", \
        #                                            "numero", max=50, min=10)
        #valor, confirmado = QInputDialog.getItem(self, "se leera un numero elemento", \
        #                                            "colores", ['rojo', 'verde', 'azul',], editable=False)
        #print (valor, confirmado)

        #fuente, confirmado = QFontDialog.getFont(self)
        #if confirmado:
        #    self.boton.setFont(fuente)

        color = QColorDialog.getColor()
        if color.isValid():
            self.boton.setStyleSheet(f"background-color: {color.name()}")

def main():
    print("Iniciando el programa")
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
