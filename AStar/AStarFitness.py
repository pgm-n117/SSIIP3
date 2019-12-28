from time import time

from AStar.AEstrella import *
from AStar.Estructuras.Solucion import *
from Structures.Individual import *

def fitness (n, walls):
    solucion = Solucion(None, None, None, None, None, None, None)
    solucion = AEstrella(n, 2, walls)

    #En vez de imprimir la solución, devolvemos solo los datos que necesitemos, en este caso el tiempo de ejecución.
    #solucion.printSolucion()
    return solucion.






