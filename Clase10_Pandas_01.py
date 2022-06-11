import pandas as pd


url = "https://es.wikipedia.org/wiki/Copa_Am%C3%A9rica"

result = pd.read_html(url)


ediciones = result[1]

ediciones = ediciones.drop([4, 8, 12, 13], axis="columns")

ediciones = ediciones[2:]

ediciones.columns = ediciones.iloc[0]

ediciones = ediciones.drop([31],axis="rows")

print()
print(ediciones)