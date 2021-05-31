from Algoritmos.AlgoritmoBFS import buscar_solucion_BFS
from Algoritmos.AlgoritmoDFS import buscar_solucion_DFS
print("""================================================================================================================================
+                                                                                                                              +
+                                 	ALGORITMO BUSQUEDA DE BUSQUEDA EN ANCHURA                                                  +
+                                                                                                                              +
================================================================================================================================
 """)
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
	"n14":{"n9"},
    "n10":{}
	}
	estado_inicial="n1"
	solucion="n10"
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
	"n1":{"n2","n3","n11"},
	"n2":{"n4","n5"},
	"n3":{"n5","n6"},
	"n4":{"n7"},
	"n5":{"n7","n8"},
	"n6":{"n8"},
	"n7":{"n9"},
	"n8":{"n9"},
	"n9":{"n10"},
	"n10":{},
	"n11":{"n12"},

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