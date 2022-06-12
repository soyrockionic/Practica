class Carta():
    def __init__(self, tipo, numero):
        self._tipo = tipo
        self._numero = numero

    def __str__(self):
        return (f"{self._numero} de {self._tipo}")
 
    def get_tipo(self):
        return self._tipo
        
class Mazo():
    def __init__(self, tipo):
        self._tipo = tipo
        self._cartas = []
        self._descartadas = []
        self._posicion = 0
        
    def __iter__(self):
        return(self) 

    def __next__(self):
        if self._posicion == len(self._cartas):
            raise(StopIteration)
        carta = self._cartas[self._posicion]
        self._posicion = self._posicion + 1
        return carta
    
    def agregar_carta(self, carta):
        if carta.get_tipo() == self._tipo:
            self._cartas.append(carta)
        else:
            self._descartadas.append(carta)
        
mazo_espadas = Mazo("oro")
mazo_espadas.agregar_carta(Carta("oro", 3))
mazo_espadas.agregar_carta(Carta("oro", 4))
mazo_espadas.agregar_carta(Carta("espadas", 1))

print()
for carta in mazo_espadas:
     print(carta)

