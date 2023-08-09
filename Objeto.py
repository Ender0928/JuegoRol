import TipoArma, Stats

class Objeto:
    
    def __init__(self, nombre: str, descripcion: str):
        self.nombre = nombre
        self.descripcion = descripcion
        
class Mochila(Objeto):
    
    def __init__(self, nombre: str):
        super().__init__(nombre, 'Sirve para guardar los objetos que encuentres en la aventura')
        self.capacidad = 10
        self.contenido = []
        
    def agregarObjeto(self, objeto: Objeto):
        
        if len(self.contenido) < self.capacidad:
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
        
        
class Arma(Objeto):
    
    def __init__(self, nombre: str, descripcion: str, ataque: int, requerimiento: Stats, velocidad: int, tipoArma: TipoArma):
        super().__init__(nombre, descripcion)
        self.ataque = ataque
        self.requerimiento = requerimiento
        self.velocidad = velocidad
        self.tipoArma = tipoArma
        
    def __str__(self):
        return self.nombre + " (Ataque: " + str(self.ataque) + " - Velocidad: " + str(self.velocidad) + ")"
    
    def getAtaque(self):
        return self.ataque + self.tipoArma.getAtaque()
    
    def getVelocidad(self):
        return self.velocidad + self.tipoArma.getVelocidad()
    
    def getRequerimiento(self):
        return self.requerimiento
    
    def getDescripcion(self):
        return self.descripcion