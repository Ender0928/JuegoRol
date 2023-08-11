import Stats, Sala, Objeto, random
from Objeto import *

class Personaje:
    def __init__(self, vida: int, nombre: str, sala: Sala):
        self.vidaMax = vida
        self.vidaActual = vida
        self.nivel = 0
        self.nombre = nombre
        self.sala = sala
        self.danioBase = 2
        self.stats = Stats.Stats()
        self.velocidad_base = 1
        
    def getVelocidad(self):
        return self.velocidad_base
         
    def getNombre(self):
        return self.nombre
    
    def getVida(self):
        return self.vidaActual
    
    def atacar(self, objetivo):
        objetivo.recibirDanio(random.randint(self.danioBase-2, self.danioBase+2))
    
    def recibirDanio(self,ataque: int):
        self.vidaActual -= ataque
        if self.vidaActual <= 0:
            self.vidaActual = 0
                   
    def __str__(self):
        return self.nombre + " (" + str(self.vidaActual) + "/" + str(self.vidaMax) + ")"  + " nivel" + str(self.nivel)
    

#___________________________________________Protagonista__________________________________________________

class Humano(Personaje):
    
    arma: Arma
    
    def __init__(self, vida: int, nombre: str, sala: Sala):
        super().__init__(vida, nombre, sala)
        self.mochila = Mochila()
        self.velocidad_base = 1
        self.danioBase = 8
        self.mejora = False
        
    def equiparArma(self, arma: Arma):
        self.arma = arma
        self.danio += arma.getAtaque           
            
    def consultar_mochila(self):
        if self.mochila :
            self.mochila.__str__()
        else:
            print('No tiene una mochila equipada ahora mismo')
            
    def getMochila(self):
        return self.mochila
    
    def equiparMochila(self, mochila: Objeto):
        self.mochila = mochila
        
    def elegir_clase(self):
        print('¿Que clase desea elegir?\n 1:Asesino \n 2:Guerrero \n 3:Mago')
        clase = input()
        if(clase == 1):
            return Asesino()
        elif(clase == 2):
            return Guerrero()
        elif(clase == 3):
            return Mago()
        else:
            print('No ha elegido ninguna clase válida')
            return self.elegir_clase()
        
class Asesino(Humano):
    
    def __init__(self, vida, nombre):
        super().__init__(vida, nombre)
        self.velocidad_base = 1
        self.PE = 50
        super.mejora = True
        
    def hab_esp(self):
        print('Apuñalas en un punto vital del enemigo')
        self.PE -= 20
        return self.arma.getAtaque() * 2
        
class Guerrero(Humano):
    
    def __init__(self, vida, nombre):
        super().__init__(vida, nombre)
        self.velocidad_base = 1
        self.PE = 75
        super.mejora = True
        
    def hab_esp(self):
        print('Realizas un placaje al enemigo')
        self.PE -= 25
        return self.arma.getAtaque() * 1.5
        
class Mago(Humano):
    
    def __init__(self, vida: int, nombre: str):
        super().__init__(vida, nombre)
        self.velocidad_base = 1
        self.PE = 100
        super.mejora = True
        
    def hab_esp(self):
        print('Lanzas una bola de fuego al enemigo')
        self.PE -= 45
        return self.arma.getAtaque() * 2.5        
#___________________________________________Enemigos______________________________________________________
class Goblin(Personaje):
    
    numGoblin: int = 0
    ataque: int = 3
    defensa: int = 3
    def __init__(self, vida: int, nombre: str, sala: Sala):
        super().__init__(vida, nombre, sala)
        Goblin.numGoblin += 1
        self.ataque = random.randint(Goblin.ataque-2, Goblin.ataque+2)
        self.defensa = random.randint(Goblin.defensa-2, Goblin.defensa+2)  
        
class Moblin(Personaje):
    numMoblin: int = 0
    ataque: int = 10
    defensa: int = 10
    def __init__(self, vida: int, nombre: str, sala: Sala):
        super.__init__(vida, 'Moblin'+Moblin.numMoblin, sala)
        Moblin.numMoblin += 1
        self.ataque = random.randint(Moblin.ataque-3, Moblin.ataque+3)
        self.defensa = random.randint(Moblin.defensa-3, Moblin.defensa+3)
        
class Ogro(Personaje):
    numOgro: int = 0
    ataque: int = 15
    defensa: int = 15
    def __init__(self, vida: int, nombre: str, sala: Sala):
        super.__init__(vida, 'Ogro'+Ogro.numOgro, sala)
        Ogro.numOgro += 1
        self.ataque = random.randint(Ogro.ataque-3, Ogro.ataque+4)
        self.defensa = random.randint(Ogro.defensa-3, Ogro.defensa+4)