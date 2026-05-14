from Varios import nuevo_tema, nuevo_subtema

nuevo_tema("Funciones esenciales")
nuevo_subtema("captura")
#nombre=input("Por favor introduce tu nombre:")
#print(f"El nombre introducido es:{nombre}")

nuevo_subtema ("Impresion base")
numero= 912345
print(f"el numero en decimal: {numero}")
print(f"el numero en hexadecimal: {hex(numero)}")
print(f"el numero en binario: {bin(numero)}")
print(f"el numero en octal: {oct(numero)}")

nuevo_subtema("cambio de tipo")
numero_string = "342"
print(f"numero en entero: {int(numero_string)+88}")

numero_string2= "342.88"
print(f"numero en flotante: {float(numero_string2)+13}")

numero3= 67.34
print(f"numero convertido a cadena de caracteres: {str(numero3) + 'gatos'}")

nuevo_subtema("caracter a ascii")
letra = 'f'
representacion_ascii = ord(letra)
print(f"La representacion ascii de la letra {letra} \ es {representacion_ascii} ")

nuevo_subtema("ascii a caracter")
codigo = 88
letra = chr (codigo)
print(f"el simbolo del codigo {codigo} es {letra}")

