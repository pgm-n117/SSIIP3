from Structures.IndividualClass import *
from AStar.AStarFitness import *

def geneticAlgorithm(n, seed):

    random.seed(seed)
    #i = Individual(n)

    p = list()
    for i in range(100): #100 individuos
        p.append(Individual(n))

    fitness(n, p[45].getIndividual())


    return None