def ingreso_notas() :

    nombre = input("Ingresa un nombre 'fin' para finalizar ")
    dicci = {}
    while nombre != "fin" :
        nota = int(input(f"Ingresa la nota de {nombre} "))
        dicci[nombre] = nota
        nombre = input("Ingresa un nombre 'fin' para finalizar ")

    return dicci


def calcular_promedio(notas) :
    suma = 0
    for i in notas :
        suma += notas[i]
    promedio = 0 if len(notas) == 0 else suma / len(notas)
    return promedio


def menores_al_prom(notas) :
    
    cont = 0
    for i in notas :
        if notas[i] < calcular_promedio(notas) :
            cont += 1

    return cont
    

notas = ingreso_notas()

print()
for i in notas :
    print(i + f" {notas[i]}")

print()
print(f"Promedio {calcular_promedio(notas):.2f}")

print(f"Cantidad de notas menores a {calcular_promedio(notas):.2f} = {menores_al_prom(notas)}")
