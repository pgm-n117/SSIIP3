from ..Estructuras.Accion import *
from ..Estructuras.Nodo import *


#suma 2 Tuplas x con x e y con y
def SumaTuplas(a,b):
    return (a[0]+b[0],a[1]+b[1])

#Obtiene el estado inicial
def eInicial(maze, n, nCars):
    estado = [(0,0) for i in range(nCars)]
    for i in range(n):
        if (maze[0][i] > 0):
            estado[maze[0][i]-1]=(i,0)
    return estado;

def aplicaAccion(estado,accion):
    nuevoEstado=estado[:]
    nuevoEstado[accion.coche]=SumaTuplas(nuevoEstado[accion.coche],accion.direccion)
    return nuevoEstado;

def Sucesores(listaAcciones, nod):
    nodosSucesores=[]
    for accion in listaAcciones:
        nodosSucesores.append(Nodo(nod, accion, nod.coste+1, None, None, aplicaAccion(nod.estado,accion)))
    return nodosSucesores;

#Obtiene las posibles acciones a partir de un estado
def AccionesPosibles(maze, n, estado):
    acciones=[]
    for direccion in range(4):
        for coche in range(len(estado)):
            posicion=SumaTuplas(estado[coche],dir[direccion])   #Calculamos la posible siguiente posicion
            if(not(posicion[0]<0 or posicion[1]<0 or posicion[0]>n-1 or posicion[1]>n-1 or maze[posicion[1]][posicion[0]]==-1 or posicion in estado) ):
                acciones.append(Accion(coche,dir[direccion]))
    return acciones;

def InicializaHeuristica(n,maze):
    global matrizH
    matrizH=[maze[i][:] for i in range(n)]
    matrizH[0]=[0 for i in range(n)]
    coords=[0,1,[]]
    for x in range(n):
        if (matrizH[n-2][x]==0): matrizH[n-2][x]=1
        if (matrizH[n-2][x]==1 and matrizH[n-3][x]==0):
            matrizH[n-3][x]=2
            coords[2].append((n-3,x))
    for num in range(2,int(n*n/2)):
        noEncontrado=True
        coords.append([])
        for elem in coords[num]:
            (y,x)=elem
            if(matrizH[y][x]==num):
                if((y!=n-1) and matrizH[y+1][x]==0):
                    matrizH[y+1][x]=num+1
                    coords[num+1].append((y+1,x))
                if((y!=0) and matrizH[y-1][x]==0):
                    matrizH[y-1][x]=num+1
                    coords[num+1].append((y-1,x))
                if((x!=n-1) and matrizH[y][x+1]==0):
                    matrizH[y][x+1]=num+1
                    coords[num+1].append((y,x+1))
                if((x!=0) and matrizH[y][x-1]==0):
                    matrizH[y][x-1]=num+1
                    coords[num+1].append((y,x-1))
        if (len(coords[num+1])==0): break
    for i in range(n):
        print(matrizH[i])
    return matrizH

#Calcula la heurística de un nodo, devuelve la distancia en linea recta desde un coche hasta la última fila
def Heuristica(estado):
    h=0
    for pos in estado:
        h += matrizH[pos[1]][pos[0]]
    return h;
'''
    h=0
    for pos in estado:
        h += ((n-1)-pos[1])
        if(-1 in ([maze[i][pos[0]] for i in range(pos[1],n)])):
            h+=1
    return h;
'''


#Comprobamos si un estado es una solución
#Si la segunda componente de algun coche no está en la última fila,
# no estaremos ante una solución
def esSolucion(estado, n):
    for i in range(len(estado)):
        if(estado[i][1] != n-1):
            return False;
    return True;


def mazePreview(num, maze):

    mazePreview=[[" " for i in range(num)]for j in range(num)]
    mazePreview[0]=maze[0][:]
    for i in range(1,num):
        for j in range(num):
            if(maze[i][j]==-1):
                mazePreview[i][j]="x"

    for i in range(num):
        print(mazePreview[i])

    return
