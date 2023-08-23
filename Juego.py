import Sala, Entidad, time, Dado
from Entidad import *
from Sala import *

class Juego:

    
    def atacar(self, jugador: Entidad, target: str, sala: Sala):
        for enemigo in sala.enemigos:
            if enemigo.getVida() > 0:                   
                if enemigo.getVelocidad() <= jugador.getVelocidad():
                    if target == enemigo.getNombre():
                        jugador.atacar(enemigo)
                        if enemigo.getVida() <= 0:
                            jugador.ganarExp(enemigo.getExp())
                            sala.eliminar_enemigo(enemigo)
                if enemigo.getVida() > 0:
                    enemigo.atacar(jugador)
                    
                  
    def action(self, jugador: Entidad, sala: Sala):
        rondaCombate = 1
        sala.sortEnemigos()
        while jugador.vidaActual > 0 and sala.enemigos:
            print('Inicio de la ronda de combate ' + str(rondaCombate))
            print('Enemigos restantes:\n\n' + sala.__str__())
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
                    jugador.consultar_mochila()
                    objeto = input()
                    for i in jugador.mochila.contenido:
                        if objeto == i.getNombre():
                            i.usar(jugador)
                            jugador.mochila.eliminarObjeto(i)
                            break
                        else :
                            print('No tienes ese objeto en tu mochila')
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

    def tirarDados(caras: int, numeroDados: int):
        acumulador = 0
        for i in range(numeroDados):
            dado = Dado(caras)
            acumualdor += dado.rolar()
        return acumulador
        
def main():
    juego = Juego()
    print('Bienvenido a la mazmorra')
    time.sleep(2)
    print('Encarnarás a un aventurero que deberá superar las pruebas de la mazmorra')
    time.sleep(2)
    nombre = input('Introduce el nombre de tu personaje: ')
    sala = Sala()
    jugador = Humano(10, nombre, sala)
    
    while jugador.getNivel() < 10 and jugador.vidaActual > 0:
        #elegir si quieres realizar una accion antes o continuar(equipar objeto)
        #print('Antes de continuar a la siguiente sala, ¿desea realizar alguna acción?')
        #print(' 1:Equipar objeto \n 2:Continuar')
        sala.generarEnemigos('Goblin', random.randint(1, 2)) 
        if(jugador.getNivel() >= 2):
            sala.generarEnemigos('Goblin', random.randint(1, 2))
        if(jugador.getNivel() >= 4):
            sala.generarEnemigos('Moblin', random.randint(1, 2))
        if(jugador.getNivel() >= 6):
            sala.generarEnemigos('Ogro', random.randint(1, 2))
        time.sleep(2)
        print('Han aparecido ' + str(sala.enemigos.__len__()) + ' enemigos')
        time.sleep(2)
        print('Inicio del combate')
        juego.action(jugador, sala)
        print('Has superado la sala ' + str(sala.getNumero()))
        juego.obtenerRecompensa(jugador, sala)
        
        sala = Sala()
    
if __name__ == '__main__':
    main()