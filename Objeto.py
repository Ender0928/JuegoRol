import TipoArma, Stats

class Objeto:
    
    def __init__(self, nombre: str, descripcion: str):
        self.nombre = nombre
        self.descripcion = descripcion
        
class Mochila(Objeto):
    
    def __init__(self, nombre: str, descripcion: str, capacidad: int):
        super().__init__(nombre, descripcion)
        self.capacidad = capacidad
        self.contenido = list(Objeto)
        
class Arma(Objeto):
    
    def __init__(self, nombre: str, descripcion: str, ataque: int, requerimiento: Stats, velocidad: int, tipoArma: TipoArma):
        super().__init__(nombre, descripcion)
        self.ataque = ataque
        self.requerimiento = requerimiento
        self.velocidad = velocidad
        self.tipoArma = tipoArma
        
    def __str__(self):
        return self.nombre + " (Ataque: " + str(self.ataque) + " - Velocidad: " + str(self.velocidad) + ")"
    
    def getAtaque(self):
        return self.ataque + self.tipoArma.getAtaque()
    
    def getVelocidad(self):
        return self.velocidad + self.tipoArma.getVelocidad()
    
    def getRequerimiento(self):
        return self.requerimiento
    
    def getDescripcion(self):
        return self.descripcion