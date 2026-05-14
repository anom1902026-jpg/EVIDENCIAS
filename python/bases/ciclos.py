from Varios import nuevo_tema, nuevo_subtema

nuevo_tema("ciclo for")
nuevo_subtema("de 0 a 5")
for i in range (6):
    print(i)

nuevo_tema("ciclo for")
nuevo_subtema("de 3 a 11")
for i in range (3, 12):
    print(i)

nuevo_tema("ciclo for")
nuevo_subtema("de 3 11 de 2 en 2")
for i in range (3,12,2):
    print(i)

nuevo_subtema("con una lista")
cosas = ['refrigeradores', 'estufas', 'lavadoras', 'microondas', 'colchones', \
          'tambores', 'o fierro viejo que venda']
print("imprimiendo la lista")
print(f"cosas:{cosas}")
for cosa in cosas:
    print(f"se venden {cosa}")

nuevo_subtema("lista numerada")
for indice, cosa in enumerate(cosas):
    print(f"{indice} .- {cosa}")

nuevo_subtema("lista numerada reversa")
cosas.reverse()
for indice, cosa in enumerate(cosas):
    print(f"{indice} .- {cosa}")

nuevo_tema("ciclo while")
limite = 34
resultado = 0
vez = 0
while(resultado < limite):
    vez = vez +1
    print(f"se realizo {vez} veces")
    resultado = resultado +2
