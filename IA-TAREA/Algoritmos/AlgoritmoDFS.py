from .Nodo import Nodo
def buscar_solucion_DFS(estado_inicial,conexiones,solucion):
    solucionado=False
    nodos_visitados=[]
    nodos_frontera=[]
    nodoInicial= Nodo(estado_inicial)
    nodos_frontera.append(nodoInicial)
    while (not solucionado) and len(nodos_frontera)!=0:
        nodo= nodos_frontera.pop()
        nodos_visitados.append(nodo)
        if nodo.get_datos() == solucion:
            #SOLUCION ENCONTRADA
            solucionado= True
            return nodo
        else:
            dato_nodo=nodo.get_datos()
            lista_hijos=[]
            for un_hijo in conexiones[dato_nodo]:
                hijo=Nodo(un_hijo)
                lista_hijos.append(hijo)
                if not hijo.en_lista(nodos_visitados) and not hijo.en_lista(nodos_frontera):
                    nodos_frontera.append(hijo)
            nodo.set_hijos(lista_hijos)
""" def buscar_solucion_DFS(estado_inicial, solucion):
    solucionado = False
    nodos_visitados = []
    nodos_frontera = []
    nodoInicial = Nodo(estado_inicial)
    nodos_frontera.append(nodoInicial)
    while (not solucionado) and len(nodos_frontera) != 0:
        nodo = nodos_frontera.pop()
        # EXTRAER NODO Y AGREGARLO A VISITADOS
        nodos_visitados.append(nodo)
        if nodo.get_datos() == solucion:
            # SOLUCION ENCONTRADA
            solucionado = True
            return nodo
        else:
            # EXPANDIR NODOS HIJO
            dato_nodo = nodo.get_datos()
            # OPERADOR IZQUIERDO
            hijo = [dato_nodo[1], dato_nodo[0], dato_nodo[2], dato_nodo[3]]
            hijo_izquierdo = Nodo(hijo)

            if not hijo_izquierdo.en_lista(nodos_visitados) and not hijo_izquierdo.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_izquierdo)
                # OPERADOR CENTRAL
            hijo = [dato_nodo[0], dato_nodo[2], dato_nodo[1], dato_nodo[3]]
            hijo_central = Nodo(hijo)
            if not hijo_central.en_lista(nodos_visitados) and not hijo_central.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_central)
                # OPERADOR DERECHO
            hijo = [dato_nodo[0], dato_nodo[1], dato_nodo[3], dato_nodo[2]]
            hijo_derecho = Nodo(hijo)
            if not hijo_derecho.en_lista(nodos_visitados) and not hijo_derecho.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_derecho)
            nodo.set_hijos([hijo_izquierdo, hijo_central, hijo_derecho])


def DFS_prof_iter(nodo,solucion):
    for limite in range(0,100):
        visitados=[]
        sol=buscar_solucion_DFS_limitado(nodo, solucion, visitados, limite)
        if sol !=None:
            return sol

def DFS_prof_iter2(nodo,conexiones,solucion):
    for limite in range(0,100):
        visitados=[]
        sol=buscar_solucion_DFS_limitado2(nodo,conexiones, solucion, visitados, limite)
        if sol !=None:
            return sol

def buscar_solucion_DFS_limitado2(nodo,conexiones ,solucion, visitados, limite):
    if limite>0:
        visitados.append(nodo)
        if nodo.get_datos()==solucion:
            return nodo
        else:
            #EXPANDIR NODOS HIJO (CIUDADES CON CONEXION)
            dato_nodo=nodo.get_datos()
            lista_hijos=[]
            for un_hijo in conexiones[dato_nodo]:
                hijo=Nodo(un_hijo)
                if not hijo.en_lista(visitados):
                    lista_hijos.append(hijo)
            nodo.set_hijos(lista_hijos)
            for nodo_hijo in nodo.get_hijos():
                if not nodo_hijo.get_datos() in visitados:
                    #LLAMADA RECURSIVA
                    sol=buscar_solucion_DFS_limitado(nodo_hijo,solucion,visitados,limite-1)
                    if sol!= None:
                        return sol
        return None



def buscar_solucion_DFS_limitado(nodo, solucion, visitados, limite):
    if limite>0:
        visitados.append(nodo)
        if nodo.get_datos()==solucion:
            return nodo
        else:
            #EXPANDIR NODOS HIJO (CIUDADES CON CONEXION)
            dato_nodo=nodo.get_datos()
            lista_hijos=[]
            for un_hijo in conexiones[dato_nodo]:
                hijo=Nodo(un_hijo)
                if not hijo.en_lista(visitados):
                    lista_hijos.append(hijo)
            nodo.set_hijos(lista_hijos)
            for nodo_hijo in nodo.get_hijos():
                if not nodo_hijo.get_datos() in visitados:
                    #LLAMADA RECURSIVA
                    sol=buscar_solucion_DFS_limitado2(nodo_hijo,conexiones,solucion,visitados,limite-1)
                    if sol!= None:
                        return sol
        return None

if __name__=="__main__":
    conexiones={
        "Malaga":{"Salamanca","Madrid","Barcelona"},
        "Sevilla":{"Santiago","Madrid"},
        "Granada":{"Valencia"},
        "Valencia":{"Barcelona"},
        "Madrid":{"Salamanca","Sevilla","Malaga","Barcelona","Santander"},
        "Salamanca":{"Malaga","Madrid"},
        "Santiago":{"Sevilla","Santander","Barcelona"},
        "Santander":{"Santiago","Madrid"},
        "Zaragoza":{"Barcelona"},
        "Barcelona":{"Zaragoza","Santiago","Madrid","Malaga","Valencia"}
        }
    estado_inicial="Malaga"
    solucion="Santiago"
    nodo_inicial=Nodo(estado_inicial)
    nodo=DFS_prof_iter(nodo_inicial,solucion)
    #MOSTRAR RESULTADO
    if nodo!=None:
        resultado=[]
        while nodo.get_padre()!=None:
            resultado.append(nodo.get_datos())
            
            nodo=nodo.get_padre()
        resultado.append(estado_inicial)
        resultado.reverse()
        print(resultado)
    else:
        print("SOLUCIÓN NO ENCONTRADA")

if __name__=="__main__":
    conexiones={
	"n1":{"n2","n3","n11"},
	"n11":{"n12"},
    "n12":{"n13"},
    "n13":{"n14"},
    "n2":{"n4","n5"},
	"n3":{"n5","n6"},
	"n4":{"n7"},
	"n5":{"n7","n8"},
	"n6":{"n8"},
	"n7":{"n9"},
	"n8":{"n9"},
	"n14":{"n9"},
    "n9":{"n10"},
	}
    estado_inicial="n1"
    solucion="n10"
    nodo_inicial=Nodo(estado_inicial)
    nodo=DFS_prof_iter(nodo_inicial,solucion)
    #MOSTRAR RESULTADO
    if nodo!=None:
        resultado=[]
        while nodo.get_padre()!=None:
            resultado.append(nodo.get_datos())
            nodo=nodo.get_padre()
        resultado.append(estado_inicial)
        resultado.reverse()
        print(resultado)
    else:
        print("SOLUCIÓN NO ENCONTRADA")
if __name__=="__main__":
    conex={
	"n1":{"n2","n3","n11"},
	"n11":{"n12"},
    "n12":{"n13"},
    "n13":{"n14"},
    "n2":{"n4","n5"},
	"n3":{"n5","n6"},
	"n4":{"n7"},
	"n5":{"n7","n8"},
	"n6":{"n8"},
	"n7":{"n9"},
	"n8":{"n9"},
	"n14":{"n9"},
    "n9":{"n10"},
	}
    estado_inicial="n1"
    solucion="n10"
    nodo_inicial=Nodo(estado_inicial)
    nodo=DFS_prof_iter2(nodo_inicial,conex,solucion)
    #MOSTRAR RESULTADO
    if nodo!=None:
        resultado=[]
        while nodo.get_padre()!=None:
            resultado.append(nodo.get_datos())
            nodo=nodo.get_padre()
        resultado.append(estado_inicial)
        resultado.reverse()
        print(resultado)
    else:
        print("SOLUCIÓN NO ENCONTRADA")
 """




