from Algoritmos.AlgoritmosNoInformales import dijkstra
if __name__=="__main__":
	grafo={
	'1':{'3':6, '2':3},
	'2':{'4':1, '1':3, '3':2},
	'3': {'1':6, '2':2, '4':4, '5':2},
	'4': {'2':1, '3':4, '5':6},
	'5': {'3':2, '4':6, '6':2, '7':2},
	'6': {'5':2, '7':3},
	'7': {'5':2, '6':3}
	}
""" 	etiquetas = dijkstra(grafo, '1')
	print(etiquetas) """


if __name__=="__main__":
	grafo={
	'A': {'C':4, 'D':7},
	'B': {'D':22, 'E':8, 'F':14},
	'C': {'A':4, 'E':3, 'H':10},
	'D': {'A':7, 'B':22},
	'E': {'B':14,'C':3, 'F':9, 'G':6},
	'F': {'B':8,'E':9, 'G':13,'K':13},
	'G': {'E':6, 'F':13,'H':4,'I':17,'J':5},
	'H': {'C':10, 'G':4,'I':18},
	'I': {'G':17, 'H':18,'J':22},
	'J': {'G':5,'I':22, 'K':8},
	'K': {'F':8, 'J':8}
	}
	estado_inicial ='A'
	solucion  ='K'
	etiquetas = dijkstra(grafo, estado_inicial,solucion)
	print(etiquetas)
	key=[solucion]
	key.append(etiquetas[solucion][1])
	elementos=[]
	for i in etiquetas.values():
		elementos.append(i)
	
	for i in elementos[::-1]:
		if i[1]:
			if i[1] in key:
				if   etiquetas[i[1]][1]:
					if not etiquetas[i[1]][1] in key:
						key.append(etiquetas[i[1]][1])
	
	print('Ruta: {} Costo:{}'.format(key[::-1],etiquetas[solucion][0]))
