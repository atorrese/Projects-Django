from AlgoritmosBusquedas.Informados  import buscar_solucion_UCS

print("""================================================================================================================================
+                                                                                                                              +
+                                    ALGORITMO BUSQUEDA DE COSTO UNIFORME                                                      +
+                                                                                                                              +
================================================================================================================================
 """)
if __name__=="__main__":
	conexiones={
	"Santa Ana":{"Chalatenango":53,"La Libertad":45,"Sansonate":76,"Ahuachapan":83},
	"Chalatenango":{"Cabañas":67,"Cuscatlan":76,"San Salvador":74,"La Libertad":67,"Santa Ana":53},
	"La Libertad":{"San Salvador":64,"Sansonate":38,"Santa Ana":45},
	"Sansonate":{"La Libertad":38,"Santa Ana":76,"Ahuachapan":56},
	"Ahuachapan":{"Santa Ana":83,"Sansonate":56},
	"San Salvador":{"Cuscatlan":55,"Chalatenango":74,"La Libertad":64,"La Paz":78},
	"Cuscatlan":{"Cabañas":56,"Chalatenango":76,"San Salvador":55,"La Paz":88,"San Vicente":49},
	"Cabañas":{"Cuscatlan":56,"Chalatenango":67,"San Vicente":39},
	"San Vicente":{"Cuscatlan":49,"Cabañas":39,"La Paz":48,"San Miguel":97,"Usulutan":82},
	"La Paz":{"Cuscatlan":88,"San Vicente":48,"San Salvador":78},
	"Usulutan":{"San Vicente":82,"San Miguel":77},
	"San Miguel":{"San Vicente":97,"Usulutan":77,"Morazan":66,"La Union":57},
	"Morazan":{"San Miguel":66,"La Union":54},
	"La Union":{"Morazan":54,"San Miguel":57},
	}
	estado_inicial="Santa Ana"
	solucion="La Union"
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