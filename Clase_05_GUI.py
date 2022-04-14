import PySimpleGUI as sg

titulos = open("Titulos_2021.txt", "r")
arch_titulos = titulos.read().split(";")

peliculas=""
for peli in arch_titulos:
    if "2021" in peli:
        peliculas = peliculas + peli + "\n"

layout = [[sg.Text("Titulos 2021 - Netflix\n" + "-"*40)], [sg.Text(peliculas)], [sg.Button("Salir")]]

window = sg.Window("Lista de Titulos 2021", layout, margins=(80,80))

event, values = window.read()

titulos-close()
window.close()