import numpy

class linkedListNode:
	"""
	A simple data structure representing a node in a singly linked linked list
	"""
	def __init__(self,data):
		self.data = data
		self.child = None

	def setChild(self,child):
		self.child = child

	def setData(self,data):
		self.data = data
	
	def getData(self):
		return self.data

	def getChild(self):
		return self.child


class linkedList:
	"""
	A singly linked link list class. Represents a FILO Q.
	"""

	def __init__(self,data):
		self.head = linkedListNode(data)

	def push(self,data):
		newHead = linkedListNode(data)
		newHead.child = self.head
		self.head = newHead

	def pop(self):
		if self.head is None:
			return self.head
		
		oldHead = self.head
		self.head = self.head.child
		return oldHead
	
	def printLL(self):
		head = self.head
		while head is not None:
			print head.data
			head = head.child
	
	def reverse(self):
		"""
		Reverse the linked list
		"""
		last = None
		head = self.head
		while head is not None:
			temp = head
			head = head.child
			temp.child = last
			last = temp

		self.head = last
			
def swap(x,i,j):
	"""
	Swap the ith and the jth element of the array x
	"""
	temp = x[i]
	x[i] = x[j]
	x[j] = temp

class heap:
	"""
	A simple heap class needed for a priority queue
	"""
	def __init__(self,data=None):
		"""
		Initialize a heap with 'data'
		"""
		self.x = [None]	# Heap initially empty. There is no nice way to ensuring that x never grows beyond 
								# length N in python, so we will enforce this "manually"
		self.heapLen = 0
		try:
			iterator = iter(data)
			[self.insert(p) for p in data]
		except TypeError:
			pass

	def insert(self,d):
		"""
		Insert data 'd' into the heap
		"""
		self.x.append(d)
		self.heapLen += 1
		self.__swim()

	def delMax(self):
		if self.heapLen > 0:
			swap(self.x,1,self.heapLen)
			self.heapLen -= 1
			self.__sink()
			return self.x.pop()
		else:
			return None
	
	def __swim(self):
		"""
		Re-heapyfy with swim
		"""
		child = self.heapLen
		heaped = True if child <= 1 else False 	# heap of length 1 or less is always in heap order

		while not heaped and child > 1:
			parent = numpy.floor(0.5*child).astype(int)
			if self.x[child] > self.x[parent]:
				swap(self.x,child,parent)
				child = parent
			else:
				heaped = True


	def __sink(self):
		"""
		Re-heapyfy with sink
		"""
		parent = 1
		heaped = True if self.heapLen <= 1 else False # Heap of len 1 or less is always in heap order

		while not heaped:
			child1, child2 = parent*2, parent*2+1
			if child1 > self.heapLen:
				break
			elif child2 > self.heapLen:
				maxChild = child1
				heaped = True
			elif self.x[child1] > self.x[child2]:
				maxChild = child1
			else:
				maxChild = child2
			if self.x[parent] < self.x[maxChild]:
				swap(self.x,parent,maxChild)
				parent = maxChild
			else:
				heaped = True
				

class priorityQue:
	"""
	A simple priorityQue client implemented with a heap datastructure
	"""

	def __init__(self):
		"""
		N : Number of keys to keep
		"""
		self.hp = heap()	

	def push(self,data):
		"""
		Push 'data' into the queue 
		"""
		self.hp.insert(data)

	def pop(self):
		return self.hp.delMax()

	def len(self):
		return self.hp.heapLen

