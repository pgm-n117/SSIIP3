from time import time

from AStar.AEstrella import *
from AStar.Estructuras.Solucion import *
from Structures.IndividualClass import *

def fitness (n, walls):
    solucion = Solucion(None, None, None, None, None, None, None, 0.0)
    solucion = AEstrella(n, 2, walls)

    #En vez de imprimir la solución, devolvemos solo los datos que necesitemos, en este caso el tiempo de ejecución.
    #solucion.printSolucion()
    if solucion.secuenciaAcc is not None:
        #solucion.printSolucion()
        return solucion.nExpan, solucion.coste
    else:
        #print("No hay solución")
        return (-1, -1)





