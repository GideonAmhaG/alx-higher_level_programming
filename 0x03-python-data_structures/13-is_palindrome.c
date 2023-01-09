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
	listint_t *rev, *current;

	if (head == NULL)
		return (1);

	if (*head == NULL)
		return (1);

	current = *head;
	rev = reverse_listint(head);
	while (current)
	{
		if (current->n != rev->n)
			return (0);
		current = current->next;
		rev = rev->next;
	}
	return (1);
}

/**
 * reverse_listint - reverses a listint_t linked list
 * @head: pointer to pointer to head node
 *
 * Return: a pointer to the first node of the reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *prev, *next, *current;

	if (*head == NULL || head == NULL)
		return (NULL);

	current = *head;
	prev = NULL;
	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
	return (*head);
}
