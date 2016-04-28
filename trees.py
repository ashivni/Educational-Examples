import numpy
import random
class bstNode:
	def __init__(self,key,value):
		self.key = key
		self.value = value
		self.left = None
		self.right = None

		self.color = 'b'		# Needed only for black-red trees

		# Auxillary variables, not needed for basic functions:
		self.N = 1	# Size of the subtree rooted a this node
		self.depth = 0	# Distance of this node from the root

class bst:
	"""
	A binary search tree with unique keys.
	"""
	def __init__(self,key,value):
		self.root = bstNode(key,value)
		self.depth = 0

	def size(self,node):
		return 0 if node is None else node.N

	def get(self,key,**kwargs):
		"""
		Look for key in the tree. Return None key not found, else return the value.
		"""

		head = kwargs.get('head',self.root)

		if head is None:
			return None

		if head.key == key:
			return head.value

		return self.get(key,head=head.left) if head.key > key else self.get(key,head=head.right)

	def put(self,key,value,**kwargs):
		"""
		If key exists in the tree, replace value. 
		Else, add key.
		"""
		
		head = kwargs.get('head',self.root)
		depth = kwargs.get('depth',0)

		if head is None:
			head = bstNode(key,value)
			head.depth = depth

		elif head.key == key:
			head.value = value
		
		elif head.key > key:
			head.left = self.put(key,value,head=head.left,depth=head.depth+1)

		else:
			head.right = self.put(key,value,head=head.right,depth=head.depth+1)

		# Set the size and depth as needed
		head.N = self.size(head.left) + self.size(head.right) + 1
		self.depth = self.depth if self.depth > head.depth else head.depth
		
		return head

	def inOrderPrint(self,**kwargs):
		head = kwargs.get('head',self.root)
		
		if head is None:
			return

		self.inOrderPrint(head=head.left)
		print (head.key, head.value, head.N)
		self.inOrderPrint(head=head.right)

	def maxKey(self):
		head = self.root

		while head is not None:
			if head.right is None:
				return head.key

			head = head.right
	
	def minKey(self):
		head = self.root

		while head is not None:
			if head.left is None:
				return head.key

			head = head.left

def testBST(N = 20):

	"""
	t = bst(1,1)

	randInp = numpy.random.randint(0,100,N)
	sortInp = numpy.sort(randInp)

	for x in randInp:
		t.put(x,1)

	t.inOrderPrint()

	for x in random.sample(randInp,N/2):
		print (x, t.get(x))

	t.inOrderPrint()

	depths = []
	t.treeDepth(depths=depths)
	print depths
	"""

	"""
	depths = {}
	for i in range(10):
		print i
		t = bst(numpy.random.rand(),1)
		for i in range(100000):
			t.put(numpy.random.rand(),1)
			if i % 100 == 0 and i > 0:
				if i < 1000 or i%1000 == 0:
					if i in depths:
						data = depths[i]
						depths[i] = (data[0]+t.depth,data[1]+1)
					else:
						depths[i] = (t.depth,1)

	size, dpt = [], []
	for k, v in depths.iteritems():
		size.append(k)
		dpt.append((1.0*v[0])/v[1])
	
	return numpy.array(size), numpy.array(dpt)
	"""


	t = bst(numpy.random.rand(),1)
	for i in range(1000):
		t.put(numpy.random.rand(),1)

	return t
