import PySimpleGUI as sg

bandas = {
    "William Campbell": {"ciudad": "La Plata", "ref": "www.instagram.com/williamcampbellok"},
    "Buendia": {"ciudad": "La Plata", "ref":"https://buendia.bandcamp.com/"},
    "Lumine": {"ciudad": "La Plata", "ref": "https://www.instagram.com/luminelp/"},
    "La Renga": {"ciudad": "XXXX", "ref": "ALGUNA"},
    "Divididos": {"ciudad": "XXXX", "ref": "http://divididos.com.ar/"}}

mis_bandas = []

layout = [[sg.Input()], [sg.Button("OOK")]]
window = sg.Window("Elementos basicos", layout, margins=(80,60))
event, values = window.read()
window.close()

while values[0] != "fin":
    try:
        mis_bandas.append({"banda": values[0], "datos":bandas[values[0]]})
        window.close()
    except KeyError:
        layout = [[sg.Text("Ingresaste una banda que no tengo registrada")], [sg.Button("Volver")]]
        window = sg.Window("Bandas de Rock Nacional", layout, margins=(80,60))
        event, values = window.read()
        window.close()

    layout = [[sg.Input()], [sg.Button("OOK")]]
    window = sg.Window("Bandas de Rock Nacional", layout, margins=(80,60))
    event, values = window.read()
    window.close()

lista = ""
for banda in mis_bandas:
   lista = lista + str(banda) + "\n"

layout = [[sg.Text("Bandas de Rock Nacional\n" + "-"*100)], [sg.Text(lista)], [sg.Button("  Salir  ")]]

window = sg.Window("Rock Argento", layout, margins=(80,60))
event, values = window.read()
window.close()