#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle and 0 if it has no cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *f1 = list;
	listint_t *f2 = list;

	if (list == NULL)
		return (0);

	while (f1 && f2 && f2->next)
	{
		f1 = f1->next;
		f2 = f2->next->next;
		if (f1 == f2)
			return (1);
	}

	return (0);
}
