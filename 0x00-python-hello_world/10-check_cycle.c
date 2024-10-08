#include "lists.h"

/**
 * check_cycle - checks if a linked list has a cycle
 * @list: pointer to the head of the list
 * Return: 1 if there is a cycle, 0 if there is no cycle
 */
int check_cycle(listint_t *list)
{
listint_t *tortoise = list;
listint_t *hare = list;

while (hare != NULL && hare->next != NULL)
{
tortoise = tortoise->next;
hare = hare->next->next;

if (tortoise == hare)
{
return (1); /* Cycle detected */
}
}

return (0); /* No cycle */
}
