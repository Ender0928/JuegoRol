import Sala, Entidad, time
from Entidad import *
from Sala import *

class Juego:


    def generarEnemigos(self, nombre: str, num: int, sala: Sala):
        
        if nombre == 'Goblin':
            for i in range(num):
                self.generarGoblin(sala)
            
        
        elif nombre == 'Moblin':
            for i in range(num):
                self.generarMoblin(sala)
                
        elif nombre == 'Ogro':
            for i in range(num):
                self.generarOgro(sala)
                
    def generarGoblin(self, sala):
        goblin = Goblin(5, 'prueba', Sala())
    def generarMoblin(self, sala):
        pass
    def generarOgro(sala):
        pass
    
    def atacar(self, jugador: Entidad, target: str, sala: Sala):
        for enemigo in sala.enemigos:
            if enemigo.getVida() > 0:
                if(enemigo.getVelocidad() > jugador.getVelocidad()):
                    enemigo.atacar(jugador)
                    
                elif enemigo.getVelocidad() <= jugador.getVelocidad():
                    if target == enemigo.getNombre():
                        jugador.atacar(enemigo)
                        if enemigo.getVida() <= 0:
                            sala.enemigos.remove(enemigo)
                    enemigo.atacar(jugador)
                    
                  
    def action(self, jugador: Entidad, sala: Sala):
        rondaCombate = 1
        while jugador.vidaActual > 0 and sala.enemigos:
            print('Inicio de la ronda de combate ' + str(rondaCombate))
            print('Enemigos restantes:\n' + sala.__str__())
            print('Tu personaje:\n' + jugador.__str__() + '\n')
            print('Seleccione la acción que desea realizar:')
            print(' Atacar')
            print(' Objeto')
            if jugador.mejora:
                print(' Habilidad especial')
            
            print('\n')
                
            accion = input()

            #Acción que realiza al atacar
            if accion == 'Atacar':
                print('Seleccione el objetivo de su ataque:')
                target = input()
                self.atacar(jugador, target, sala) 
            
            #Acción que realiza al usar un objeto    
            elif accion == 'Objeto':
                if jugador.mochila:
                    print('Seleccione el objeto que desea utilizar:\n')
                    jugador.mochila.__str__()
                    objeto = input()
                    objeto.usar(jugador)
                else:
                    print('No tiene una mochila equipada ahora mismo')
                
                rondaCombate -= 1
                    
            rondaCombate += 1
            
        #Comprueba si el jugador ha muerto     
        if(jugador.vidaActual <= 0):
            print('Has muerto')
            exit()
   
    def obtenerRecompensa(self, jugador: Humano, sala: Sala):
        jugador.getMochila().agregarObjeto(sala.recompensa)       
    
    
def main():
    juego = Juego()
    print('Bienvenido a la mazmorra')
    #Hacer espera de 2 segundos
    time.sleep(2)
    print('Encarnarás a un aventurero que deberá superar las pruebas de la mazmorra')
    time.sleep(2)
    nombre = input('Introduce el nombre de tu personaje: ')
    sala = Sala()
    jugador = Humano(10, nombre, sala)
    enemigo1 = Goblin(5, 'prueba', sala)
    enemigo2 = Goblin(5, 'prueba2', sala)
    sala.agregar_enemigo(enemigo1, enemigo2)
    time.sleep(2)
    print('Han aparecido ' + str(sala.enemigos.__len__()) + ' enemigos')
    time.sleep(2)
    print('Inicio del combate')
    juego.action(jugador, sala)
    print('Has superado la primera sala')
    juego.obtenerRecompensa(jugador, sala)
    
if __name__ == '__main__':
    main()