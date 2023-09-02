import random

class Dado:
    def __init__(self, lados: int):
        self.lados = lados

    def rolar(self) -> int:
        return random.randint(1, self.lados)
    
    def caracteristica(self) -> int:
        numeros = []
        for i in range(4):
            numeros.append(self.rolar())      
                
        numeros.pop(numeros.index(min(numeros)))
        return numeros[0] + numeros[1] + numeros[2]
    
def main():
    dado = Dado(6)
    print("Característica:", dado.caracteristica())
    
if __name__ == '__main__':
    main()