#include "lists.h"

/**
 * check_cycle - checks if there is loop/cycle in a linked list
 * @list: pointer to head node of the linked list
 *
 * Return: 0 if no loop, 1 if there is loop
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = list, *slow = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
