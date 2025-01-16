#!/usr/bin/python3
"""Defines a node of a singly linked list and the singly linked list itself."""

class Node:
    """Represents a node in a singly linked list."""
    
    def __init__(self, data, next_node=None):
        """Initializes a new node.
        
        Args:
            data (int): The data for the new node.
            next_node (Node): The next node in the list. Defaults to None.
        """
        self.data = data
        self.next_node = next_node
    
    @property
    def data(self):
        """Gets the data of the node."""
        return self.__data
    
    @data.setter
    def data(self, value):
        """Sets the data of the node with validation.
        
        Args:
            value (int): The data to set.
        
        Raises:
            TypeError: If data is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value
    
    @property
    def next_node(self):
        """Gets the next node."""
        return self.__next_node
    
    @next_node.setter
    def next_node(self, value):
        """Sets the next node with validation.
        
        Args:
            value (Node): The next node to set.
        
        Raises:
            TypeError: If next_node is not a Node or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly linked list."""
    
    def __init__(self):
        """Initializes an empty singly linked list."""
        self.head = None
    
    def __str__(self):
        """Returns a string representation of the list."""
        nodes = []
        current_node = self.head
        while current_node:
            nodes.append(str(current_node.data))
            current_node = current_node.next_node
        return "\n".join(nodes)
    
    def sorted_insert(self, value):
        """Inserts a new node with the given value into the sorted list.
        
        Args:
            value (int): The value to insert into the list.
        """
        new_node = Node(value)
        if not self.head or self.head.data >= value:
            # Insert at the beginning of the list
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node and current.next_node.data < value:
                current = current.next_node
            # Insert the new node after the current node
            new_node.next_node = current.next_node
            current.next_node = new_node
