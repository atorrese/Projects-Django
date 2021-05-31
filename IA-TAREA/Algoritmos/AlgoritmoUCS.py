from .Nodo import Nodo

def buscar_solucion_UCS(conexiones, estado_inicial, solucion):
	solucionado=False
	nodos_visitados=[]
	nodos_frontera=[]
	nodo_inicial=Nodo(estado_inicial)
	nodo_inicial.set_coste(0)
	nodos_frontera.append(nodo_inicial)
	while (not solucionado) and len(nodos_frontera) !=0:
		#ORDENAR LA LISTA DE NODOS FRONTERA
		nodo=nodos_frontera[0]
		#EXTRAER NODO Y AGREGARLO A VISITADOS
		nodos_visitados.append(nodos_frontera.pop(0))
		if nodo.get_datos()==solucion:
			#SOLUCION ENCONTRADA
			solucionado=True
			return nodo
		else:
			#EXPANDIR NODOS HIJO (CIUDADES CON CONEXION)
			dato_nodo = nodo.get_datos()
			lista_hijos=[]
			for un_hijo in conexiones[dato_nodo]:
				hijo=Nodo(un_hijo)
				coste=conexiones[dato_nodo][un_hijo]
				hijo.set_coste(nodo.get_coste()+ coste)
				lista_hijos.append(hijo)
				if not hijo.en_lista(nodos_visitados):
					if hijo.en_lista(nodos_frontera):
						for n in nodos_frontera:
							if n.igual(hijo) and n.get_coste()>hijo.get_coste():
								nodos_frontera.remove(n)
								nodos_frontera.append(hijo)
					else:
						nodos_frontera.append(hijo)
				nodo.set_hijos(lista_hijos)
