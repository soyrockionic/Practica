def imprimo(*datos) :
    for val in datos :
        print(f"{val} es de tipo {type(val)}")


def imprimo_muchos_valores(mensaje_inicial, *en_otro_idioma, **en_detalle) :
    print("Mensaje original")
    print(mensaje_inicial)

    print("\nEn otros idiomas")
    print("-" * 30)
    for val in en_otro_idioma:
        print(val)
    print("\nEn detalle")
    print("-" * 30)

    for clave in en_detalle:
        print(f"{clave}: {en_detalle[clave]}")

    print("\nFuente: traductor de Google. ")


def ordeno(cadena) :
    lista = cadena.split()
    return sorted(lista, key=str.lower)


def ordeno3(cadenas) :
    return sorted(cadenas, key=lambda usuario: usuario[0])
