class Graph:
	def __init__(self):
		# dictionary containing keys that map to the corresponding vertex object
		self.vertices = {}
	def add_vertex(self, key):
		"""Add a vertex with the given key to the graph."""
		vertex = Vertex(key)
		self.vertices[key] = vertex
	def get_vertex(self, key):
		"""Return vertex object with the corresponding key."""
		return self.vertices[key]
	def __contains__(self, key):
		return key in self.vertices
	def add_edge(self, src_key, dest_key, weight=1):
		"""Add edge from src_key to dest_key with given weight."""
		self.vertices[src_key].add_neighbour(self.vertices[dest_key], weight)
	def does_edge_exist(self, src_key, dest_key):
		"""Return True if there is an edge from src_key to dest_key."""
		return self.vertices[src_key].does_it_point_to(self.vertices[dest_key])
	def __len__(self):
		return len(self.vertices)
	def __iter__(self):
		return iter(self.vertices.values())


class Vertex:
	def __init__(self, key):
		self.key = key
		self.points_to = {}
	def get_key(self):
		"""Return key corresponding to this vertex object."""
		return self.key
	def add_neighbour(self, dest, weight):
		"""Make this vertex point to dest with given edge weight."""
		self.points_to[dest] = weight
	def get_neighbours(self):
		"""Return all vertices pointed to by this vertex."""
		return self.points_to.keys()
	def get_weight(self, dest):
		"""Get weight of edge from this vertex to dest."""
		return self.points_to[dest]
	def does_it_point_to(self, dest):
		"""Return True if this vertex points to dest."""
		return dest in self.points_to