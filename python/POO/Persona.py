

class Persona:
    #constructor
    def __init__ (self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.calificaciones = []
        #print ("dentro del constructor")

    def mostrar_calificaciones(self):
        texto = ""
        if self.calificaciones:
            for calif in self.calificaciones:
                texto = texto + ", " + str(calif)
            print (texto)
        else:
            print("sin calificaciones")

    def calificar(self):
        print("ingresa calificaciones escriba -1 para terminar")
        calif=0 
        while calif !='-1':
            calif= input("ingresa calificacion: ")
            if calif != '-1':
                self.calificaciones.append(float(calif))

    
    def saludar (self):
        print (f"hola como estas soy {self.nombre} {self.apellido}")
    
    #toString: representacionde cadena de caracteres del objeto
    def __str__(self):
        return f"mi nombre es {self.nombre} {self.apellido}"
def main():
    gael = Persona ("gael", "garrido")
    gael.saludar ()
    print(gael)

    print ("-----")
    oliver = Persona("oliver", "romero")
    oliver.saludar()
    print(oliver)

if __name__ == "__main__":
    main()