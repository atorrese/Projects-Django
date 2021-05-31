from AlgoritmosBusquedas.Informados   import buscar_solucion_BFS, buscar_solucion_DFS
print("""================================================================================================================================
+                                                                                                                              +
+                                 	ALGORITMO BUSQUEDA DE BUSQUEDA EN ANCHURA                                                  +
+                                                                                                                              +
================================================================================================================================
 """)
if __name__=="__main__":
	conexiones={
	"A":{"C","D","E","F","G","H","J"},
	"B":{"C","J"},
	"C":{"A","B","J"},
	"D":{"A","D"},
	"E":{"A","D","G"},
	"F":{"A","G"},
	"G":{"A","E","F","H"},
	"H":{"A","G","J"},
	"J":{"A","B","C","H"}
	}
	estado_inicial="B"
	solucion="F"
	nodo_solucion=buscar_solucion_BFS(conexiones,estado_inicial,solucion)
	#MOSTRAR RESULTADO
	resultado=[]
	nodo=nodo_solucion
	while nodo.get_padre()!=None:
		resultado.append(nodo.get_datos())
		nodo=nodo.get_padre()
	resultado.append(estado_inicial)
	resultado.reverse()
	print(resultado)
print("""================================================================================================================================
+                                                                                                                              +
+                                 	ALGORITMO BUSQUEDA DE BUSQUEDA EN PROFUNDIDAD                                              +
+                                                                                                                              +
================================================================================================================================
 """)
if __name__=="__main__":
	conexiones={
	"A":{"C","D","E","F","G","H","J"},
	"B":{"C","J"},
	"C":{"A","B","J"},
	"D":{"A","D"},
	"E":{"A","D","G"},
	"F":{"A","G"},
	"G":{"A","E","F","H"},
	"H":{"A","G","J"},
	"J":{"A","B","C","H"}
	}
	estado_inicial="B"
	solucion="F"
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