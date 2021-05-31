import sys
def dijkstra(grafo, nodo_inicial,solucion):
	etiquetas={}
	visitados=[]
	pendientes=[nodo_inicial]
	nodo_actual= nodo_inicial
	#NODO INICIAL
	etiquetas[nodo_actual] = [0,'']
	#SELECCIONAR EL SIGUIENTE NODO DE MENOR PESO ACUMULADO
	while len(pendientes)>0:
		nodo_actual=nodo_menor_peso(etiquetas, visitados)
		visitados.append(nodo_actual)
		#OBTENER NODOS AYDACENTES
		for adyacente, peso in grafo[nodo_actual].items():
			if adyacente not in pendientes and adyacente not in visitados:
				
				pendientes.append(adyacente)
			nuevo_peso=etiquetas[nodo_actual][0] + grafo[nodo_actual][adyacente]
			#ETIQUETAR
			if adyacente not in visitados:
				if adyacente not in etiquetas:
					print(etiquetas)
					if solucion in etiquetas.keys():
						etiquetas[adyacente]=[nuevo_peso, nodo_actual]
						return etiquetas
						
					etiquetas[adyacente]=[nuevo_peso, nodo_actual]
				else:
					if etiquetas[adyacente][0]>nuevo_peso:
						etiquetas[adyacente]= [nuevo_peso, nodo_actual]
		del pendientes[pendientes.index(nodo_actual)]
	return etiquetas
	
def nodo_menor_peso(etiquetas, visitados):
	menor=sys.maxsize
	for nodo, etiqueta in etiquetas.items():
		if etiqueta[0]<menor and nodo not in visitados:
			menor=etiqueta[0]
			nodo_menor=nodo
	return nodo_menor
