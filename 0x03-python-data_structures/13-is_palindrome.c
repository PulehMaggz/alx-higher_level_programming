#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse_list - Reverses a linked list
 * @head: Pointer to pointer to the head of the list
 * Return: Pointer to the new head of the reversed list
 */
listint_t *reverse_list(listint_t **head)
{
    listint_t *prev = NULL;
    listint_t *current = *head;
    listint_t *next = NULL;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    *head = prev;
    return *head;
}

/**
 * is_palindrome - Checks if a linked list is a palindrome
 * @head: Pointer to pointer to the head of the list
 * Return: 1 if the list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head, *fast = *head;
    listint_t *second_half, *prev_of_slow = NULL;
    int result = 1;

    if (*head == NULL || (*head)->next == NULL)
        return 1;

    /* Find the middle of the list */
    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        prev_of_slow = slow;
        slow = slow->next;
    }

    /* If the list has odd number of nodes, then move slow pointer one step further */
    if (fast != NULL)
    {
        second_half = slow->next;
    }
    else
    {
        second_half = slow;
    }
    prev_of_slow->next = NULL; // Terminate the first half

    /* Reverse the second half and compare */
    second_half = reverse_list(&second_half);
    listint_t *first_half = *head;

    while (second_half != NULL)
    {
        if (first_half->n != second_half->n)
        {
            result = 0;
            break;
        }
        first_half = first_half->next;
        second_half = second_half->next;
    }

    /* Restore the original list (optional) */
    second_half = reverse_list(&second_half);
    if (fast != NULL)
    {
        prev_of_slow->next = slow;
    }

    return result;
}
