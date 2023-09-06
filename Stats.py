import random, Dado, Stats
from Dado import *


class Stats:
    def __init__(self):
        dado = Dado(6)
        self.Strength = dado.caracteristica()
        self.Dexterity = dado.caracteristica()
        self.Constitution = dado.caracteristica()
        #self.Intelligence = dado.caracteristica()
        self.Wisdom = dado.caracteristica()
        #self.Charisma = dado.caracteristica()
    
    def getStrength(self):
        return self.Strength
    
    def getDexterity(self):
        return self.Dexterity
    
    def getConstitution(self):
        return self.Constitution
    
    def getWisdom(self):
        return self.Wisdom
    
    def sumarPuntoStrenght(self):
        self.Strength += 1
        
    def sumarPuntoDexterity(self):
        self.Dexterity += 1
        
    def sumarPuntoConstitution(self):
        self.Constitution += 1
        
    def sumarPuntoWisdom(self):
        self.Wisdom += 1
        
    def agregarPuntos(self):
        self.Strength += random.randint(0,2)
        self.Dexterity += random.randint(0,2)
        self.Constitution += random.randint(0,2)
        self.Wisdom += random.randint(0,2)
    
    def requerimientoObjeto(self):
        self.Strength = random.randint(9,14)  
        self.Dexterity = random.randint(9,14)
        self.Wisdom = random.randint(9,14)
    
    def compararStats(self, stats: Stats) -> bool:
        if(self.Strength < stats.getStrength() or self.Dexterity < stats.getDexterity() 
           or self.Constitution < stats.getConstitution() or self.Wisdom < stats.getWisdom()):
            return False
        return True
                 
    def __str__(self):
        #return "STR: " + str(self.Strength) + "\nDEX: " + str(self.Dexterity) + "\nCON: " + str(self.Constitution) + "\nINT: " + str(self.Intelligence) + "\nWIS: " + str(self.Wisdom) + "\nCHA: " + str(self.Charisma)
        return "STR: " + str(self.Strength) + "\nDEX: " + str(self.Dexterity) + "\nCON: " + str(self.Constitution) + "\nWIS: " + str(self.Wisdom)
    
