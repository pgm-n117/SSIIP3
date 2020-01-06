from time import time
import os
import random
from Algorithms import GeneticAlgorithm, HillClimbing

tiempoInicio = None
tiempoFin = None

Npruebas = 25 #numero de pruebas que se haran para cada caso

problemSizes = [5, 10, 15, 20]

seeds = []
random.seed(2019)
for i in range(len(problemSizes)):
    seeds.append([])
    for n in range(Npruebas):
        seeds[i].append(random.random())

'''
Formato del fichero csv para Iteracion de valores:
Tamaño del laberinto, Iteraciones necesarias, Utilidad de la política encontrada, Tiempo de aprendizaje, Tiempo de ejec.
'''

if(not(os.path.exists("./Datos"))):
    os.mkdir('./Datos', 0o777)

'''
Pruebas variando el tamaño y manteniendo el resto de valores 
'''
if(not(os.path.exists("./Datos/Genericas"))):
    os.mkdir('./Datos/Genericas', 0o777)



cabecera = "Tamaño de problema, Nodos Expandidos, Coste\n"

#Hill Climbing [100 iteraciones por ejecución]
fd = open("./Datos/Genericas/HillClimbingGenerics5-10-15-20 100it.csv", "w")
fd.writelines(cabecera)
solucion = None
for i in range(len(problemSizes)):
    for n in range(Npruebas):
        tiempoInicio = time()
        solucion = HillClimbing.HillClimbing(problemSizes[i], seeds[i][n], 100)
        tiempoFin = time() - tiempoInicio
        fd.writelines(problemSizes[i].__str__() + "," + str(solucion[0]) + "," + str(solucion[1]) + "\n")

fd.close()
#Genetic Algorithm genérico: [Cruce Uniforme, Tamaño de población: 100, Generaciones: 100, Prob Cruce: 0.9, Prob Mutación: 0.1, Miembros Torneo: 10]
fd = open("./Datos/Genericas/GeneticGenerics5-10-15-20 100gen 09 01 Uniforme.csv", "w")
fd.writelines(cabecera)
solucion = None
for i in range(len(problemSizes)):
    for n in range(Npruebas):
        tiempoInicio = time()
        solucion = GeneticAlgorithm.geneticAlgorithm(problemSizes[i], seeds[i][n], 100, 100, 0.9, 0.1, 10, 'uniforme')
        tiempoFin = time() - tiempoInicio
        fd.writelines(problemSizes[i].__str__() + "," + str(solucion[0]) + "," + str(solucion[1]) + "\n")
fd.close()



if(not(os.path.exists("./Datos/ComparacionCruces"))):
    os.mkdir('./Datos/ComparacionCruces', 0o777)

#Genetic Algorithm genérico: [Cruce uniforme, Tamaño de problema: 10]
fd = open("./Datos/ComparacionCruces/GeneticUniforme10 100gen 09 01.csv", "w")
fd.writelines(cabecera)
solucion = None

for n in range(Npruebas):
    tiempoInicio = time()
    solucion = GeneticAlgorithm.geneticAlgorithm(10, seeds[i][n], 100, 100, 0.9, 0.1, 10, 'uniforme')
    tiempoFin = time() - tiempoInicio
    fd.writelines(problemSizes[i].__str__() + "," + str(solucion[0]) + "," + str(solucion[1]) + "\n")
fd.close()

#Genetic Algorithm genérico: [Cruce por 1 punto, Tamaño de problema: 10]
fd = open("./Datos/ComparacionCruces/Genetic1px10 100gen 09 01.csv", "w")
fd.writelines(cabecera)
solucion = None
for n in range(Npruebas):
    tiempoInicio = time()
    solucion = GeneticAlgorithm.geneticAlgorithm(10, seeds[i][n], 100, 100, 0.9, 0.1, 10, '1px')
    tiempoFin = time() - tiempoInicio
    fd.writelines(problemSizes[i].__str__() + "," + str(solucion[0]) + "," + str(solucion[1]) + "\n")
fd.close()

#Genetic Algorithm genérico: [Cruce por 2 puntos, Tamaño de problema: 10]
fd = open("./Datos/ComparacionCruces/Genetic2px10 100gen 09 01.csv", "w")
fd.writelines(cabecera)
solucion = None
for n in range(Npruebas):
    tiempoInicio = time()
    solucion = GeneticAlgorithm.geneticAlgorithm(10, seeds[i][n], 100, 100, 0.9, 0.1, 10, '2px')
    tiempoFin = time() - tiempoInicio
    fd.writelines(problemSizes[i].__str__() + "," + str(solucion[0]) + "," + str(solucion[1]) + "\n")
fd.close()


#Prueba Variando el tamaño de torneo el número de miembros del torneo
#Genetic Algorithm genérico: [Cruce uniforme, Tamaño de problema: 10, tamaño de torneo 20]
fd = open("./Datos/Genetic10 torneo20 100gen 09 01.csv", "w")
fd.writelines(cabecera)
solucion = None

for n in range(Npruebas):
    tiempoInicio = time()
    solucion = GeneticAlgorithm.geneticAlgorithm(10, seeds[i][n], 100, 100, 0.9, 0.1, 20, 'uniforme')
    tiempoFin = time() - tiempoInicio
    fd.writelines(problemSizes[i].__str__() + "," + str(solucion[0]) + "," + str(solucion[1]) + "\n")
fd.close()

#Genetic Algorithm genérico: [Cruce uniforme, Tamaño de problema: 10, tamaño de torneo 5]
fd = open("./Datos/Genetic10 torneo5 100gen 09 01.csv", "w")
fd.writelines(cabecera)
solucion = None

for n in range(Npruebas):
    tiempoInicio = time()
    solucion = GeneticAlgorithm.geneticAlgorithm(10, seeds[i][n], 100, 100, 0.9, 0.1, 5, 'uniforme')
    tiempoFin = time() - tiempoInicio
    fd.writelines(problemSizes[i].__str__() + "," + str(solucion[0]) + "," + str(solucion[1]) + "\n")
fd.close()



#Prueba bajando prob Cruce
#Genetic Algorithm genérico: [Cruce uniforme, Tamaño de problema: 10, prob Cruce 0.5]
fd = open("./Datos/Genetic10 100gen ProbC05 01.csv", "w")
fd.writelines(cabecera)
solucion = None

for n in range(Npruebas):
    tiempoInicio = time()
    solucion = GeneticAlgorithm.geneticAlgorithm(10, seeds[i][n], 100, 100, 0.5, 0.1, 10, 'uniforme')
    tiempoFin = time() - tiempoInicio
    fd.writelines(problemSizes[i].__str__() + "," + str(solucion[0]) + "," + str(solucion[1]) + "\n")
fd.close()

#Prueba subiendo probabilidad de mutación
#Genetic Algorithm genérico: [Cruce uniforme, Tamaño de problema: 10, prob Mutación 0.5]
fd = open("./Datos/Genetic10 100gen 09 ProbM05.csv", "w")
fd.writelines(cabecera)
solucion = None

for n in range(Npruebas):
    tiempoInicio = time()
    solucion = GeneticAlgorithm.geneticAlgorithm(10, seeds[i][n], 100, 100, 0.9, 0.5, 10, 'uniforme')
    tiempoFin = time() - tiempoInicio
    fd.writelines(problemSizes[i].__str__() + "," + str(solucion[0]) + "," + str(solucion[1]) + "\n")
fd.close()




