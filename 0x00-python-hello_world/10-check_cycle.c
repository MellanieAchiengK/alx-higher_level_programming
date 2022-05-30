#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks list
 * @list: list being checked
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *n;
	listint_t *t;

	if (list == NULL)
		return (0);
	n = list;
	t = list;

	while (n && t && t->next)

	{
		n = n->next;
		t = t->next->next;
		if (n == t)
		return (1);
	}
	return (0);
}
