# Sample implementations of basic sorts in python
# The implementations are not aimed to be roboust, but
# to be instructive
import copy
import numpy

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

