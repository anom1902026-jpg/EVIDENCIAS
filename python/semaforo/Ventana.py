from PyQt6.QtWidgets import QApplication, QMainWindow, \
    QGridLayout, QLabel, QWidget, QPushButton
from PyQt6.QtCore import QRunnable, QObject, pyqtSignal as Signal, QThreadPool
import sys

class WorkerSignals(QObject):
    luz_roja = Signal(bool)
    luz_amarilla = Signal(bool)
    luz_verde = Signal(bool)


    def __init__(self):
        super().__init__()
class Worker(QRunnable):
    def __init__(self):
        super().__init__()
        self.signals = WorkerSignals()
    
    def prender_luz_roja(self, estado:bool):
        try:
            self.signals.luz_roja.emit(estado)
        except Exception as e:
            print(e)

    def prender_luz_amarilla(self, estado:bool):
        try:
            self.signals.luz_amarilla.emit(estado)
        except Exception as e:
            print(e)

    def prender_luz_verde(self, estado:bool):
        try:
            self.signals.luz_verde.emit(estado)
        except Exception as e:
            print(e)


    def run(self):
        pass

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        print("Dentro de ventana")
        contenedor = QWidget()
        mi_layout = QGridLayout()
        contenedor.setLayout(mi_layout)
        boton_arranque = QPushButton("Activar")
        boton_paro = QPushButton("Detener")
        self.indicador = QLabel()
        self.indicador_2 = QLabel()
        self.indicador_3 = QLabel()
        mi_layout.addWidget(boton_arranque, 0, 0)
        mi_layout.addWidget(boton_paro, 1, 0)
        mi_layout.addWidget(self.indicador, 0, 1, 2, 1)
        mi_layout.addWidget(self.indicador_2, 1, 1, 2, 1)
        mi_layout.addWidget(self.indicador_3, 2, 1, 2, 1)

        # self.actualizar_control(boton_arranque, "Green")
        # self.actualizar_control(boton_paro, "Red")
        self.actualizar_control(self.indicador, "Gray")

        self.setCentralWidget(contenedor)

        self.proceso = None
        # 
        # ++ Worker
        self.worker = Worker()
        self.pool = QThreadPool()
        self.pool.start(self.worker)
        boton_arranque.setCheckable(True)
        boton_arranque.clicked.connect(self.cambiar_estado)

        boton_paro.setCheckable(True)
        boton_paro.clicked.connect(self.cambiar_estado1)

        self.worker.signals.luz_roja.connect(self.prender_indicador_rojo)
        self.worker.signals.luz_amarilla.connect(self.prender_indicador_amarillo)
        self.worker.signals.luz_verde.connect(self.prender_indicador_verde)

    def obtener_worker(self): 
        return self.worker

    def cambiar_estado(self, valor):
        self.cambiar_bandera_proceso(0,valor)

    def cambiar_estado1(self, valor):
        self.cambiar_bandera_proceso(1,valor)

    def establecer_proceso(self, proceso):
        self.proceso = proceso
    
    def cambiar_bandera_proceso(self, indice:int, valor:bool):
        if self.proceso:
            self.proceso.cambiar_valor_x(indice, valor)

    def prender_indicador_rojo(self, valor):
        if valor:
            self.actualizar_control(self.indicador, "Red")
        else:
            self.actualizar_control(self.indicador, "Gray")

    def prender_indicador_amarillo(self, valor):
        if valor:
            self.actualizar_control(self.indicador_2, "Yellow")
        else:
            self.actualizar_control(self.indicador_2, "Gray")

    def prender_indicador_verde(self, valor):
        if valor:
            self.actualizar_control(self.indicador_3, "Green")
        else:
            self.actualizar_control(self.indicador_3, "Gray")

    def actualizar_control(self, etiqueta: QLabel, color:str):
        etiqueta.setStyleSheet(f"""background-color: {color}; 
                               border-radius: 15""")
        etiqueta.setFixedSize(30, 30)



def main():
    print("Iniciando el programa")
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())

if __name__ == "__main__" :
    main()