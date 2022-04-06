def codifica(cadena) : 
    for ch in cadena:
        print(ch + ' = ' + str(ord(ch)))

    cadena_encrip = map(lambda ch : chr(ord(ch) + 1), cadena)
    cadena_encrip = ' '.join(cadena_encrip)
    print()
    return cadena_encrip


cadena = input("Ingrese un texto ")
print(codifica(cadena))