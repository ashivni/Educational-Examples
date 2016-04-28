import numpy
import random
import Queue

class bstNode:
	def __init__(self,key,value):
		self.key = key
		self.value = value
		self.left = None
		self.right = None
		self.parent = None

		self.color = 'b'		# Needed only for black-red trees

		# Auxillary variables, not needed for basic functions:
		self.N = 1	# Size of the subtree rooted a this node
		self.depth = 0	# Distance of this node from the root

	def __repr__(self):
		return "bstNode(key, value)"
	
	def __str__(self):
		if self.left != None:
			leftStr = str(self.left.key)
		else:
			leftStr = 'None'

		if self.right != None:
			rightStr = str(self.right.key)
		else:
			rightStr = 'None'

		if self.parent != None:
			parentStr = str(self.parent.key)
		else:
			parentStr = 'None'
		
		return 'key = ' + str(self.key) + ', value = ' + str(self.value) + ', left = ' + leftStr + ', right = ' + rightStr + ', parent = ' + parentStr

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
		parent = kwargs.get('parent',None)
		depth = kwargs.get('depth',0)

		if head is None:
			head = bstNode(key,value)
			head.depth = depth
			head.parent = parent

		elif head.key == key:
			head.value = value
		
		elif head.key > key:
			head.left = self.put(key,value,head=head.left,depth=head.depth+1,parent=head)

		else:
			head.right = self.put(key,value,head=head.right,depth=head.depth+1,parent=head)

		# Set the size and depth as needed
		head.N = self.size(head.left) + self.size(head.right) + 1
		self.depth = self.depth if self.depth > head.depth else head.depth
		
		return head

	def inOrderPrint(self,**kwargs):
		head = kwargs.get('head',self.root)
		
		if head is None:
			return

		self.inOrderPrint(head=head.left)
		print head 
		self.inOrderPrint(head=head.right)

	def bfsPrint(self,**kwargs):
		head = self.root
		q = Queue.Queue()
		if head is not None:
			q.put(head)

		while not q.empty():
			head = q.get()
			print head
			if head.left is not None:
				q.put(head.left)
			if head.right is not None:
				q.put(head.right)
	
	def dfsPrint(self,**kwargs):
		head = self.root
		q = Queue.LifoQueue()
		if head is not None:
			q.put(head)

		while not q.empty():
			head = q.get()
			print head
			if head.left is not None:
				q.put(head.left)
			if head.right is not None:
				q.put(head.right)


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


