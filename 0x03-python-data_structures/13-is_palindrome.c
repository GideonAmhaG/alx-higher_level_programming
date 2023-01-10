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
		  *left = *head, *right, *second_list, *prev = NULL;

	if (head == NULL || *head == NULL)
		return (1);

	while (fast && fast->next)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}
	if (fast)
		slow = slow->next;
	second_list = slow;
	prev_slow->next = NULL;
	while (second_list)
	{
		tmp = second_list->next;
		second_list->next = prev;
		prev = second_list;
		second_list = tmp;
	}
	right = prev;
	while (left && right)
	{
		if (left->n != right->n)
			return (0);
		left = left->next;
		right = right->next;
	}
	return (1);
}
