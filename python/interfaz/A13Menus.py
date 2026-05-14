from PyQt6.QtWidgets import QApplication, QMainWindow, QStatusBar, QMessageBox
from PyQt6.QtGui import QIcon, QAction
import sys
from Utils import abs_path

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        print("Dentro de ventana")
        self.setStatusBar(QStatusBar())
        self.construir_menu()
        self.resize(350, 200)

    def construir_menu(self):
        menu = self.menuBar()
        menu_Archivo = menu.addMenu("&Archivo")
        menu_Archivo.addAction("&Prueba")
        submenu_archivo = menu_Archivo.addMenu("&Submenu")
        submenu_archivo.addAction("Subopcion &1")
        submenu_archivo.addAction("Subopcion &2")
        menu_Archivo.addSeparator()
        icono = QIcon(abs_path("tierra-png-3.jpg"))

        action_salir = QAction(self)
        action_salir.setIcon(icono)
        action_salir.setText("&Salir")
        action_salir.setShortcut('Ctrl+Q')
        action_salir.triggered.connect(self.close)
        action_salir.setStatusTip("Cierra el programa")
        menu_Archivo.addAction(action_salir)

        menu_editar = menu.addMenu("&Editar")

        menu_ayuda = menu.addMenu("A&yuda")
        action_acercade = QAction (self, text = "Acerca de...")
        action_acercade.triggered.connect(self.mostrar_informacion)
        menu_ayuda.addAction(action_acercade)
    
    def mostrar_informacion(self):
        QMessageBox.information(self, "informacion", "esto es untexto informativo")
        #menu_Archivo.addAction()


def main():
    print("Iniciando el programa")
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
