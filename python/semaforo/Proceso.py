import time
import threading

from Temporizador import Temporizador

class Proceso:
    def __init__(self):
        self.X = []
        self.numeroX = 8

        self.Y = []
        self.numeroY = 8

        self.M = list()
        self.numeroM = 8
        self.worker = None

        for i in range(self.numeroX):
            self.X.append(False)
        
        for i in range(self.numeroY):
            self.Y.append(False)

        for i in range(self.numeroM):
            self.M.append(False)

        self.TON_0 = Temporizador("TON_00", 5)
        self.TON_1 = Temporizador("TON_01", 2)
        self.TON_2 = Temporizador("TON_02", 6)

        self.X[0] = True

        self.contador = 0
        self.proceso_funcionando = False

        self.tarea = threading.Thread(target=self.run_proceso)
    
    def iniciar_tarea(self):
        self.tarea.start()

    def run_proceso (self):
        self.proceso_funcionando = True
        while self.proceso_funcionando:

            # secuencia a realizar AQUI->
            self.M[0] = ( self.X[0] or self.M[0] ) and not self.X[1]

            self.TON_0.entrada = self.M[0] and not self.TON_2.salida
            self.TON_0.actualizar()

            self.TON_1.entrada = self.M[0] and self.TON_0.salida
            self.TON_1.actualizar()

            self.TON_2.entrada = self.M[0] and self.TON_1.salida
            self.TON_2.actualizar()

            self.Y[0] = self.M[0] and self.TON_1.salida
            self.Y[1] = self.M[0] and self.TON_0.salida and not self.TON_1.salida
            self.Y[2] = self.M[0] and not self.TON_0.salida


            # YA te pasaste


            if self.worker:
                # print(self.worker)
                self.worker.prender_luz_roja(self.Y[0])
                self.worker.prender_luz_amarilla(self.Y[1])
                self.worker.prender_luz_verde(self.Y[2])

            print(f"R: {self.Y[0]} A: {self.Y[1]} V: {self.Y[2]}")
            self.contador +=1
            ##print(f"contador: {self.contador}")
            time.sleep(0.001)

    def cambiar_valor_x(self, indice:int, valor:bool):
        if indice < self.numeroX:
            self.X[indice] = valor

    def establecer_worker(self, worker):
        self.worker = worker

    def __str__(self):
        return ""
    

def main():
    proceso = Proceso()
    proceso.iniciar_tarea()

if __name__ == "__main__":
    main()
