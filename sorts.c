#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

typedef enum {true, false} myBool;
#define arrayPrintPerLine 5

myBool isSorted(int *x, int len)
{
	/* 
	Return true if array x of length len is sorted. 
	*/

	myBool sorted = true;
	int count = 0;
	for(count = 0; count < len-1; count++)
	{
		if (x[count] > x[count+1])
		{
			printf("Breaking sort order with x[%d] = %d, x[%d] = %d\n",count,x[count],count+1,x[count+1]);
			sorted = false;
			break;
		}
	}

	return sorted;
}


int * randomArray(int len)
{
	// Random integer array of lenght len
	int *x = (int *)malloc(len*sizeof(int));
	srand(time(NULL));
	while(len > 0)
	{
		x[--len] = rand();
	}
	return x;
}

void printArray(int *x, int len)
{
	
	int count = 0;
	for(count = 0; count < len; count++)
	{
		printf("x[%.3d] = %.10d\t",count,x[count]);
		if ((count+1)%arrayPrintPerLine == 0) printf("\n");
	}

	printf("\n");
}

void assertSorted(int *x, int len, char *name)
{
	if (isSorted(x,len) == true)
	{
		printf("%s is sorted\n",name);
	}
	else
	{
		printf("%s is unsorted\n",name);
	}
}

void swap(int *x, int i, int j)
{
	int temp = x[i];
	x[i] = x[j];
	x[j] = temp;
}

void insertionSort(int *x, int len)
{
	int i, j;
	for(i = 0; i < len; i++)
	{
		for(j=0; j<i; j++)
		{
			if(x[i-j]<x[i-j-1])
			{
				swap(x,i-j,i-j-1);
			}
			else
			{
				break;
			}
		}
	}
}

void selectionSort(int *x, int len)
{
	int i, j;
	
	for(i=0; i<len; i++)
	{
		int minInd = i;
		for(j=i; j<len; j++)
		{
			minInd = x[j] < x[minInd] ? j : minInd;
		}
		swap(x,i,minInd);
	}
}

void merge(int *x, int len, int div)
{
	/*
	Merge the array x of length 'len' into 
	one sorted array, if x[0...div-1], and 
	x[div... len-1] are sorted
	*/

	// auxillary array for sorting
	int *aux = (int *)malloc(len*sizeof(int));

	// pointers to walk the two divisions
	int ptr1 = 0, ptr2 = div, auxPos = 0;

	while(ptr1 < div || ptr2 < len)
	{
		if (ptr1 < div && ptr2 < len)
		{
			// None of the divisions is exhausted, its business as usual
			if (x[ptr1] < x[ptr2])
			{
				aux[ptr1 + ptr2 - div] = x[ptr1];
				ptr1 += 1;
			}
			else
			{
				aux[ptr1 + ptr2 - div] = x[ptr2];
				ptr2 += 1;
			}
		}
		else if(ptr1 < div)
		{
			aux[ptr1 + ptr2 - div] = x[ptr1];
			ptr1 +=1;
		}
		else
		{
			aux[ptr1 + ptr2 - div] = x[ptr2];
			ptr2 +=1;
		}
	}

	while(len > 0)
	{
		x[len-1] = aux[len-1];
		len -= 1;
	}

	free(aux);
}

void mergeSort(int *x, int len)
{
	/*
	Mergesort an array of length len
	*/
	if (len < 2) return;	// array of length 1 or 0 is always sorted.
	
	int div = len/2;	// Divide array into left and right bits. 
										// left: 0,...,div-1 right: div,...,len-1

	mergeSort(x,div);
	mergeSort(x+div,len-div);
	merge(x,len,div);
}


// **** START HEAP FUNCTIONS ETC. **** //
typedef struct
{
	// An array based datastructure to store a binary heap.
	int maxSize;
	int size;
	int *x;
} heap;

heap * heap_initialize(int maxSize)
{
	heap *h = (heap *)malloc(sizeof(heap));
	h->maxSize = maxSize;
	h->x = (int *)malloc((maxSize+1)*sizeof(int));
	h->size = 0;
	return h;
}

void heap_swim(heap *h)
{
	/*
	Re-establish heap order by "swimming" the last 
	element to its correct position
	*/

	int swimmer = h->size;

	while (swimmer != 1)
	{
		int parent = (int) floor(swimmer*0.5);
		if (h->x[parent] < h->x[swimmer])
		{
			swap(h->x,parent,swimmer);
			swimmer = parent;
		}
		else
		{
			break;
		}
	}

}

void heap_sink(heap *h)
{
	/* 
	Re-establish heap order by sinking the first 
	element to its correct position.
	*/

	int sinker = 1;
	myBool heaped = false;

	while(heaped == false)
	{
		int lChild = 2*sinker, rChild = 2*sinker + 1, maxChild=sinker;

		if(lChild > h->size)
		{ 
			heaped = true;
		}
		else if(rChild > h->size) 
		{ 
			heaped = true; 
			maxChild = h->x[lChild] > h->x[sinker] ? lChild : sinker;
		}
		else if(h->x[rChild] > h->x[sinker] || h->x[lChild] > h->x[sinker])
		{
			maxChild = h->x[rChild] > h->x[lChild] ? rChild : lChild;
		}
		else
		{
			heaped = true;
		}
		swap(h->x,maxChild,sinker);
		sinker = maxChild;
	}
}

void heap_print(heap *h)
{
	printArray(h->x+1,h->size);
}

void heap_push(heap *h, int data)
{
	// Check for heap overflow
	if (h->size == h->maxSize)
	{
		printf(" Trying to push to full heap. Exiting\n");
		fflush(stdout);
		exit(EXIT_FAILURE);
	}

	// Add data to heap
	h->size += 1;
	h->x[h->size] = data;

	// Re-establish heap order
	heap_swim(h);
}

int heap_pop(heap *h)
{
	int popped = h->x[1];

	swap(h->x,1,h->size);
	h->size -= 1;
	
	heap_sink(h);

	return popped;
}

void heap_free(heap **h)
{
	free((*h)->x);
	free(*h);
}

void heap_sort(int *x, int len)
{
	/*
	Sort x with a heap sort. 
	*/

	heap *h = heap_initialize(len);

	int count = 0;
	for(count = 0; count < len; count++)
	{
		heap_push(h,x[count]);
	}


	for(count = 0; count < len; count++)
	{
		x[len-count-1] = heap_pop(h);
	}

	heap_free(&h);
}

// **** END HEAP FUNCTIONS ETC. **** //

// **** START PRIORITY QUEQE FUNCTIONS ETC. **** //
typedef struct 
{
	int maxSize, size;
	heap *h;
} priorityQ;

priorityQ * priorityQ_initialize(int maxSize)
{
	priorityQ * pQ = (priorityQ *)malloc(sizeof(priorityQ));
	pQ->maxSize = maxSize;
	pQ->size = 0;
	pQ->h = heap_initialize(maxSize);

	return pQ;
}

void priorityQ_insert(priorityQ *pQ, int data)
{
	if(pQ->size < pQ->maxSize)
	{
		pQ->size += 1;
		heap_push(pQ->h, data);	
	}
	else if (data < (pQ->h)->x[1])
	{
		heap_pop(pQ->h);
		heap_push(pQ->h,data);
	}
}

int priorityQ_pop(priorityQ *pQ)
{
	if (pQ->size == 0)
	{
		printf("Popping empty priorityQ. Exiting\n");
		exit(EXIT_FAILURE);
	}

	pQ->size -= 1;
	return heap_pop(pQ->h);
}

void priorityQ_print(priorityQ *pQ)
{
	heap_print(pQ->h);
}

// **** END PRIORITY QUEQE FUNCTIONS ETC. **** //


int qs_partition(int *x, int lo, int hi)
{
	int ptr1 = lo+1, ptr2 = hi;
	myBool partitioned = false;

	while (partitioned == false)
	{
		while (x[ptr1] < x[lo] && ptr1 < hi)
		{
			ptr1 += 1;
		}

		while (x[ptr2] > x[lo] && ptr2 > lo)
		{
			ptr2 -= 1;
		}

		if (ptr1 >= ptr2 || ptr1 == hi || ptr2 == lo)
		{
			partitioned = true;
		}
		else
		{
			swap(x,ptr1,ptr2);
		}
	}

	swap(x,lo,ptr2);
	return ptr2;
}

void qs_sort(int *x, int lo, int hi)
{
	if (hi <= lo)	return;

	int pivot = qs_partition(x,lo,hi);
	qs_sort(x,lo,pivot-1);
	qs_sort(x,pivot+1,hi);
}

int main()
{
	int len = 10000000;
	char *name = "X";
	int *x;
	//printArray(x,len);

	/*
	x = randomArray(len);
	printf("\nSorting %s with insertion sort\n",name);
	insertionSort(x,len);
	//printArray(x,len);
	assertSorted(x,len,name);
	free(x);


	x = randomArray(len);
	printf("\nSorting %s with selection sort\n",name);
	selectionSort(x,len);
	//printArray(x,len);
	assertSorted(x,len,name);
	free(x);
	x = randomArray(len);
	printf("\nSorting %s with merge sort\n",name);
	mergeSort(x,len);
	//printArray(x,len);
	assertSorted(x,len,name);
	free(x);

	x = randomArray(len);
	printf("\nSorting %s with heap sort\n",name);
	heap_sort(x,len);
	assertSorted(x,len,name);
	free(x);

	x = randomArray(len);
	printf("\nSorting %s with quick sort\n",name);
	qs_sort(x,0,len-1);
	assertSorted(x,len,name);
	free(x);
	*/
	
	
	x = randomArray(len);
	int pQSize = 10;
	priorityQ *pQ = priorityQ_initialize(pQSize);
	{
		int count = 0;
		for (count = 0; count < len; count++)
		{
			priorityQ_insert(pQ,x[count]);
		}
	}
	while(pQ->size > 0)
	{
		printf("%d\n",priorityQ_pop(pQ));
	}

	mergeSort(x,len);
	printArray(x,pQSize);

	free(x);

	return 1;
}
