import sys, random

def getProblemInstance(n, walls):
    """
    This method generates a new problem instance.
    Cells with value 0 means empty cells. Cells with value -1 are walls.
    Cells with value i (1..n) are occupied by the i-th car.

    Info extra para Práctica 3:
        2 coches por defecto, uno en cada esquina


    Returns a maze (problem instance)

    Parameters:

    :param n:       size of the maze (Int)
    :param walls:   walls to be placed on the maze [row (n-2)][col (n)]

    """
    maze = [[0 for i in range(n)] for j in range(n)]

    #random.seed(seed)

    #number of walls
    #nWalls = int(n * (n-2) * 0.2)

    #placing walls
    for i in range(len(walls)):
        maze[1+i] = walls[i].copy()

    #placing cars, labelled as 1, 2, ..., nCars
    #if(nCars > n):
    #   print("** Error **, number of cars must be <= dimension of maze!!")
    #    sys.exit()

    list = [i for i in range(n)]

    '''
    for c in range(nCars):
        idx = random.randint(0, len(list)-1)
        maze[0][list[idx]] = c+1;
        list.pop(idx)
    '''
    #Placing 2 cars on maze's corners
    maze[0][0] = 1;
    maze[0][n-1] = 2;
    return maze;