# Sample implementations of basic sorts in python
# The implementations are not aimed to be roboust, but
# to be instructive
import copy
import numpy

def isSorted(x):
	"""
	Return True if x is sorted
	"""
	for i in range(len(x)-1):
		if x[i] > x[i+1]:
			print i, i+1, x[i], x[i+1]
			return False

	return True

def swap(x,i,j):
	"""
	Swap the ith and the jth element of the array x
	"""
	temp = x[i]
	x[i] = x[j]
	x[j] = temp


def insertionSort(x):
	"""
	Sort the array-like object x inplace with insertion sort
	"""

	for i in range(len(x)):
		for j in range(i):
			if x[i-j] < x[i-j-1]:
				swap(x,i-j,i-j-1)
			else:
				break


def selectionSort(x):
	"""
	Sort the array-like object x inplace with selection sort
	"""
	for i in range(len(x)):
		minId = i
		for j in range(i,len(x)):
			minId = minId if x[minId] < x[j] else j
		swap(x,i,minId)

def mergeSort(x,**kwargs):
	"""
	Sort the array-like object x with merge sort. 
	"""
	start = kwargs.get('start',0)
	end = kwargs.get('end',len(x))

	if end - start == 1 or end == 0: # Array of length 1 is always sorted, also return for empty array
		return

	# Construct auxillary array for merging
	aux = kwargs.get('aux',copy.copy(x))

	# Partition the array and sort the parts
	mid = numpy.floor(0.5*(end+start)).astype('int')
	mergeSort(x,start=start,end=mid,aux=aux)
	mergeSort(x,start=mid,end=end,aux=aux)


	# Merge the sorted partitions into the aux array
	ptr1 = start
	ptr2 = mid
	for i in range(start,end):
		if ptr1 == mid:
			aux[i] = x[ptr2]
			ptr2 += 1
		elif ptr2 == end:
			aux[i] = x[ptr1]
			ptr1 +=1
		elif x[ptr1] < x[ptr2]:
			aux[i] = x[ptr1]
			ptr1+=1
		else:
			aux[i] = x[ptr2]
			ptr2+=1

	# Copy the aux array back to x.
	for i in range(start,end):
		x[i] = aux[i]


def heapSort(x):
	"""
	Sorts the array x by using heapsort
	"""
	h = heap(len(x),x)
	for i in range(len(x)):
		x[len(x)-i-1] = h.delMax()

	
class heap:
	def __init__(self,N,data=None):
		"""
		Initialize a heap of size N, with data such that len(data) <=N
		"""
		self.x = [None]	# Heap initially empty. There is no nice way to ensuring that x never grows beyond 
								# length N in python, so we will enforce this "manually"
		self.heapLen = 0
		self.maxHeapLen = N
		try:
			iterator = iter(data)
			if len(data) > N:
				raise Exception('Heap overflow. Too much data')
			else:
				[self.insert(p) for p in data]
		except TypeError:
			pass
		

	def insert(self,d):
		"""
		Insert data 'd' into the heap
		"""
		if self.heapLen == self.maxHeapLen:
			raise Exception('Heap overflow. Cannot insert in a full heap')

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
	
	def delMin(self):
		if self.heapLen > 0:
			self.heapLen -= 1
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
				
def quicksort(x):
	"""
	Sort x inplace using the classical quicksort algorithm.
	We do not randomize; the user must.
	"""
	def partition(x,lo,hi):
		"""
		Partition the array x[lo,...,hi-1] such that the entry originally
		at x[lo] is at its correct sorted position. Return 'j' where j 
		is the correct index of this entry
		"""
		ptr1, ptr2 = lo+1, hi
		partitioned = False

		while not partitioned:
			while x[ptr1] <= x[lo] and ptr1 < hi:
				ptr1 += 1
		
			while x[ptr2] > x[lo] and ptr2 > lo:
				ptr2 -= 1

			if ptr1 >= ptr2 or ptr1 == hi or ptr2 == lo:
				partitioned = True
			else:
				swap(x,ptr1,ptr2)

		swap(x,lo,ptr2)

		return ptr2

	def sort(x,lo,hi):
		if hi <= lo:
			return
		pivot = partition(x,lo,hi)
		sort(x,lo,pivot-1)
		sort(x,pivot+1,hi)

	sort(x,0,len(x)-1)
