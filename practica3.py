from argparse import ArgumentParser
from time import time

if __name__ == "__main__":

    # ArgumentParser con una descripción de la aplicación
    parser = ArgumentParser(description='%(prog)s es una implementación metaheurísticas, Búsqueda local (Hill Climbing) y algoritmo genético. ' )
    # Argumento posicional con descripción
    parser.add_argument('n', type=int, help='tamaño del problema')
    parser.add_argument('seed', type=int, help='semilla para funcion random')

    parser.add_argument('algoritmo', choices=['hillclimbing', 'geneticalgorithm'],
                        help='Algoritmo con el que se abordará el ejercicio')

    parser.add_argument('--it', type=int, help='Número de iteraciones para Hill Climbing')
    parser.add_argument('--cruce', choices=['uniforme', '1px', '2px'],
                        help='Cruce para algoritmo genético')
    parser.add_argument('--pS', type=int, help='Polulation Size: Tamaño de la población para Algoritmo Genético')
    parser.add_argument('--gen', type=int, help='Generaciones para Algoritmo Genético')
    parser.add_argument('--probC', type=float, help='Probabilidad de cruce para Algoritmo Genético')
    parser.add_argument('--probM', type=float, help='Probabilidad de mutación para Algoritmo Genético')
    parser.add_argument('--members', type=int, help='Miembros del torneo para Algoritmo Genético')

    args = parser.parse_args()

    print(args)

    # Para medir el tiempo de ejecución
    global tiempoInicio
    tiempoInicio = time()

    if (args.algoritmo == 'hillclimbing'):
        from Algorithms.HillClimbing import *

        solucion = HillClimbing(args.n, args.seed, args.it)
    elif (args.algoritmo == 'geneticalgorithm'):
        from Algorithms.GeneticAlgorithm import *

#        solucion = geneticAlgorithm(args.n, args.seed. args.pS, args.gen, args.probC, args.probM, args.members, args.cruce)
        solucion = geneticAlgorithm(args.n, args.seed, args.pS, args.gen, args.probC, args.probM, args.members, args.cruce )

    tiempoFin = str(time() - tiempoInicio)

    print("Tiempo de ejecución: " + tiempoFin)