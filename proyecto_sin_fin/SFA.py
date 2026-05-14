import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QVBoxLayout, QComboBox, QSpinBox
)
from PyQt6.QtCore import QTimer

TEMP_MAX = 60

frutas = {
    "Manzana": {"temp": 55, "tiempo": 6, "espesor": "5 mm"},
    "Plátano": {"temp": 55, "tiempo": 6, "espesor": "5-7 mm"},
    "Mango": {"temp": 60, "tiempo": 8, "espesor": "5 mm"},
    "Fresa": {"temp": 50, "tiempo": 4, "espesor": "3-5 mm"},
    "Piña": {"temp": 60, "tiempo": 10, "espesor": "5-8 mm"},
}

# ------------------ VENTANA DECISIÓN ------------------
class DecisionWindow(QWidget):
    def __init__(self, proceso):
        super().__init__()
        self.setWindowTitle("Paro de emergencia")
        self.setMinimumSize(300, 150)

        self.proceso = proceso

        layout = QVBoxLayout()

        label = QLabel("¿Qué deseas hacer?")
        btn_continuar = QPushButton("🟢 Continuar secado")
        btn_abrir = QPushButton("📦 Abrir bandejas (detener)")

        btn_continuar.clicked.connect(self.continuar)
        btn_abrir.clicked.connect(self.detener)

        layout.addWidget(label)
        layout.addWidget(btn_continuar)
        layout.addWidget(btn_abrir)

        self.setLayout(layout)

    def continuar(self):
        self.proceso.reanudar()
        self.close()

    def detener(self):
        self.proceso.detener_total()
        self.close()

# ------------------ VENTANA PROCESO ------------------
class ProcesoWindow(QWidget):
    def __init__(self, temp_obj, tiempo):
        super().__init__()
        self.setWindowTitle("Proceso en ejecución")
        self.setMinimumSize(400, 200)

        self.temp_obj = temp_obj
        self.tiempo = tiempo

        self.layout = QVBoxLayout()

        self.label = QLabel("Iniciando...")
        self.btn_stop = QPushButton("🔴 PARO DE EMERGENCIA")

        self.btn_stop.clicked.connect(self.parar)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.btn_stop)

        self.setLayout(self.layout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.controlar)
        self.timer.start(2000)

    def controlar(self):
        temp_actual = 50  # simulación

        if temp_actual < self.temp_obj:
            estado = "Calefactor ON"
        else:
            estado = "Calefactor OFF"

        self.label.setText(f"Temp: {temp_actual}°C | {estado}")

    def parar(self):
        self.timer.stop()
        self.label.setText("⛔ PAUSADO")
        self.decision = DecisionWindow(self)
        self.decision.show()

    def reanudar(self):
        self.label.setText("Reanudando...")
        self.timer.start(2000)

    def detener_total(self):
        self.label.setText("📦 Bandejas abiertas - proceso terminado")

# ------------------ VENTANA FRUTA ------------------
class FrutaWindow(QWidget):
    def __init__(self, fruta):
        super().__init__()
        self.setWindowTitle(fruta)
        self.setMinimumSize(350, 200)

        self.datos = frutas[fruta]

        layout = QVBoxLayout()

        info = QLabel(
            f"Temperatura: {self.datos['temp']} °C\n"
            f"Tiempo: {self.datos['tiempo']} h\n"
            f"Espesor: {self.datos['espesor']}"
        )

        btn = QPushButton("INICIAR")
        btn.clicked.connect(self.iniciar)

        layout.addWidget(info)
        layout.addWidget(btn)

        self.setLayout(layout)

    def iniciar(self):
        self.proc = ProcesoWindow(self.datos["temp"], self.datos["tiempo"])
        self.proc.show()

# ------------------ VENTANA MANUAL ------------------
class ManualWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Modo Manual")
        self.setMinimumSize(350, 200)

        layout = QVBoxLayout()

        self.temp = QSpinBox()
        self.temp.setRange(0, TEMP_MAX)
        self.temp.setValue(50)

        self.tiempo = QSpinBox()
        self.tiempo.setRange(1, 24)

        btn = QPushButton("INICIAR")
        btn.clicked.connect(self.iniciar)

        layout.addWidget(QLabel("Temperatura °C"))
        layout.addWidget(self.temp)
        layout.addWidget(QLabel("Tiempo (h)"))
        layout.addWidget(self.tiempo)
        layout.addWidget(btn)

        self.setLayout(layout)

    def iniciar(self):
        self.proc = ProcesoWindow(self.temp.value(), self.tiempo.value())
        self.proc.show()

# ------------------ VENTANA PRINCIPAL ------------------
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Deshidratador")
        self.setMinimumSize(300, 150)

        layout = QVBoxLayout()

        self.combo = QComboBox()
        self.combo.addItems(frutas.keys())

        btn_fruta = QPushButton("Seleccionar fruta")
        btn_manual = QPushButton("Modo manual")

        btn_fruta.clicked.connect(self.abrir_fruta)
        btn_manual.clicked.connect(self.abrir_manual)

        layout.addWidget(self.combo)
        layout.addWidget(btn_fruta)
        layout.addWidget(btn_manual)

        self.setLayout(layout)

    def abrir_fruta(self):
        fruta = self.combo.currentText()
        self.win = FrutaWindow(fruta)
        self.win.show()

    def abrir_manual(self):
        self.win = ManualWindow()
        self.win.show()

# ------------------ MAIN ------------------
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())