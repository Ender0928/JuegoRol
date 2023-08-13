import Entidad, random, Objeto
from Objeto import *
from Entidad import *

class Sala:
        numero = 0
        lista_objetos_recompensas = [Espada(10), Espada(12)] #'Pocion Vida', 'Mochila', 'Armadura', 'Lanza', 'Hacha', 'Pocion PE']
        
        def __init__(self):
            self.numero = Sala.numero 
            Sala.numero += 1
            self.enemigos = []
            self.recompensa = random.choice(Sala.lista_objetos_recompensas)
            
        def agregar_enemigo(self, *personaje : Entidad):
            self.enemigos.extend(personaje)
            self.enemigos.sort(key=lambda x: x.getVelocidad(), reverse=True)
            
        def eliminar_enemigo(self, personaje: Entidad):
            self.enemigos.remove(personaje)
            
        def get_enemigos(self):
            return self.enemigos
        

        def generarEnemigos(self, nombre: str, num: int):
        
            if nombre == 'Goblin':
                for i in range(num):
                    self.generarGoblin()
            
        
            elif nombre == 'Moblin':
                for i in range(num):
                    self.generarMoblin()
                
            elif nombre == 'Ogro':
                for i in range(num):
                    self.generarOgro()
                
        def generarGoblin(self):
            self.agregar_enemigo(Goblin(random.randint(5-2, 5+2), self))
            
        def generarMoblin(self):
            self.agregar_enemigo(Moblin(random.randint(10-3, 10+3), self))
        
        def generarOgro(self):
            self.agregar_enemigo(Ogro(random.randint(15-4, 15+4), self))   

        def __str__(self):
            acum = ''
            for i in self.enemigos:
                acum += i.__str__() + '\n'               
            return acum
 
def main():
    print("Sala")
    sala1 = Sala()
    sala2 = Sala()
    print(sala1.__str__())
    print(sala2.__str__())
    
if __name__ == '__main__':
    main()