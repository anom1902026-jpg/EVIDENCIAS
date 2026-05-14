from Varios import nuevo_tema, nuevo_subtema

nuevo_tema("diccionarios")
nuevo_subtema("creando diccionario")

alumno = {
    "nombre": "coco",
    "apellido": "cruz",
    "edad":27,
    "hobbys": ["coleccionar diccionarios", "jugar"]
}

print("alumno:", alumno)

nuevo_subtema("obteniendo claves")
print("alumno.keys():", alumno.keys())

nuevo_subtema("obteniendo valores")
print("alumno.values():", alumno.values())

nuevo_subtema("obteniendo elementos")
print("alumno.items():", alumno.items())

nuevo_subtema("obteniendo el valor de una clave")
print("alumno['nombre']:", alumno['nombre'])
print("alumno.get('nombre'):", alumno.get('nombre'))

#nuevo_subtema("obteniendo el valor de una clave que no")
#print("alumno['telefono']:", alumno['telefono'])
#print("alumno.get('telefono'):", alumno.get('telefono'))

nuevo_subtema("anexando elementos")
print("alumno.update({'telefono':911}):", alumno.update({'telefono':911}))

print("alumno:", alumno)

nuevo_subtema("quitando elemento")
valor_extraido = alumno.pop('nombre')
print("alumno_extraido'",valor_extraido)
print("alumno:",alumno)

nuevo_subtema("recorriendo todos los elementos (for)")
for clave, valor in alumno.items():
    print(f"{clave}, {valor}")

nuevo_subtema("eliminando todos los items")
alumno.clear()
print("alumno:", alumno)

