
import time
import threading

class Tarea: 
    def __init__(self, nombre:str, duracion:float):
        self.nombre = nombre
        self.duracion = duracion
        print (f"creando la tarea {self.nombre}")
        self.t = threading.Thread(target=self.iniciar_tarea)

    def iniciar (self):
        self.t.start()
    
    def iniciar_tarea(self):
        print(f"iniciando la terea {self.nombre}")
        time.sleep(self.duracion)
        print(f"terminando la tarea {self.nombre}")


def main ():
    print("iniciando el programa")
    tarea1 = Tarea("realizar los circuitos electronicos", 6)
    tarea2 = Tarea("Manufactura de la estructura", 4)
    tarea3 = Tarea("programar", 6)

    tarea1.iniciar()
    tarea2.iniciar()
    tarea3.iniciar()
    print("finalizando tarea")

if __name__ == "__main__":
    main()


