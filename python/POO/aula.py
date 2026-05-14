class Aula:
    def __init__(self, ubicacion, materia):
        self.ubicacion = ubicacion
        self.materia = materia
        self.alumnos = []
    
    def inscribir_alumno(self, alumno):
        self.alumnos.append(alumno)
        print("se ah inscrito un alumno nuevo")

    def mostrar_alumnos(self):
        if self.alumnos:
            print('='*10, f"lista de alumnos inscritos a {self.materia}",'='*10)
            for indice, alumno in enumerate (self.alumnos):
                print(f"{indice}.-{alumno}")
        
        else:
            print(f"no hay alumnos escritos a {self.materia}")
    
