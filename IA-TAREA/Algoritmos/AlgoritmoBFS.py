from .Nodo import Nodo

def buscar_solucion_BFS(conexiones, estado_inicial, solucion):
	solucionado=False
	nodos_visitados=[]
	nodos_frontera=[]
	nodoInicial= Nodo(estado_inicial)
	nodos_frontera.append(nodoInicial)
	while (not solucionado) and len(nodos_frontera) !=0:
		nodo=nodos_frontera[0]
		#EXTRAER NODO Y AGREGARLO A VISITADOS
		nodos_visitados.append(nodos_frontera.pop(0))
		if nodo.get_datos() == solucion:
			#SOLUCION ENCONTRADA
			solucionado= True
			return nodo
		else:
			#EXPANDIR NODOS HIJO (CIUDADES CON CONEXION)
			dato_nodo=nodo.get_datos()
			lista_hijos=[]
			for un_hijo in conexiones[dato_nodo]:
				hijo=Nodo(un_hijo)
				lista_hijos.append(hijo)
				if not hijo.en_lista(nodos_visitados) and not hijo.en_lista(nodos_frontera):
					nodos_frontera.append(hijo)
			nodo.set_hijos(lista_hijos)

