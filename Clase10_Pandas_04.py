import pandas as pd


url = "https://www.infozona.com.ar/aumento-de-cigarrillos-precios-2022/"

result = pd.read_html(url)

tabla_h = result[0]
tabla_h = tabla_h.drop([0,3,12,19,26,29,33], axis='rows') #Elimino la filas con valor nulo
print('Lista de precios 2022 de cigarrillos Massalin Particulares')
print()
print(tabla_h)

print()
print('Lista de cigarrilos que cuestan mas de 250 pesos')
new_tabla = tabla_h[tabla_h['Precios'] > 250]
print(new_tabla)

print()
print('Lista de los 5 cigarrillos mas caros')
print(tabla_h.sort_values(by='Precios',ascending=False).head())