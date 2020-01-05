from enum import Enum

#Acciones posibles del problema
#Una accion se define por un coche, y la direccion que toma
#Orden de la acciones originario

class Dir(Enum):
    abajo=0
    izquierda=1
    derecha=2
    arriba=3

    def __str__(self):
        return str(self.name)


dir=[(0,1),(-1,0),(1,0),(0,-1)]
'''
#Orden de las acciones diferente: Para testear

class Dir(Enum):
    arriba=0
    abajo=1
    derecha=2
    izquierda=3

    def __str__(self):
        return str(self.name)


dir=[(0,-1),(0,1),(1,0),(-1,0)]
'''

class Accion:
    def __init__(self, coche, direccion):
        self.coche=coche
        self.direccion=direccion

    def __str__(self):
        return str("Coche: " + str(self.coche + 1) + " Dirección: " + str(Dir(dir.index(self.direccion))))
