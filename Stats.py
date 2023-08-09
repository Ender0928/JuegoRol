class Stats:
    def __init__(self):
        self.Strength = 10
        self.Dexterity = 10
        self.Constitution = 10
        self.Intelligence = 10
        self.Wisdom = 10
        self.Charisma = 10
        
    def __str__(self):
        return "STR: " + str(self.Strength) + "\nDEX: " + str(self.Dexterity) + "\nCON: " + str(self.Constitution) + "\nINT: " + str(self.Intelligence) + "\nWIS: " + str(self.Wisdom) + "\nCHA: " + str(self.Charisma)
        
    
