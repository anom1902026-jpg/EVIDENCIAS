
from blessed import Terminal
from Varios import nuevo_subtema, nuevo_tema 

term = Terminal ()

print ("hola mundo")


"""
este es un comentario de muchas lineas

"""


# se explican las variables en python
nuevo_tema ("variables")
#int: numeros enteros
edad = 21 
print("edad:", edad)
#float: numero con punto decimal
estatura = 1.7
print("estatura",estatura)
#str: cadena de caracteres
nombre = "toño"
print("nombre", nombre)
#bool: variable boleana
fuma = True
print("fuma", fuma)

nuevo_tema("Operadores Aritmetico")
numero1 = 7
numero2 = 3
print ("numero1", numero1)
print ("numero2", numero2)
print ("numero1 + numero2", numero1+numero2)
print ("numero1 - numero2", numero1-numero2)
print ("numero1 / numero2", numero1/numero2)
print ("numero1 * numero2", numero1*numero2)
print ("numero1 % numero2", numero1%numero2)
print ("numero1 ** numero2", numero1**numero2)

nuevo_tema("Operadores Logicos")
estudia=True
pasara=False
print("estudia:", estudia)
print("pasara:", pasara)

print("estudia and pasara", estudia and pasara)
print("estudia or pasara", estudia or pasara)
print("estudia not pasara", not estudia)
print("estudia xor pasara", estudia ^ pasara)

nuevo_tema("Instruciones de Control")

print ("-------- If-else")
numero_a = 6
numero_b = 5
print ("numero_a:", numero_a)
print ("numero_b:", numero_b)

if numero_a > numero_b:
    print(f"El numero {numero_a} es mayor al numero {numero_b}")
if numero_a >= numero_b:
    print(f"El numero {numero_a} es mayor o igual al numero {numero_b}")
if numero_a < numero_b:
    print(f"El numero {numero_a} es menor al numero {numero_b}")
if numero_a <= numero_b:
    print("El numero {numero_a} es menor o igual al numero {numero_b}")
if numero_a == numero_b:
    print(f"El numero {numero_a} es igual al numero {numero_b}")


nuevo_tema("str: cadena de caracteres")

nombre2 = "Arturo"
nombre3 = "José"

saludo = f"hola {nombre2} '¿cómo estas', mi nombre es {nombre3}"
print(saludo)

saludo2 = "hola {} '¿como estas?', mi nombre es {}" .format(nombre2, nombre3)
print(saludo2)

print("hola", nombre2, "'¿como estas?, mi nombre es'", nombre3)

print("debo venir a clases\n" *10)
print(nombre2, nombre3)
print(nombre2, nombre3, sep="********", end="------")
print()


def nuevo_tema(tema):
    print("="*20)
    print(f"====== {tema} ======")
    print("="*20)

nuevo_tema("funciones")

nuevo_tema("list: listas")
frutas=['kiwis', 'naranjas', 'peras', 'manzanas', 'uvas', 'limones']
nuevo_subtema('Imprimiendo la lista')
print("frutas:", frutas)

nuevo_subtema('selecionando un elemento')
print("frutas[2]", frutas[2])

nuevo_subtema('mostrar el tamaño de la lista')
print("len(ftutas)", len(frutas))

nuevo_subtema('obtener desde el elemento 2 hasta el 3')
print

nuevo_subtema('aagregando elementos')
frutas.append('papayas')
frutas.append('sandias')
print("frutas", frutas)

nuevo_subtema('quitando elementos')
frutas.remove('peras')
print("frutas", frutas)

nuevo_subtema('obtener desde el elemento1 hasta el 5 cada 2 elementos')
print("fruts[1:6:2]", frutas[1:2:6])

nuevo_subtema('obtener el ultimo elemento')
print("frutas[-1]", frutas[-1])

nuevo_subtema('obtener el penultimo elemento')
print("frutas[-2]", frutas[-2])

nuevo_subtema('obtener el anteultimo elemento')
print("frutas[-3]", frutas[-3])

nuevo_subtema('invitiendo la lista')
print("frutas:", frutas)
frutas .reverse()
print("frutas:", frutas)

nuevo_subtema('ordenando la lista')
print("frutas:", frutas)
frutas .sort()
print("frutas:", frutas)

nuevo_subtema('quitar elemento')
print("frutas:", frutas)
elemento_removido = frutas.pop(1)
print("frutas:", frutas)
print("elemento_removido:", elemento_removido)

nuevo_subtema('agregar elemento en la posicion3')
print("frutas:", frutas)
frutas.insert(3, 'cerezas')
print("frutas:", frutas)

#nuevo_subtema('borrar lista')
#frutas.clear ()
print("frutas:", term.bold_mediumorchid, frutas, term.normal)

print (term.green("funciona blessed"))