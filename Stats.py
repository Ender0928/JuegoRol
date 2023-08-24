import random

class Stats:
    def __init__(self):
        self.Strength = random.randint(8,12)
        self.Dexterity = random.randint(8,12)
        self.Constitution = random.randint(8,12)
        #self.Intelligence = 10
        self.Wisdom = random.randint(8,12)
        #self.Charisma = 10
    
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
                  
    def __str__(self):
        #return "STR: " + str(self.Strength) + "\nDEX: " + str(self.Dexterity) + "\nCON: " + str(self.Constitution) + "\nINT: " + str(self.Intelligence) + "\nWIS: " + str(self.Wisdom) + "\nCHA: " + str(self.Charisma)
        return "STR: " + str(self.Strength) + "\nDEX: " + str(self.Dexterity) + "\nCON: " + str(self.Constitution) + "\nWIS: " + str(self.Wisdom)
    
