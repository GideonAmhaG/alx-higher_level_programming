#include "lists.h"

listint_t *reverse_listint(listint_t **head);

/**
 * is_palindrome - checks if the data of a linked list is a palindrome
 * @head: pointer to head node pointer
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *fast = *head, *slow = *head, *prev_slow = *head, *tmp,
		  *left = *head, *second, *prev = NULL;

	if (head == NULL)
		return (0);

	if (*head == NULL)
		return (1);

	while (fast && fast->next)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}
	if (fast)
	{
		slow = slow->next;
	}
	second = slow;
	prev_slow->next = NULL;
	while (second)
	{
		tmp = second->next;
		second->next = prev;
		prev = second;
		second = tmp;
	}
	while (left && prev)
	{
		if (left->n != prev->n)
			return (0);
		left = left->next;
		prev = prev->next;
	}
	return (1);
}
