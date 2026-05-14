from enum import Enum

import threading
import time

class EstadoMotor(Enum):
    home = 0
    estado_1 = 1
    estado_2 = 2
    estado_3 = 3
    estado_4 = 4
    estado_5= 5
    estado_6 = 6
    estado_7 = 7
    estado_8 = 8

class MotorPasos: 
    def __init__(self):
        print("dentro de MotorPasos")
        #ENTRADAS
        self.e1_arranque = False
        self.e2_giro = False


        #salidas
        self.bobina_A = False
        self.bobina_B = False
        self.bobina_C = False
        self.bobina_D = False

        self.funcionando = False
        self.contador = 0
        self.estado_actual = EstadoMotor.home
        self.tarea = threading.Thread(target=self.motor_funcionando)
        self.tarea.start()
    
    def motor_funcionando(self):
        print ("iniciando el motor")
        self.funcionando = True
        
        while self.funcionando:
            self.contador += 1
            print(f"contador {self.contador}")
            if self.e1_arranque:
                self.estado_aux = self.estado_actual
                match(self.estado_aux):
                    case EstadoMotor.home:
                        if self.e2_giro:
                            self.estado_actual = EstadoMotor.estado_1
                        else:
                            self.estado_actual= EstadoMotor.estado_1
            
            
            
            time.sleep(1)
    




def main():
    print("dentro de main")
    motor = MotorPasos()

if __name__ == "__main__":
    main()
