import math
inf=math.inf
a= [[0,8,5],[3,0,inf],[inf,2,0]]

conexion={
    1:{2:8,3:5},
    2:{1:3},
    3:{2:2}
}
c={
    0:{ 1:0.4,4:0.3},
    1:{ 0:0.4,2:0.5,3:0.3,4:0.1},
    2:{1:0.5,3:0.5},
    3:{1:0.3,2:0.5,4:0.5}, 
    4:{0:0.3,1:0.1,3:0.5} 
}
el=[0,1,2,3,4]


def grafo_matriz_distancia(elementos,conexiones):
    matriz=[]
    for elem in elementos:
        temp = []
        for celem in elementos:
            if elem != celem:
                if celem in conexiones[elem].keys():
                    temp.append(conexiones[elem][celem])
                else:
                    temp.append(inf)
            else:
                temp.append(0)
        matriz.append(temp)
    return matriz
def floyd(matriz):
    for k in range(len(matriz)):
        for i in range(len(matriz)):
            for j in range(len(matriz)):
                if (matriz[i][k]+matriz[k][j]<matriz[i][j]):
                    matriz[i][j]=round(matriz[i][k]+matriz[k][j],1)
    return matriz
matriz_distancia= grafo_matriz_distancia(el,c)
for row in matriz_distancia:
    print(row)
print('\n\n')
suma=0
lista=[]
for i ,row in enumerate(floyd(matriz_distancia)):
    for j ,col in enumerate(row):
        if(j==0 ):
            lista.append(i)
            suma+=col
    
    print(suma)
    print(lista)
    print(i,row)

