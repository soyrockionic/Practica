import os
import csv
import PySimpleGUI as sg

logs = 'appstore_games.csv'
try:
    with open(os.path.join(logs)) as logs_moodle:
        data_logs = csv.reader(logs_moodle, delimiter=',')
        header, logs_recurso = next(data_logs), list(data_logs)

    juegos = []
    for lin in logs_recurso:
        if lin[7] == '0' and 'ES' in lin[12]:
            juegos.append(lin)

    layout = [[sg.Text("1 Lista de juegos gratis en español\n")],
               [sg.Text("2 Iconos de los 10 juegos con mas calificaciones\n")],
               [sg.Input()], [sg.Button("Play")]]
    window = sg.Window(title="Desafio 2 Clase 7", layout=layout, margins=(80, 60))
    event, values = window.read()
    window.close()

    lista = ""
    cont = 0
    if values[0] == "1":
        for juego in juegos:
            if cont < 10:
                lista = lista + str(juego[2]) + "\n"
            cont += 1

        layout = [[sg.Text("Juegos gratis en español\n" + "-"*80)],[sg.Text(lista)], [sg.Button("  Salir  ")]]
    elif values[0] == "2":
        layout = [[sg.Text("Opción 2 en construcción")], [sg.Button("Salir")]]
    else:
        layout = [[sg.Text("Se ingresó una opción inválida - Fin del programa")], [sg.Button("Salir")]]
except: 
    layout = [[sg.Text("Archivo no encontrado\n" + "-"*80)],[sg.Button("  Salir  ")]]

window = sg.Window("Desafio 2 Clase 7", layout, margins=(80, 60))
event, values = window.read()
window.close()