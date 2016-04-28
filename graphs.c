#include <stdio.h>
#include <stdlib.h>

// **** START LINKED LIST FUNCTIONS ****

typedef struct linkedList_node 
{
	int data;
	struct linkedList_node *next;
} linkedList_node;

typedef struct
{
	int size;
	linkedList_node *head;
} linkedList;

linkedList * linkedList_initialize(int data)
{
	linkedList *ll = (linkedList *)malloc(sizeof(linkedList));
	linkedList_node *head = (linkedList_node *)malloc(sizeof(linkedList_node));
	head->data = data;
	head->next = NULL;
	ll->head = head;
	ll->size = 1;

	return ll;
}

void linkedList_push(linkedList *ll,int data)
{
	linkedList_node *head = (linkedList_node *)malloc(sizeof(linkedList_node));
	head->data = data;
	head->next = ll->head;
	ll->head = head;
	ll->size += 1;
}

int linkedList_pop(linkedList *ll)
{
	if(ll->size == 0)
	{
		printf("Error. Trying to pop an empty linkedlist. Exiting\n");
		exit(EXIT_FAILURE);
	}

	int data = (ll->head)->data;
	linkedList_node *oldHead = ll->head;
	ll->head = oldHead->next;
	free(oldHead);
	ll->size -= 1;

	return data;
}

int * linkedList_toArray(linkedList *ll)
{
	int *ar = (int *)malloc((ll->size)*sizeof(int));
	linkedList_node *head = ll->head;

	int count = 0;
	while (head != NULL)
	{
		ar[count] = head->data;
		count += 1;
		head = head->next;
	}

	return ar;
}

void linkedList_free(linkedList **ll)
{
	while((*ll)->head != NULL)
	{
		linkedList_node *temp = ((*ll)->head)->next;
		free((*ll)->head);
		(*ll)->head = temp;
	}

	free(*ll);
}

void linkedList_print(linkedList *ll)
{
	linkedList_node *head = ll->head;

	while (head != NULL)
	{
		printf("%d\n",head->data);
		head = head->next;
	}
}

void linkedList_test()
{
	int len = 10, count = 0;
	linkedList *ll = linkedList_initialize(0);

	for(count = 1; count < len; count++)
	{
		linkedList_push(ll,count);
	}

	printf("Printing Linked List\n");
	linkedList_print(ll);
	printf("Popped: %d\n",linkedList_pop(ll));
	printf("Popped: %d\n",linkedList_pop(ll));
	printf("Pushing 23\n");
	linkedList_push(ll,23);
	printf("Printing Linked List\n");
	linkedList_print(ll);
	linkedList_free(&ll);
}
// **** END LINKED LIST FUNCTIONS ****

// **** START GRAPH FUNCTIONS ****

typedef struct graph_node
{
	int ID;
	linkedList
} graph_node;

int main()
{
	linkedList_test();
	return 1;
}
