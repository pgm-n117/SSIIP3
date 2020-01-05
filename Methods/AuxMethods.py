from Structures.IndividualClass import Individual
from AStar.AStarFitness import fitness
from copy import deepcopy
import random
import math

'''HILL CLIMBING'''
#Generación de vecinos para Hill Climbing
def generateNeighbourhood(n, individual: Individual, refFitness):

    Neighbourhood = list()
    eval = (-math.inf, -math.inf)
    index = None

    for i in range(len(individual.getIndividual())):
        for j in range(len(individual.getIndividual()[i])):


            #deepcopy para evitar cambiar las referencias al original
            auxInd = deepcopy(individual)                       #Copiamos el original
            auxValue = abs(individual.getIndividual()[i][j])-1  #Cambiamos el valor que genera un vecino
            auxInd.individual[i][j] = auxValue                  #Guadamos el cambio en el vecino

            #Añadimos el vecino
            Neighbourhood.append(auxInd)                        #Añadimos el vecino a la lista

            #Conforme calculamos los vecinos, los vamos evaluando
            auxeval = None
            auxeval = fitness(n, auxInd.getIndividual())        #Evaluamos el vecino

            ''' SE PUEDE COMENTAR PARA QUITAR ESTA CONDICION'''
            #Si el individuo generado tiene mejor coste que refFitness, lo devolvemos, no seguimos
            if auxeval[1] > refFitness[1]:
                eval = auxeval
                index = (i*n)+j #para calcular el indice del mejor individuo
                return (Neighbourhood, index, eval)

            ''''''

            if auxeval[1] > eval[1]:
                eval = auxeval
                index = (i*n)+j #para calcular el indice del mejor individuo
            elif auxeval[1] == eval[1] and auxeval[0] > auxeval[0]:
                eval = auxeval
                index = (i*n)+j


    #Si ninguna configuración tiene solución, como eval es -inf, se devolverá la primera encontrada,
    # y se buscará otra configuración en le algoritmo alterando el individuo evaluado
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


'''GENETIC'''
#Generación de una población aleatoria
def generatePopulation(n, popSize):
    '''
    n           tamaño de problema
    popSize     tamaño de la población
    '''

    population = list()
    for i in range(popSize):
        population.append(Individual(n, None))

    return population

def evaluatePopulation(n, population):

    '''
    n           tamaño de problema
    population  población a evaluar
    '''

    popEval = list()

    for i in range(len(population)):
        auxEval = fitness(n, population[i].getIndividual())

        popEval.append(auxEval)
    '''
    popEval es la evaluación de cada individuo
    '''

    return popEval

#Selección de individuos por torneo
def tournamentSelection(popEval, members):

    '''
    popEval     Lista con cada evaluación de cada individuo (n.Exp, Coste)
    members     Número se miembros participantes en el torneo

    Como el unico dato necesario para conocer los miembros de la población es su indice, y está
    implicito en el índice de cada evaluación, no necesitamos pasar la población entera,
    solo la lista de evaluaciones.
    '''

    bestIndividual = -math.inf
    bestIndex = -math.inf

    for i in range(members):
        auxIndex = random.randint(0, len(popEval)-1)
        if(popEval[auxIndex][1] > bestIndividual):
            bestIndividual = popEval[auxIndex][1]
            bestIndex = auxIndex

    return bestIndex
def crossover(cruce, parent1: Individual, parent2: Individual):
    if cruce == 'uniforme':
        return crossover1(parent1, parent2)
    elif cruce == '1px':
        return crossover2(parent1, parent2)
    elif cruce == '2px':
        return crossover3(parent1, parent2)

#Cruce por dos puntos
def crossover3(parent1: Individual, parent2: Individual):
    #Creamos los dos individuos Hijo
    c1 = [[int for _ in range(len(parent1.getIndividual()[0]))] for _ in range(len(parent1.getIndividual()))]
    c2 = [[int for _ in range(len(parent1.getIndividual()[0]))] for _ in range(len(parent1.getIndividual()))]

    #Tamaño de un individuo
    indSize = len(parent1.getIndividual())*len(parent1.getIndividual()[0])

    #Obtener los puntos de cruce
    crossoverPoints = list()
    crossoverPoints.append(random.randint(0, indSize-1))
    x=None
    while(x == crossoverPoints[0] or x == None):
        x = random.randint(0, indSize-1)
    crossoverPoints.append(x)
    crossoverPoints.sort()

    #Cruce
    for i in range(len(parent1.getIndividual())):
        for j in range(len(parent1.getIndividual()[0])):
            if(i * len(parent1.getIndividual()[0]) + j >= crossoverPoints[0]):
                if(i * len(parent1.getIndividual()[0]) + j<= crossoverPoints[1]):
                    c1[i][j] = parent2.getIndividual()[i][j]
                    c2[i][j] = parent1.getIndividual()[i][j]
                else:
                    c1[i][j] = parent1.getIndividual()[i][j]
                    c2[i][j] = parent2.getIndividual()[i][j]
            else:
                c1[i][j] = parent1.getIndividual()[i][j]
                c2[i][j] = parent2.getIndividual()[i][j]

    c1 = Individual(None, c1)
    c2 = Individual(None, c2)

    return c1, c2

#Cruce por un punto
def crossover2(parent1: Individual, parent2: Individual):
    # Creamos los dos individuos Hijo
    c1 = [[int for _ in range(len(parent1.getIndividual()[0]))] for _ in range(len(parent1.getIndividual()))]
    c2 = [[int for _ in range(len(parent1.getIndividual()[0]))] for _ in range(len(parent1.getIndividual()))]

    #Tamaño del individuo
    indSize = len(parent1.getIndividual())*len(parent1.getIndividual()[0])

    #Obtener punto de cruce

    crossoverPoint = random.randint(0, indSize-1)

    # Cruce
    for i in range(len(parent1.getIndividual())):
        for j in range(len(parent1.getIndividual()[0])):
            if (i * len(parent1.getIndividual()[0]) + j > crossoverPoint):
                c1[i][j] = parent2.getIndividual()[i][j]
                c2[i][j] = parent1.getIndividual()[i][j]
            else:
                c1[i][j] = parent1.getIndividual()[i][j]
                c2[i][j] = parent2.getIndividual()[i][j]

    c1 = Individual(None, c1)
    c2 = Individual(None, c2)

    return c1, c2

#Cruce uniforme: con una máscara
def crossover1(parent1: Individual, parent2: Individual):
    # Creamos los dos individuos Hijo
    c1 = [[int for _ in range(len(parent1.getIndividual()[0]))] for _ in range(len(parent1.getIndividual()))]
    c2 = [[int for _ in range(len(parent1.getIndividual()[0]))] for _ in range(len(parent1.getIndividual()))]

    #Tamaño del individuo
    indSize = len(parent1.getIndividual())*len(parent1.getIndividual()[0])

    #Máscara:
    mask = [[random.randint(0,1) for _ in range(indSize)] for _ in range(indSize-2)]

    # Cruce
    for i in range(len(parent1.getIndividual())):
        for j in range(len(parent1.getIndividual()[0])):
            if (mask[i][j]):
                c1[i][j] = parent2.getIndividual()[i][j]
                c2[i][j] = parent1.getIndividual()[i][j]
            else:
                c1[i][j] = parent1.getIndividual()[i][j]
                c2[i][j] = parent2.getIndividual()[i][j]

    c1 = Individual(None, c1)
    c2 = Individual(None, c2)

    return c1, c2
