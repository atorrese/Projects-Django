from Algoritmos.AlgoritmoUCS import buscar_solucion_UCS

print("""================================================================================================================================
+                                                                                                                              +
+                                    ALGORITMO BUSQUEDA DE COSTO UNIFORME                                                      +
+                                                                                                                              +
================================================================================================================================
 """)
if __name__=="__main__":
	conexiones={    
	"n1":{"n2":1,"n3":5,"n11":1},
	"n2":{"n4":18,"n5":4},
	"n3":{"n5":2,"n6":20},
	"n11":{"n3":5,"n6":1,"n12":1},
	"n4":{"n7":4},
	"n5":{"n7":6,"n8":7},
	"n6":{"n8":10},
	"n7":{"n9":14},
	"n8":{"n9":14},
	"n9":{"n10":21},
	"n12":{"n6":1,"n13":1},
    "n13":{"n8":1,"n14":1},
	"n14":{"n9":1}
	}
	estado_inicial="n1"
	solucion="n10"
	nodo_solucion=buscar_solucion_UCS(conexiones, estado_inicial, solucion)
	#MOSTRAR RESULTADO
	resultado=[]
	nodo=nodo_solucion
	while nodo.get_padre()!=None:
		resultado.append(nodo.get_datos())
		nodo=nodo.get_padre()
	resultado.append(estado_inicial)
	resultado.reverse()
	print(resultado)
	print("Coste: "+ str(nodo_solucion.get_coste()))