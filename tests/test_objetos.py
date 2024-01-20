from Objeto import *

def main():
    
    armadura = Armadura(10)
    print(armadura.__str__())
    
    arma = Arma(10, 10)
    print(arma.__str__())
    
    espada = Espada(10, 10)
    print(espada.__str__())
    
    hacha = Hacha(10, 10)
    print(hacha.__str__())
    
    lanza = Lanza(10, 10)
    print(lanza.__str__())
    
if __name__ == '__main__':
    main()