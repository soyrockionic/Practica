palabra = input('Ingresa una palabra ')
while palabra != 'fin' :
    if palabra[0] == palabra[-1] :
        print(f"{palabra}")    
    palabra = input('Ingresa una palabra ')