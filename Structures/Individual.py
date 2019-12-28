import sys, random
class Individual:
    #Representación del individuo
    individual = []

    #Constructor de un individuo, crea un individuo con muros aleatorios de tamaño de problema n
    def __init__(self, size):
        self.individual = [[random.randint(-1, 0) for _ in range(size)] for _ in range(size-2)]
    #Devuelve el array de muros del individuo
    def getIndividual(self):
        return self.individual


