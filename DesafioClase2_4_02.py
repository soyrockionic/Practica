nombre = input("Ingresa un nombre 'fin' para finalizar ")
dicci = {}
while nombre != "fin" :
    nota = int(input(f"Ingresa la nota de {nombre} "))
    dicci[nombre] = nota
    nombre = input("Ingresa un nombre 'fin' para finalizar ")

print()
print(dicci)

print()
for i in dicci :
    print(i + f" {dicci[i]}")

print()
suma = 0
for i in dicci :
    suma += dicci[i]
promedio = 0 if len(dicci) == 0 else suma / len(dicci)
print(f"Promedio {promedio}")

for i in dicci :
    if dicci[i] < promedio :
        print(f"{i} esta por debajo del promedio")