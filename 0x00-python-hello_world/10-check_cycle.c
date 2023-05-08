#include "lists.h"
/**
 * check_cycle - Check if a loop exists in the linked list
 * @list: Is the pointer to the head of the linked list
 * Return: 1 if a loop exists or 0 if it does not
 */
int check_cycle(listint_t *list)
{
	listint_t *slow_p = list;
	listint_t *fast_p = list;

	while (slow_p != NULL && fast_p != NULL && fast_p->next != NULL)
	{
		slow_p = slow_p->next;
		fast_p = fast_p->next->next;

		if (slow_p == fast_p)
			return (1);
	}

	return (0);
}

