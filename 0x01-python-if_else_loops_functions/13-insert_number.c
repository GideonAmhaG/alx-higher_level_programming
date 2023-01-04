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
	int i = 0;

	current = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	while (i < 4 && current->next != NULL)
	{
		current = current->next;
		i++;
	}
	new->next = current->next;
	current->next = new;
	return (new);
}
