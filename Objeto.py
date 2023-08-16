import TipoArma, Stats

class Objeto:
    
    def __init__(self, nombre: str, descripcion: str):
        self.nombre = nombre
        self.descripcion = descripcion
        
    def getNombre(self):
        return self.nombre
    
    def __str__(self):
        return self.nombre
        
class Mochila(Objeto):
    
    def __init__(self):
        super().__init__('Mochila', 'Sirve para guardar los objetos que encuentres en la aventura')
        self.capacidad = 10
        self.contenido = []
        
    def agregarObjeto(self, objeto: Objeto):
        
        if len(self.contenido) < self.capacidad:
            print('Has obtenido como recompensa: ' + objeto.getNombre() + '\n')
            self.contenido.append(objeto)

        else:
            print('¿Desea tirar el objeto o cambiarlo por otro?')
            print(' 1. Tirar')
            print(' 2. Cambiar\n')
            opcion = int(input('Ingrese una opcion: '))
            if opcion == 1:
                print('Objeto tirado')
                
            elif opcion == 2:
                print('Seleccione el objeto que desea cambiar')
                print (self.contenido)
                objetoTirado = input()
                self.contenido.remove(objetoTirado)
                self.contenido.append(objeto)

            else: 
                print('Error')
                self.agregarObjeto(objeto)
                
    def eliminarObjeto(self, objeto: Objeto):
        self.contenido.remove(objeto)
        
    def __str__(self):
        acum = ''
        for i in self.contenido:
            acum += i.__str__() + '\n'
        print(acum)
      
class Arma(Objeto):
    
    def __init__(self, ataque: int, velocidad: int):
        super().__init__('Arma', 'Objeto para atacar')
        self.ataque = ataque
        #self.requerimiento = requerimiento
        self.velocidad = velocidad
        #self.tipoArma = tipoArma
        
    def __str__(self):
        return self.nombre + " (Ataque: " + str(self.ataque) #+ " - Velocidad: " + str(self.velocidad) + ")"
    
    def getAtaque(self):
        return self.ataque #+ self.tipoArma.getAtaque()
    
    def getVelocidad(self):
        return self.velocidad #+ self.tipoArma.getVelocidad()
    
    def getRequerimiento(self):
        return self.requerimiento
    
    def getDescripcion(self):
        return self.descripcion
    
class PocionVida(Objeto):
    def __init__(self):
        super().__init__('Pocion Vida', 'Recupera 10 puntos de vida')
        
    def usar(self, jugador):
        jugador.recuperarVida(10)
        
class PocionPE(Objeto):
    def __init__(self):
        super().__init__('Pocion PE', 'Recupera 30 puntos de PE')
        
    def usar(self, jugador):
        jugador.recuperarPE(30)

class Espada(Arma):
    def __init__(self, attack: int, velocidad: int):
        super().__init__(attack, velocidad)#'Espada', 'Arma de filo', 5, Stats.Stats(0, 0, 0, 0, 0, 0, 0), 0, TipoArma.TipoArma.ESPADA)
    
class Hacha(Arma):
    def __init__(self, attack: int, velocidad: int):
        super().__init__(attack, velocidad)
        
class Lanza(Arma):
    def __init__(self, attack: int, velocidad: int):
        super().__init__(attack, velocidad)
        
