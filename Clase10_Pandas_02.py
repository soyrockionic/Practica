import pandas as pd


url = "https://es.wikipedia.org/wiki/Copa_Am%C3%A9rica"

result = pd.read_html(url)

tabla_h = result[4]
print()
print('Tabla historica')
print(tabla_h)

print()
print(tabla_h[['Equipo','Puntos','PJ']])

print()
print('Tabla de equipos que sus goles a favor es mayor a sus goles en contra')
tabla_h = tabla_h[tabla_h['GF'] > tabla_h['GC']]
print()
print(tabla_h[['Equipo','GF']])