import pandas as pd

url = 'python_plus_acumulados.csv'

datos = pd.read_csv(url,header = 0)

# informo los primeros 10 ordenados alfabeticamente por nombre de mayor a menor
print(datos.head(10).sort_values(by='Nombre',ascending=False))

# informo nombre , apellido y puntaje total de los primeros 10
print(datos[['Nombre','Apellido(s)','Total Python plus']].head(10))

# informo los totales mayores a 140
puntos = datos['Total Python plus']
for i in puntos:
    if(float(i.replace(',','.')) > 140):
        print(i)