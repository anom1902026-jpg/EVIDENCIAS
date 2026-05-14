
class Madre:
    def __init__(self):
        print("soy madre")
    
    def pegar(self):
        print("estoy pegando")


class Padre:
    def __init__(self):
        print("soy padre")
    
    def reganar(self):
        print("estoy regañando")




class Hijo(Padre, Madre):
    # este es el constructor
    def __init__(self):
        #super().__init__()
        Padre.__init__(self)
        Madre.__init__(self)
        print("soy Hijo")

    
def main():
        print("iniciando el programa")
        hijo = Hijo()
        hijo.reganar()
        hijo.pegar()
    
if __name__ == "__main__":
        main()
