from Structures.IndividualClass import Individual
from AStar.AStarFitness import *
from Methods.AuxMethods import *

def HillClimbing(n, seed, it):

    '''
    n:     tamaño del problema
    seed:  semilla aleatoria
    it:     número de iteraciones
    '''

    random.seed(seed)

    #El mejor individuo encontrado
    bestIndividual = None
    bestFitness = 0

    #Inicializamos otras variables necesarias
    iteration = 0
    bestNeighbIndex = 0
    actualFitness = 0

    #Generamos una configuración aleatoria de muros
    actualIndividual = Individual(n)
    actualFitness = fitness(n, actualIndividual.getIndividual())
    print("Individuo inicial: ")
    actualIndividual.__str__()

    #Iteramos
    while iteration < it:

        #Introducimos no determinismo, generando individuos aleatorios con probabilidad 0.x (variable)
        if(random.random() < 0.4):
            print("Aleatorio")

            bestNeighb = Individual(n)
            randomNeighbFit = fitness(n, bestNeighb.getIndividual())
            newFitness = randomNeighbFit

        else:
            #Generamos los vecinos (solo hasta que encontremos el mejor,
            # o todos si no hay ninguno mejor que el actual)
            result = generateNeighbourhood(n, actualIndividual, actualFitness)
            neighbourhood = result[0]       #Vecinos
            bestNeighbIndex = result[1]     #El mejor encontrado
            bestNeighb = neighbourhood[bestNeighbIndex]
            newFitness = result[2]          #Fitness del mejor encontrado

            #Si no obtenemos solución de los vecinos, alteramos el actual
            if bestNeighbIndex == None:
                print("Sin solucion en el vecindario")
                actualIndividual = mutation(n, actualIndividual)



        print("IT: " + iteration.__str__() + " Fitness actual: " + actualFitness.__str__() + ", Fitness del nuevo vecino: " + newFitness.__str__())

        iteration+=1

        if(newFitness > actualFitness):
            actualIndividual = bestNeighb
            actualFitness = newFitness      #De esta manera no tenemos que reevaluar el fitness del actual, solamente si lo alteramos abajo


        elif(newFitness != -1):     #APLICAMOS ILS, PERO SIN TENER EN CUENTA INDIVIDUOS SIN SOLUCIÓN ALEATORIOS
            print("Alteración individuo")   #Alteramos el mejor individuo en vez de el actual
            actualIndividual = mutation(n, bestIndividual)
            actualFitness = fitness(n, actualIndividual.getIndividual())

        #Actualizamos el mejor individuo hasta ahora
        if (actualFitness > bestFitness):
            bestFitness = actualFitness
            bestIndividual = actualIndividual


    print("Mejor Individuo: ")
    bestIndividual.__str__()
    print("Coste: " + bestFitness.__str__())
    return bestIndividual.getIndividual()
