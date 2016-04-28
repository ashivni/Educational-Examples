#include <stdio.h>
#include <stdlib.h>

struct node
{
	void *data;
	struct node *next;
};

struct ll
{
	struct node *head;
};

struct ll *initializeLL(void *data)
{

	struct node *head = (struct node *)malloc(sizeof(struct node));
	struct ll *list = (struct ll *) malloc(sizeof(struct ll));

	head->data = data;
	head->next = NULL;

	list->head = head;

	return list;
}

void push(struct ll *list, void *data)
{
	struct node *head = (struct node *)malloc(sizeof(struct node));
	head->data = data;
	head->next = list->head;
	list->head = head;
}

void printLL(struct ll *list)
{
	struct node *head = list->head;

	while (head != NULL)
	{
		printf("%d\n",*((int*)(head->data)));
		head = head->next;
	}
}

void reverse(struct ll *list)
{
	struct node *last = NULL;
	struct node *head = list->head;

	while(head!=NULL)
	{
		struct node *temp = head;
		head = head->next;
		temp->next = last;
		last = temp;
	}
	list->head = last;
}

int main()
{
	int a[10];
	{
		int count = 0;
		for(count = 0; count < 10; count++)	a[count] = count;
	}
	struct ll *list = initializeLL((void *)(&a[0]));

	{
		int count = 1;
		for(count = 1; count < 10; count++) push(list,(void *)(&a[count]));
	}
	printLL(list);
	reverse(list);
	printLL(list);
	return 1;
}
