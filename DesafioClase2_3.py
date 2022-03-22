notas = []

nota = int(input('Ingresa una nota '))
while nota != -1:
    notas.append(nota)
    nota = int(input('Ingresa una nota '))

print()
print(notas)

print()
print(f"Promedio {sum(notas) / len(notas)}")

print()
cont = 0
for i in range(len(notas)) :
    if notas[i] < sum(notas) / len(notas) :
        cont += 1
print(f"Cantidad de notas menores a '{sum(notas) / len(notas)}' : {cont}")
 