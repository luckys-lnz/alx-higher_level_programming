#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        """Check if data is an integer"""
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        """Check if next_node is either None or a Node object"""
        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        
        """Initialize private instance attributes"""
        self.__data = data
        self.__next_node = next_node

    """Property and setter for data"""
    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        """Check if the new value is an integer"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    """Property and setter for next_node"""
    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Check if the new value is None or a Node object"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        """Initialize a singly linked list with a head (starting node)"""
        self.__head = None

    def sorted_insert(self, value):
        """Create a new node with the given value"""
        new_node = Node(value)

        """
        If the list is empty or the new value is smaller than the current head,
        insert the new node at the beginning of the list
        """

        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            """
            Find the correct position to insert the new node while maintaining
            the sorted order of the linked list
            """
            current = self.__head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Generate a string representation of the linked list"""
        result = []
        current = self.__head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return '\n'.join(result)
