from enum import Enum, auto

class TipoArma(Enum):
    ESPADA = (5, 0.5)
    LANZA = (6, 0.7)
    HACHA = (8, 1)

    def __init__(self, ataque: int, velocidad: int):
        self.ataque = ataque
        self.velocidad = velocidad
        
    def getAtaque(self):
        return self.ataque
    
    def getVelocidad(self):
        return self.velocidad