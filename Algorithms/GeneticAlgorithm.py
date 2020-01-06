from Structures.IndividualClass import *
from AStar.AStarFitness import *
from Methods.AuxMethods import *



def geneticAlgorithm(n: int, seed: int, pSize: int, generations: int, probC: float, probM: float, members: int, cruce: str):


    '''
    n:              tamaño del problema
    seed:           semilla aleatoria
    pSize:          tamaño de la población
    generations:    número de generaciones
    probC:          probabilidad de cruce
    probM:          probabilidad de mutación
    members:        miembros del torneo
    cruce:          tipo de cruce
    '''

    random.seed(seed)

    #El mejor individuo encontrado
    bestIndividual = None
    bestFitness = 0

    #Inicializamos otras variables necesarias
    gen = 0

    #Población inicial aleatoria
    actualPopulation = generatePopulation(n, pSize)
    evaluation = evaluatePopulation(n, actualPopulation)
    actualPopEval = evaluation   #Evaluación de cada individuo de la población



    #Iteramos
    while gen < generations:
        # Variables para las nuevas poblaciones generadas
        newPopulation = list()
        newPopEval = None

        #Variable auxiliar pasa saber donde empezar a añadir nuevos individuos
        initialPos = 1


        print("Generación " + gen.__str__())
        #Seleccionar los mejores individuos que pasarán a la generación siguiente
        #TournamentSelection devuelve el índice del individuo seleccionado
        #Si el tamaño de población es par, seleccionamos dos individuos para facilitar el cruce?
        newPopulation.append(actualPopulation[tournamentSelection(actualPopEval, members)])
        if pSize % 2 == 0:
            newPopulation.append(actualPopulation[tournamentSelection(actualPopEval, members)])
            initialPos += 1

        #Cruce para generar la nueva población (los restantes de los seleccionados)

        for i in range(initialPos, pSize, 2):
            if(random.random() < probC):
                newIndividuals = crossover(cruce, actualPopulation[i], actualPopulation[i+1])
                newPopulation.append(newIndividuals[0])
                newPopulation.append(newIndividuals[1])
            else:
                newPopulation.append(actualPopulation[i])
                newPopulation.append(actualPopulation[i+1])
            i+=1


        #Mutación de la nueva generación (probabilidad baja, por ejemplo 0.1)
        #Los mejores individuos elegios (están los primeros) no se mutan, porque pasan directos a la siguiente gen.

        for i in range(initialPos, pSize):
            if(random.random() < probM):
                newPopulation[i] = mutation(n, newPopulation[i])

        #Evaluar la nueva población
        evaluation = evaluatePopulation(n, newPopulation)
        newPopEval = evaluation

        #Sustitución por elitismo
        #Obtenemos el mejor individuo de la población actual
        best = (-math.inf, -math.inf)
        bestIndex = None
        for i in range(len(actualPopEval)):
            if actualPopEval[i][1] > best[1]:
                best = actualPopEval[i]
                bestIndex = i
            elif(actualPopEval[i][1] == best[1] and actualPopEval[i][0] > best[0]):
                best = actualPopEval[i]
                bestIndex = i

        #Obtenemos el peor individuo de la nueva población

        worst = math.inf
        worstIndex = None
        for i in range(len(newPopEval)):
            if(newPopEval[i][1] < worst):
                worst = newPopEval[i][1]
                worstIndex = i

        newPopulation[worstIndex] = actualPopulation[bestIndex]
        newPopEval[worstIndex] = actualPopEval[bestIndex]

        #Sustitución
        actualPopulation = newPopulation
        actualPopEval = newPopEval

        print("Mejor individuo de la generación " + gen.__str__())
        actualPopulation[worstIndex].__str__() #WrstIndex porque es el mejor que hemos sustituido
        print("Nodos Expandidos: " + actualPopEval[worstIndex].__str__())

        gen += 1

    #Obtener el mejor individuo de la ultima generación
        best = -math.inf
        bestIndex = None
        for i in range(len(actualPopEval)):
            if actualPopEval[i][1] > best:
                best = actualPopEval[i][1]
                bestIndex = i

    bestIndividual = actualPopulation[bestIndex]
    bestFitness = actualPopEval[bestIndex]

    print("Mejor Individuo: ")
    bestIndividual.__str__()
    print("Coste: " + bestFitness.__str__())
    return bestFitness
