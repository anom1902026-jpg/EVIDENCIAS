from aula import Aula
from Persona import Persona

def main():
    print("iniciando")
    laboratorio3 = Aula ("hidraulica", "programacion")

    laboratorio3.mostrar_alumnos()

    antonio = Persona("antonio", "quiroz")
    laboratorio3.inscribir_alumno(antonio)
    laboratorio3.mostrar_alumnos()

    roldan = Persona("Jose", "Roldan")
    laboratorio3.inscribir_alumno(roldan)
    laboratorio3.mostrar_alumnos()

    antonio.calificar ()
    antonio.mostrar_calificaciones()

if __name__ == '__main__':
    main()

