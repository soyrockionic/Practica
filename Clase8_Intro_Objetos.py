class Jugador:
    def __init__(self, nombre, juego="Tetris", tiene_equipo=False, equipo=None):
        self.nombre = nombre
        self.juego = juego
        self.tiene_equipo = tiene_equipo
        self.equipo = equipo
        self.puntos = 0

    def jugar(self):
        if self.tiene_equipo:
            print (f"{self.nombre} juega en el equipo {self.equipo} al {self.juego}")
        else:
            print(f"{self.nombre} juega solo al {self.juego}")

    def incrementar(self, puntos):
        self.puntos += puntos
        return print(f"{self.nombre} tiene {self.puntos} puntos")  


class JugadorDeFIFA(Jugador):
    def __init__(self, nombre, equipo):
        Jugador.__init__(self, nombre, "FIFA", True, equipo)

class JugadorDeLOL(Jugador):
    def __init__(self, nombre, equipo):
        Jugador.__init__(self, nombre, "LOL")

print()

nico = JugadorDeFIFA('Nico Villalba', "Guild Esports")
nico.jugar()
nico.incrementar(50)
print("-"*30)
faker = JugadorDeLOL("Faker", "SK Telecom")
faker.jugar()
faker.incrementar(30)

print("-"*30)
nico.incrementar(20)