from Structures.IndividualClass import Individual
from AStar.AStarFitness import fitness
from copy import deepcopy
import random
import math

#Generación de vecinos para Hill Climbing
def generateNeighbourhood(n, individual: Individual, refFitness):

    Neighbourhood = list()
    eval = -math.inf
    index = None

    for i in range(len(individual.getIndividual())):
        for j in range(len(individual.getIndividual()[i])):


            #deepcopy para evitar cambiar las referencias al original
            auxInd = deepcopy(individual)
            auxValue = abs(individual.getIndividual()[i][j])-1
            auxInd.individual[i][j] = auxValue

            #Añadimos el vecino
            Neighbourhood.append(auxInd)

            #Conforme calculamos los vecinos, los vamos evaluando
            auxeval = 0
            auxeval = fitness(n, auxInd.getIndividual())

            ''' SE PUEDE COMENTAR PARA QUITAR ESTA CONDICION'''
            #Si el individuo generado tiene mejor fitness que refFitness, lo devolvemos, no seguimos
            if auxeval > refFitness:
                eval = auxeval
                index = (i*n)+j #para calcular el indice del mejor individuo
                return (Neighbourhood, index, eval)
            ''''''

            if auxeval > eval:
                eval = auxeval
                index = (i*n)+j #para calcular el indice del mejor individuo


    #Si ninguna configuración tiene solución, como eval es -inf, se devolverá la primera encontrada,
    # y se buscará otra configuración en le algoritmo aletrando el individuo evaluado
    return (Neighbourhood, index, eval)



#Mutación valida para Hill Climbing y Genético
def mutation(n, individual : Individual):
    randx = random.randint(0, n - 3)
    randy = random.randint(0, n - 1)

    # deepcopy para evitar cambiar las referencias al original
    auxInd = deepcopy(individual)
    auxValue = abs(individual.getIndividual()[randx][randy]) - 1
    auxInd.individual[randx][randy] = auxValue

    return auxInd


#Obtencion del mejor vecino
def getBestNeighbour(n, Neighbourhood: list):

    eval = 0
    index = None
    for i in range(len(Neighbourhood)):
        auxeval = 0
        auxeval = fitness(n, Neighbourhood[i].getIndividual())


    #Si no obtenemos solución de ninguno de los vecinos, devolvemos None
    if eval == 0:
        return None
    else:
        print("Best of population: " + index.__str__() + ", " + eval.__str__())
        return index


