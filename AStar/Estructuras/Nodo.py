#Atributos de un nodo cualquiera
from filecmp import cmp


class Nodo:
    def __init__(self, padre, accion, coste, heur, eval, estado):
        self.padre = padre      # Nodo superior
        self.accion = accion    # Acción realizada para llegar a este nodo
        self.coste = coste      # Coste de realizar la acción para llegar al nodo (en este problema, 1)
        self.heur = heur        # Valor de la heuristica: Coste estimado para llegar desde este nodo a la solución
        self.eval = eval        # Coste Total del nodo + Heurística: f(n) = g(n) + h(n)
        self.estado = estado    # Lista de tuplas que contiene la posiciones de los coches en el Maze



    def __gt__(self, nodo):     #Comparacion greater than, utilizada para insercion por biseccion y heap en AEstrella
        if isinstance(nodo, self.__class__):
            return self.eval > nodo.eval
    '''
    def __ge__(self, nodo):     #Comparacion greater or equal than
        if isinstance(nodo, self.__class__):
            return self.eval >= nodo.eval
    '''
    def __eq__(self, nodo):     #Comparacion equals
        if isinstance(nodo, self.__class__):
            if(self.heur==None):                     #Si no trabajamos con heuristicas esta busqueda mejor
                for coche in self.estado:
                    if(not(coche in nodo.estado)):
                        return False
                return True
            else:
                return (self.estado == nodo.estado)     #para AEstrella o PrimeroMejor mejor esta
        else:
            return False


    def __ne__(self, nodo):
        return not self.__eq__(nodo)

    def __str__(self):
        return str("Estado: "+ self.estado + ", Coste: "+self.coste)
