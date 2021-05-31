from .Grafo import Graph
def floyd_warshall(g):
	"""Return dictionaries distance and next_v.
	distance[u][v] is the shortest distance from vertex u to v.
	next_v[u][v] is the next vertex after vertex v in the shortest path from u
	to v. It is None if there is no path between them. next_v[u][u] should be
	None for all u.
	g is a Graph object which can have negative edge weights.
	"""
	distance = {v: dict.fromkeys(g, float('inf')) for v in g}
	next_v = {v: dict.fromkeys(g, None) for v in g}
	for v in g:
		for n in v.get_neighbours():
			distance[v][n] = v.get_weight(n)
			next_v[v][n] = n
	
	for v in g:
		distance[v][v] = 0
		next_v[v][v] = None
	for p in g:
		for v in g:
			for w in g:
				if distance[v][w] > distance[v][p] + distance[p][w]:
						distance[v][w] = distance[v][p] + distance[p][w]
						next_v[v][w] = next_v[v][p]
	return distance, next_v

def print_path(next_v, u, v):
	"""Print shortest path from vertex u to v.
	next_v is a dictionary where next_v[u][v] is the next vertex after vertex u
	in the shortest path from u to v. It is None if there is no path between
	them. next_v[u][u] should be None for all u.
	u and v are Vertex objects.
	"""
	p = u
	while (next_v[p][v]):
		print('{} -> '.format(p.get_key()), end='')
		p = next_v[p][v]
		print('{} '.format(v.get_key()), end='')
		
vertices={0,1,2,3,4}
c={
    0:{ 1:0.4,4:0.3},
    1:{ 0:0.4,2:0.5,3:0.3,4:0.1},
    2:{1:0.5,3:0.5},
    3:{1:0.3,2:0.5,4:0.5}, 
    4:{0:0.3,1:0.1,3:0.5} 
}
def Evalua_Floyds(conexiones,vertices,estado_inicial,solucion):
	g = Graph()
	#Agregamos nodos
	for nodo in vertices:
		if nodo not in g:
			g.add_vertex(nodo)
		else:
			print('Nodo Repetido')
	#Agregamos Conexiones del grafo
	for src in vertices:
		for dest  in vertices:
			if dest in c[src].keys():
				#print('[{},{},{}]'.format(src,dest,c[src][dest]))
				if src not in g:
					print('Vertex {} does not exist.'.format(src))
				elif dest not in g:
					print('Vertex {} does not exist.'.format(dest))			
				else:
					if not g.does_edge_exist(src, dest):
						g.add_edge(src, dest,conexiones[src][dest] )
					else:
						print('Edge already exists.')
	#print(g)
	distance, next_v = floyd_warshall(g)
	#print(distance)
	print('Distancia mas corta:')
	for start in g:
		for end in g:
			if start.get_key()==estado_inicial and end.get_key()== solucion:
				if next_v[start][end]:
					print('De {} A {}: '.format(start.get_key(),end.get_key()),end='')
					print_path(next_v, start, end)
					print('(Distancia {})'.format(round(distance[start][end],1)))

""" print('Menu')
print('add vertex <key>')
print('add edge <src> <dest> <weight>')
print('floyd-warshall')
print('quit')
while True:
	do = input('What would you like to do? ').split()
	operation = do[0]
	if operation == 'add':
		suboperation = do[1]
		if suboperation == 'vertex':
			key = int(do[2])
			if key not in g:
				g.add_vertex(key)
			else:
				print('Vertex already exists.')
		elif suboperation == 'edge':
			src = int(do[2])
			dest = int(do[3])
			weight = int(do[4])
			if src not in g:
				print('Vertex {} does not exist.'.format(src))
			elif dest not in g:
				print('Vertex {} does not exist.'.format(dest))
			else:
				if not g.does_edge_exist(src, dest):
					g.add_edge(src, dest, weight)
				else:
					print('Edge already exists.')
	elif operation == 'floyd-warshall':
		distance, next_v = floyd_warshall(g)
		print('Shortest distances:')
		for start in g:
			for end in g:
				if next_v[start][end]:
					print('From {} to {}: '.format(start.get_key(),end.get_key()),end='')
					print_path(next_v, start, end)
					print('(distance {})'.format(distance[start][end]))
	elif operation == 'quit':
		break
 """