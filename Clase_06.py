import PySimpleGUI as sg

bandas = {
    "William Campbell": {"ciudad": "La Plata", "ref": "www.instagram.com/williamcampbellok"},
    "Buendia": {"ciudad": "La Plata", "ref":"https://buendia.bandcamp.com/"},
    "Lumine": {"ciudad": "La Plata", "ref": "https://www.instagram.com/luminelp/"},
    "La Renga": {"ciudad": "XXXX", "ref": "ALGUNA"},
    "Divididos": {"ciudad": "XXXX", "ref": "http://divididos.com.ar/"}}

mis_bandas = []

nombre_banda = input("\nIngresa el nombre de una banda: ")
while nombre_banda != "fin":
    try:
        mis_bandas.append({"banda": nombre_banda, "datos":bandas[nombre_banda]})
    except KeyError:
        print("Ingresaste el nombre de una banda que no tengo registrada")
    nombre_banda = input("\nIngresa el nombre de una banda: ")

for banda in mis_bandas:
   print(mis_bandas[0])

