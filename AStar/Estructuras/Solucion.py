from ..Estructuras.Nodo import *

class Solucion:

    def __init__(self, secuenciaAcc, coste, nCreados, nExpan, nExpl, maxAbiertos, maxNodos, tEjec):
        self.secuenciaAcc = secuenciaAcc        #Nodos de la secuencia de acciones de la solución
        self.coste = coste                      #Coste de la solución
        self.nCreados = nCreados                #Nodos generados
        self.nExpan = nExpan                    #Nodos expandidos
        self.nExpl = nExpl                      #Nodos explorados
        self.maxAbiertos = maxAbiertos          #Máximo número de nodos en lista de abiertos/elegibles
        self.maxNodos = maxNodos                #Máximo número de nodos en memoria
        self.tEjec = tEjec

    def printSolucion(self):

        if self.secuenciaAcc == None:
            print("No hay solución")
            return

        for nod in self.secuenciaAcc:
            if isinstance(nod, Nodo):
                print(nod.accion)

        print("Coste de la solución: " + str(self.coste))
        print("Nodos Generados: " + str(self.nCreados))
        print("Nodos Expandidos: " + str(self.nExpan))
        print("Nodos Explorados: " + str(self.nExpl))
        print("Máximo número de nodos abiertos " + str(self.maxAbiertos))
        print("Máximo número de nodos en memoria " + str(self.maxNodos))
        print("Tiempo de ejecución: " + str(self.tEjec))

        return