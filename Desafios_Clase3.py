import Funciones as m

print("-" * 30)
m.imprimo("Hola",15)
print("-" * 30)
m.imprimo([4,7],True)

print("-" * 30)
print(m.ordeno("Triste cancion de amor."))

print("-" * 30)
m.imprimo_muchos_valores("Hola", 
    "hello", "Hallo", "Aloha ", 
    ingles= "hello", aleman="Hallo", vietnam="Cin Chao")

usuarios = [
    ("Jony Boy", "Nivel30", 5400),
    ("1962", "Nivel12", 740),
    ("Straka", "Nivel12", 1020),
    ("Caike", "nivel11", 940)
]
print()
print("-" * 30)
print(m.ordeno3(usuarios))
