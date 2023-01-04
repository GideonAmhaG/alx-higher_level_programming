#include "lists.h"

/**
 *insert_node - inserts a node
 *@head: pointer to pointer of first node of listint_t list
 *@number: integer to be included in new node
 *
 *Return: address of the new element or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *new;

	if (head == NULL)
		return (NULL);
	current = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (current)
	{
		if (number <= current->n)
		{
			new->next = current;
			*head = new;
		}
		else
		{
			while (current->next != NULL && number > (current->next)->n)
				current = current->next;
			new->next = current->next;
			current->next = new;
		}
	}
	else
	{
		new->next = NULL;
		*head = new;
	}
	return (new);
}
