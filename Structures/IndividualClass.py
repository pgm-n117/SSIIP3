import random
from copy import deepcopy

class Individual:
    #Constructor de un individuo, crea un individuo con muros aleatorios de tamaño de problema n
    def __init__(self, size):
        self.individual = [[random.randint(-1, 0) for _ in range(size)] for _ in range(size-2)]
    #Devuelve el array de muros del individuo
    def getIndividual(self):
        return self.individual


    def __deepcopy__(self, memo={}):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            setattr(result, k, deepcopy(v, memo))
        return result


    def __str__(self):
        n = self.individual.__len__()
        mazePreview = [[' ' for x in range(n+2)]for y in range(n)]

        print(str(1) + " ".join(map(str, [' ' for x in range(n+1)])) + str(2))

        for i in range(n):
            for j in range(n+2):
                if (self.individual[i][j] == -1):
                    mazePreview[i][j] = "x"
                #else: mazePreview[i][j] = " "

        for i in range(n):
            print(" ".join(map(str, mazePreview[i])))

        print(" ".join(map(str, ['_' for x in range(n+2)])))
