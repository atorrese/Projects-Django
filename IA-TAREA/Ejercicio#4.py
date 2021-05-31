from Algoritmos.AlgoritmoFloydSofis import Evalua_Floyds

if __name__ =='__main__':
    vertices={0,1,2,3,4}
    conexiones={
        0:{ 1:0.4,4:0.3},
        1:{ 0:0.4,2:0.5,3:0.3,4:0.1},
        2:{1:0.5,3:0.5},
        3:{1:0.3,2:0.5,4:0.5}, 
        4:{0:0.3,1:0.1,3:0.5} 
    }
    estado_inicial=0
    solucion=2
    Evalua_Floyds(conexiones,vertices,estado_inicial,solucion)
