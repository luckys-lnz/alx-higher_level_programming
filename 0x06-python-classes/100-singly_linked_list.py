class Node:
    def __init__(self, data, next_node=None):

        """Checks if data is integer"""
        if not isinstance(data, int):
            raise TypeError("data must be an integer")

        """Checks if next_node is either None or Node object"""
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
    def data(self, num):

        """Check if the new num is an integer"""
        if not isinstance(num, int):
            raise TypeError("data must be an integer")
        self.__data = num

    """Property and setter for next_node"""
    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, num):

        """Checks if new num is None or Node object"""
        if num is not None and not isinstance(num, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = num


class SinglyLinkedList:
    def __init__(self):

        """Initializing a singly linked list with head (starting node)"""
        self.__head = None

    def sorted_insert(self, num):

        """Created a new node with the given num"""
        new_node = Node(num)

        """
        If list is empty or the new num is smaller than the current head,
        put the new node at the beginning of the list
        """

        if self.__head is None or num < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:

            """
            Find the correct position to insert the new node while maintaining
            the sorted order of the linked list
            """
            current = self.__head
            while current.next_node is not None and current.next_node.data < num:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Generated a string to represent the linked list"""
        result = []
        current = self.__head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return '\n'.join(result)
