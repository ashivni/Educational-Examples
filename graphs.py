import Queue

class graph:
	def __init__(self,nVert,edges=[]):
		"""
		Initiate a graph with nVert vertices (0,...,nVert-1). 
		'edges' is a list of tuples, where each tuple is a pair 
		of connected vertices. Duplicate edges are not allowed.
		"""
		self.nVert = nVert
		self.nEdge = 0
		self.verts = [set() for _ in xrange(nVert)]	# Each vertex is represented as a set of all other vertices it is connected to

		try:
			for edge in edges:
				self.addEdge(edge[0],edge[1])
		except TypeError:
			raise Exception("Are your edges iterable?")

	def addEdge(self, v, u):
		"""
		Add an edge between vertex v and u
		"""
		self.verts[u].add(v)
		self.verts[v].add(u)
		self.nEdge += 1

	def degree(self, v):
		"""
		Return degree of vertex v
		"""
		return len(self.verts[v])

	def isConnected(self,u,v,method='bfs'):
		"""
		Return True if the vertices u and v are connected.
		A bfs or dfs search is conducted depending on the 'method'
		"""
		marked = [False]*self.nVert
		q = Queue.LifoQueue() if method == 'dfs' else Queue.Queue()
		q.put(u)

		while not q.empty():
			i = q.get()
			if not marked[i]:
				if i == v:
					return True
				else:
					marked[i] = True
					for j in self.verts[i]:
						if not marked[j]:
							q.put(j)

		return False


	def path(self,u,v,method='bfs'):
		"""
		Return a sequence of connected vertices starting at u and ending at v if there is a path
		between u and v. An empty sequence is returned otherwise.
		A bfs or dfs search is conducted depending on the 'method'
		A bfs results in the shortest path
		"""
		marked = [False]*self.nVert
		parent = [-1]*self.nVert
		q = Queue.LifoQueue() if method == 'dfs' else Queue.Queue()
		q.put(u)
		pathFound = False

		while not q.empty() and not pathFound:
			i = q.get()
			if not marked[i]:
				if i == v:
					pathFound = True
				else:
					marked[i] = True
					for j in self.verts[i]:
						if not marked[j]:
							parent[j] = i if parent[j] == -1 else parent[j]
							q.put(j)

		
		path = []
		if pathFound:
			path.append(v)
			while path[-1] != u:
				path.append(parent[path[-1]])
	
		path = path[::-1]

		return path

	def connectedComponents(self):
		"""
		Returns a list of sets, where each set is a set of connected components 
		of the graph.
		"""
		marked = [False]*self.nVert
		connectedComps = []

		for v in range(self.nVert):
			if marked[v] == False:
				component = set()
				q = Queue.LifoQueue() 
				q.put(v)

				while not q.empty():
					i = q.get()
					if i != v:
						component.add(i)
					if not marked[i]:
						marked[i] = True
						for j in self.verts[i]:
							if not marked[j]:
								q.put(j)


				if len(component) > 0:
					connectedComps.append(component)
		
		return connectedComps

	def hasCycle(self,method='bfs'):
		"""
		Returns True if the graph contains a cycle.
		"""
		marked = [False]*self.nVert

		for i in range(self.nVert):
			if not marked[i]:
				q = Queue.LifoQueue() if method == 'dfs' else Queue.Queue()
				q.put(i)
				while not q.empty():
					j = q.get()
					if marked[j]:
						return True
					else:
						marked[j] = True
						for k in self.verts[j]:
							if not marked[k]:
								q.put(k)
		
		return False


def test():
	import networkx as nx
	import numpy
	nNodes = 10
	nEdges = 10
	nTests = 100
	gr = graph(nNodes)
	gr_nx = nx.Graph()
	gr_nx.add_nodes_from(xrange(nNodes))

	print "Constructing a random graph with V = %d vertices and e = %d edges"%(nNodes,nEdges)
	for i in range(nEdges):
		u, v = numpy.random.randint(nNodes), numpy.random.randint(nNodes)
		if u != v:
			gr.addEdge(u,v)
			gr_nx.add_edge(u,v)
	
	print "Running tests for connectedness"
	passed = True
	# Check connectedness 
	for i in range(nTests):
		u, v = numpy.random.randint(nNodes), numpy.random.randint(nNodes)
		if u != v:
			if gr.isConnected(u,v) != nx.has_path(gr_nx,u,v):
				print "Error: ", u, v
				passed = False
	
	if passed:
		print "\t Tests passed"
	else:
		print "\t Tests failed"



	print "Running tests for shortest paths"
	passed = True
	for i in range(nTests):
		u, v = numpy.random.randint(nNodes), numpy.random.randint(nNodes)
		if u != v:
			if gr.isConnected(u,v):
				p1 = gr.path(u,v)
				p2 = nx.shortest_path(gr_nx,u,v)
				if len(p1) != len(p2):
					print len(p1), len(p2)
					print p1
					print p2
					for i in range(gr.nVert):
						print i, gr.verts[i]
					passed = False
	if passed:
		print "\t Tests passed"
	else:
		print "\t Tests failed"

	print "Running test for existance of cycles"
	passed = True
	hasCycle_nx = len(nx.cycle_basis(gr_nx)) > 0
	if gr.hasCycle() != hasCycle_nx:
		print gr.hasCycle()
		print len(nx.cycle_basis(gr_nx)) == 0
		passed = False

	if passed:
		print "\t Tests passed"
	else:
		print "\t Tests failed"



