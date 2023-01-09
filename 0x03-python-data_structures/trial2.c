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
	listint_t *fast = *head, *slow = *head, *prev = NULL, *tmp,
		  *left = *head, *right;

	if (head == NULL)
		return (0);

	if (*head == NULL)
		return (1);

	while (fast && fast->next)
	{
		fast = fast->next->next;
		slow = slow->next;
	}
	while (slow)
	{
		tmp = slow->next;
		slow->next = prev;
		prev = slow;
		slow = tmp;
	}
	right = prev;
	while (right)
	{
		if (left->n != right->n)
			return (0);
		left = left->next;
		right = right->next;
	}
	return (0);
}
