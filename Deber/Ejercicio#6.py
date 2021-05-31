from Algoritmos.AlgoritmosInformado import buscar_solucion_UCS, buscar_solucion_A_Estrella

print("""================================================================================================================================
+                                                                                                                              +
+                                    ALGORITMO BUSQUEDA DE COSTO UNIFORME                                                      +
+                                                                                                                              +
================================================================================================================================
 """)
if __name__=="__main__":
	conexiones={    
	"Turin":{"Milan":142,"Pavia":162},
	"Milan":{"Turin":142,"Venecia":280,"Parma":125,"Florencia":304},
	"Pavia":{"Turin":162,"Parma":113},
    "Parma":{"Pavia":113,"Milan":125,"Padua":210},
    "Padua":{"Pisa":296,"Florencia":237,"Parma":210,"Venecia":52},
    "Venecia":{"Forli":227,"Milan":280,"Padua":52},
    "Forli":{"Venecia":227,"Roma":447},
    "Florencia":{"Padua":237,"Milan":304,"Pisa":102,"Siena":74,"Roma":283},
    "Pisa":{"Padua":296,"Roma":383,"Florencia":102},
    "Roma":{"Forli":447,"Siena":244,"Pisa":383,"Florencia":283,"Napoles":226},
    "Siena":{"Roma":244,"Florencia":74},
    "Napoles":{"Roma":226}
	}
	coord={
		"Turin":893,
		"Milan":774,
		"Pavia":764,
		"Parma":658,
		"Padua":695,
		"Venecia":734,
		"Forli":557,
		"Florencia":473,
		"Pisa":571,
		"Roma":226,
		"Siena":437,
		"Napoles":0
	}
	estado_inicial = "Pavia"
	solucion="Napoles"
	nodo_solucion=buscar_solucion_A_Estrella(conexiones, estado_inicial, solucion,coord)
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


print("""================================================================================================================================
+                                                                                                                              +
+                                    ALGORITMO BUSQUEDA DE COSTO UNIFORME                                                      +
+                                                                                                                              +
================================================================================================================================
 """)
if __name__=="__main__":
	conexiones={    
	"Turin":{"Milan":142,"Pavia":162},
	"Milan":{"Turin":142,"Venecia":280,"Parma":125,"Florencia":304},
	"Pavia":{"Turin":162,"Parma":113},
    "Parma":{"Pavia":113,"Milan":125,"Padua":210},
    "Padua":{"Pisa":296,"Florencia":237,"Parma":210,"Venecia":52},
    "Venecia":{"Forli":227,"Milan":280,"Padua":52},
    "Forli":{"Venecia":227,"Roma":447},
    "Florencia":{"Padua":237,"Milan":304,"Pisa":102,"Siena":74,"Roma":283},
    "Pisa":{"Padua":296,"Roma":383,"Florencia":102},
    "Roma":{"Forli":447,"Siena":244,"Pisa":383,"Florencia":283,"Napoles":226},
    "Siena":{"Roma":244,"Florencia":74},
    "Napoles":{"Roma":226}
	}
	estado_inicial ="Turin"
	solucion="Roma"
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
