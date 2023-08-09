import random

class Dado:
    def __init__(self, lados):
        self.lados = lados

    def rolar(self):
        return random.randint(1, self.lados)