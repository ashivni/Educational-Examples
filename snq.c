#include <stdio.h>
#include <stdlib.h>

typedef struct node 
{
	void *data;
	struct node *next;
} node;


// ********* STACK Functions ********* //
typedef struct
{
	node *head;
}	stack;

stack * stack_initialize(void *data)
{
	stack *st = (stack *)malloc(sizeof(stack));
	node *head = (node *)malloc(sizeof(node));
	head->data = data;
	head->next = NULL;
	st->head = head;

	return st;
}

void stack_push(stack *st, void *data)
{
	node *new = (node *)malloc(sizeof(node));
	new->data = data;
	new->next = st->head;
	st->head = new;
}

node * stack_pop(stack *st)
{
	if (st->head == NULL)
	{
		printf("Warning: Popping empty stack. Returning NULL.\n");
		return NULL;
	}

	node *temp = st->head;
	st->head = st->head->next;

	return temp;
}

void stack_print(stack *st, int dType)
{
	/*
	Print a stack where the data is of type given by dType
	dType == 0: int
	dType == 1: char

	*/
	node *head = st->head;

	while(head != NULL)
	{
		switch (dType)
		{
			case 0:
				printf("%d\n",*(int *)(head->data));
				break;

			case 1:
				printf("%c\n",*(char *)(head->data));
				break;

			default:
				printf("Warning: Unknown data type.\n");
				break;
		}

		head = head->next;
	}

}

void stack_free(stack **st)
{
	node *head = (*st)->head;
	while (head !=NULL)
	{
		node *temp = head->next;
		free(head);
		head = temp;
	}
	free(*st);
}

void stack_test()
{
	int len = 10;
	int a[len], count=0;
	
	for(count = 0; count < len; count++)
	{
		a[count] = count;
	}

	stack *st = stack_initialize((void *)(&a[0]));
	for(count = 1; count < len; count++)
	{
		stack_push(st,(void *)(&a[count]));
	}

	stack_print(st,0);

	for(count = 0; count < len; count++)
	{
		node *nd = stack_pop(st);
		printf("Popped: %d\n",*(int*)(nd->data));
		free(nd);
	}

	for(count = 1; count < len; count++)
	{
		a[count] *= 2;
		stack_push(st,(void *)(&a[count]));
	}
	stack_print(st,0);
	stack_free(&st);	
}
// ********* END STACK Functions ********* //

// ********* QUEUE Functions ********* //
typedef struct
{
	node *head;
	node *tail;
}	queue;

queue * queue_initialize(void *data)
{
	queue *q = (queue *)malloc(sizeof(queue));
	node *head = (node *)malloc(sizeof(node));
	head->data = data;
	head->next = NULL;
	q->head = head;
	q->tail = head;

	return q;
}

void queue_push(queue *q, void *data)
{
	node *new = (node *)malloc(sizeof(node));
	new->data = data;
	new->next = NULL;
	if (q->tail != NULL)
	{
		q->tail->next = new;
	}
	if (q->head == NULL)
	{
		q->head = new;
	}
	q->tail = new;
}

node * queue_pop(queue *q)
{
	if (q->head == NULL)
	{
		printf("Warning: Popping empty queue. Returning NULL.\n");
		return NULL;
	}

	node *temp = q->head;
	q->head = q->head->next;
	if (q->head == NULL)
	{
		q->tail = NULL;
	}

	return temp;
}

void queue_print(queue *q, int dType)
{
	/*
	Print a queue where the data is of type given by dType
	dType == 0: int
	dType == 1: char

	*/
	node *head = q->head;

	while(head != NULL)
	{
		switch (dType)
		{
			case 0:
				printf("%d\n",*(int *)(head->data));
				break;

			case 1:
				printf("%c\n",*(char *)(head->data));
				break;

			default:
				printf("Warning: Unknown data type.\n");
				break;
		}

		head = head->next;
	}

}

void queue_free(queue **q)
{
	node *head = (*q)->head;
	while (head !=NULL)
	{
		node *temp = head->next;
		free(head);
		head = temp;
	}
	free(*q);
}

void queue_test()
{
	int len = 10;
	int a[len], count=0;
	
	for(count = 0; count < len; count++)
	{
		a[count] = count;
	}

	queue *q = queue_initialize((void *)(&a[0]));
	for(count = 1; count < len; count++)
	{
		queue_push(q,(void *)(&a[count]));
	}

	queue_print(q,0);

	for(count = 0; count < len; count++)
	{
		node *nd = queue_pop(q);
		printf("Popped: %d\n",*(int*)(nd->data));
		free(nd);
	}

	for(count = 1; count < len; count++)
	{
		a[count] *= 2;
		queue_push(q,(void *)(&a[count]));
	}
	queue_print(q,0);
	queue_free(&q);	
}
// ********* QUEUE Functions ********* //



int main()
{
	queue_test();
	return 1;

}
