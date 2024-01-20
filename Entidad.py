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
        self.stats = Stats()
        self.velocidad_base = 1
        self.exp = 0
        self.defensa = 0
        
    def getVelocidad(self):
        return self.velocidad_base
         
    def getNombre(self):
        return self.nombre
    
    def getVida(self):
        return self.vidaActual
    
    def atacar(self, objetivo):
        objetivo.recibirDanio(random.randint(self.danioBase-2, self.danioBase+2) * (self.stats.getStrength()/10))
    
    def recibirDanio(self,ataque: int):
        dañoTotal = ataque - self.defensa
        if dañoTotal < 0:
            dañoTotal = 1
            
        self.vidaActual -= dañoTotal
        
        if self.vidaActual <= 0:
            self.vidaActual = 0
     
    def getExp(self):
        return self.exp
                  
    def __str__(self):
        return self.nombre + " (" + str(self.vidaActual) + "/" + str(self.vidaMax) + ")"  + " nivel" + str(self.nivel)
    

#___________________________________________Protagonista__________________________________________________

class Humano(Personaje):    
    
    def __init__(self, vida: int, nombre: str, sala: Sala):
        super().__init__(vida, nombre, sala)
        self.mochila = Mochila()
        self.mochila.agregarObjeto(PocionVida())
        self.velocidad_base = 1
        self.danioBase = 8
        self.defensa = 0
        self.PE = 0
        self.PEMax = 0
        self.exp = 0
        self.subirNivel = 100
        self.nivel = 0
        self.arma = None
        self.armadura = None
        self.mejora = False
        
    def equiparArma(self, arma: Arma):
        self.arma = arma
        self.danioBase += arma.getAtaque()
        self.velocidad_base += arma.getVelocidad()          
    
    def equiparArmadura(self, armadura: Armadura):
        self.armadura = armadura
        self.defensa += armadura.getDefensa()
                
    def consultar_mochila(self):
        if self.mochila :
            print('Mochila: ')
            self.mochila.__str__()
        else:
            print('No tiene una mochila equipada ahora mismo')
            
    def getMochila(self):
        return self.mochila
    
    def equiparMochila(self, mochila: Objeto):
        self.mochila = mochila
        
    def recuperarVida(self, vida: int):
        self.vidaActual += vida
        if self.vidaActual > self.vidaMax:
            self.vidaActual = self.vidaMax
            
    def recuperarPE(self, PE: int):
        if(self.mejora == True):
            self.PE += PE
            if self.PE > self.PEMax:
                self.PE = self.PEMax
            return True
        else:
            print('No puede recuperar PE porque no tiene habilidad especial')
            return False
    
    def ganarExp(self, exp: int):
        self.exp += exp
        if self.exp >= self.subirNivel:
            self.subirNivel *= 1.75
            self.nivel += 1
            self.vidaMax *= 1.5
            self.vidaActual = self.vidaMax
            self.PEMax += 5
            self.PE = self.PEMax
            self.stats.agregarPuntos()
            #hacer que el usuario elija que stat subir
            print('Has subido de nivel')
            if(self.nivel == 5 and self.mejora == False):
                self.mejorar()   
    
    def getNivel(self):
        return self.nivel
             
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
    
    def atacar(self, objetivo):
        ataque = random.randint(0, self.stats.getDexterity())
        if ataque == 0:
            print(self.nombre + 'ha fallado el ataque')
        else: 
            objetivo.recibirDanio(random.randint(self.danioBase-2, self.danioBase+2) * int((self.stats.getStrength()/10)))
            if self.arma:
                if self.arma.objetoUsado():
                    self.danioBase -= self.arma.getAtaque()
                    self.velocidad_base -= self.arma.getVelocidad()
                    self.arma = None
                    
    def recibirDanio(self,ataque: int):
        dañoTotal = (int(ataque*(10/self.stats.getConstitution())) - self.defensa)
        esquivar = random.randint(0, self.stats.getDexterity())
        if esquivar == 0:
            dañoTotal = 0
            print(self.nombre + 'ha esquivado el ataque')
        if dañoTotal < 0:
            dañoTotal = 1
            
        self.vidaActual -= dañoTotal
        
        if self.vidaActual <= 0:
            self.vidaActual = 0
            
        if self.armadura:
            if self.armadura.objetoUsado():
                self.defensa -= self.armadura.getDefensa()
                self.armadura = None
                
class Asesino(Humano):
    
    def __init__(self, vida, nombre):
        super().__init__(vida, nombre)
        self.velocidad_base = 1
        self.PEMax = 50
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
        self.PEMax = 75
        super.mejora = True
        
    def hab_esp(self):
        print('Realizas un placaje al enemigo')
        self.PE -= 25
        return self.arma.getAtaque() * 1.5
    
    def intimidar(self, enemigo):
        print('Intimidas al enemigo y reduces su ataque')
        self.PE -= 25
        enemigo.ataque -= 3
        
        
class Mago(Humano):
    
    def __init__(self, vida: int, nombre: str):
        super().__init__(vida, nombre)
        self.velocidad_base = 1
        self.PE = 100
        self.PEMax = 100
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
    
    def __init__(self, vida: int, sala: Sala):
        super().__init__(vida, 'goblin' + str(Goblin.numGoblin), sala)
        Goblin.numGoblin += 1
        self.ataque = random.randint(Goblin.ataque-2, Goblin.ataque+2)
        self.defensa = random.randint(Goblin.defensa-2, Goblin.defensa+2)  
        self.exp = 20
    
    def morir(self):
        Goblin.numGoblin -= 1
        print('El goblin ha muerto')
            
class Moblin(Personaje):
    
    numMoblin: int = 0
    ataque: int = 10
    defensa: int = 10
    
    def __init__(self, vida: int, sala: Sala):
        super.__init__(vida, 'Moblin'+ str(Moblin.numMoblin), sala)
        Moblin.numMoblin += 1
        self.ataque = random.randint(Moblin.ataque-3, Moblin.ataque+3)
        self.defensa = random.randint(Moblin.defensa-3, Moblin.defensa+3)
        self.exp = 50
        
    def morir(self):
        Moblin.numMoblin -= 1
        print('El moblin ha muerto')
        
class Ogro(Personaje):
    
    numOgro: int = 0
    ataque: int = 15
    defensa: int = 15
    
    def __init__(self, vida: int, sala: Sala):
        super.__init__(vida, 'Ogro'+ str(Ogro.numOgro), sala)
        Ogro.numOgro += 1
        self.ataque = random.randint(Ogro.ataque-3, Ogro.ataque+4)
        self.defensa = random.randint(Ogro.defensa-3, Ogro.defensa+4)
        self.exp = 100
        
    def morir(self):
        Ogro.numOgro -= 1
        print('El ogro ha muerto')