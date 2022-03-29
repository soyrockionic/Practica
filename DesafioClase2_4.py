lista = []

nombre = input("Ingresa un nombre 'fin' para finalizar ")
while nombre != "fin" :
    nota = int(input(f"Ingresa la nota de {nombre} "))
    lista.append((nombre, nota))
    nombre = input("Ingresa un nombre 'fin' para finalizar ")

print()
print(lista)

print()
suma = 0
for i in lista : 
    suma += i[1]
promedio = 0 if len(lista) == 0 else suma / len(lista)
print(f"Promedio {promedio}")

print()
if len(lista) != 0 :
    for i in lista :
        if i[1] < suma / len(lista) :
            print(f"{i[0]} esta por debajo del promedio")

