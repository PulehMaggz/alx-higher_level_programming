#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to the pointer of the head node
 * @number: number to be inserted
 * Return: address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new, *current, *previous;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    new->n = number;
    new->next = NULL;

    /* Case 1: Inserting into an empty list */
    if (*head == NULL)
    {
        *head = new;
        return (new);
    }

    current = *head;
    previous = NULL;

    /* Case 2: Inserting at the beginning */
    if (number < current->n)
    {
        new->next = current;
        *head = new;
        return (new);
    }

    /* Case 3: Inserting in the middle or end */
    while (current != NULL && current->n < number)
    {
        previous = current;
        current = current->next;
    }

    previous->next = new;
    new->next = current;

    return (new);
}
