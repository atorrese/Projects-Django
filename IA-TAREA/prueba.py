from Algoritmos.Nodo import Nodo

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

if __name__=="__main__":
	conexiones={
	"n1":{"n2","n3","n11"},
	"n2":{"n4","n5"},
	"n3":{"n5","n6"},
	"n11":{"n12"},
	"n4":{"n7"},
	"n5":{"n7","n8"},
	"n6":{"n8"},
	"n7":{"n9"},
	"n8":{"n9"},
	"n9":{"n10"},
	"n12":{"n13"},
    "n13":{"n14"},
	"n14":{"n9"}
	}
	estado_inicial="n1"
	solucion="n10"
	nodo_solucion=buscar_solucion_DFS(estado_inicial,conexiones,solucion)
	#MOSTRAR RESULTADO
	resultado=[]
	nodo=nodo_solucion
	while nodo.get_padre()!=None:
		resultado.append(nodo.get_datos())
		nodo=nodo.get_padre()
	resultado.append(estado_inicial)
	resultado.reverse()
	print(resultado)

conexiones={

	"Malaga":{"Granada":125, "Madrid":513},
	"Sevilla":{"Madrid":514},
	"Granada":{"Malaga":125,"Madrid":423,
	"Valencia":491},
	"Valencia":{"Granada":491,"Madrid":356,"Zaragoza":309, "Barcelona":346},
	"Madrid":{"Salamanca":203, "Sevilla":514,"Malaga":513, "Granada":423,"Barcelona":603,"Santander":437, "Valencia":356,"Zaragoza":313, "Santander":437,"Santiago":599},
	"Salamanca":{"Santiago":390, "Madrid":203}, 
	"Santiago":{"Salamanca":390, "Madrid":599},
	"Santander":{"Madrid":437, "Zaragoza":394}, 
	"Zaragoza":{"Barcelona":296, "Valencia":309,
	"Madrid":313},
	"Barcelona":{"Zaragoza":296, "Madrid":603,"Valencia":346}
	}