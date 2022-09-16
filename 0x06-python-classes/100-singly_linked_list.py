#!/usr/bin/python3
"""A class that implements a singly linked list"""

class Node:
    """A class Node that defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """
        PARAMETERS
        data:
            1. an integer, otherwise raise a TypeError exception with the message data must be an integer
        next_node: 
            None or a Node, otherwise raise a TypeError exception with the message next_node must be a Node object
        """
        
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Function that get the data of the node"""
        
        return (self.__data)

    @data.setter
    def data(self, value):
        """Function that set the data of the node"""
        
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Function that get the data of the node"""
        
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """Function that set the data of the node"""
        
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """A class SinglyLinkedList that defines a singly linked list"""

    def __init__(self):
        """Simple instantiation"""
        
        self.__head = None

    def sorted_insert(self, value):
        """
        Function that inserts a new Node into the correct sorted position in the list (increasing order)
        """
        
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Function that defines printing the list"""
        
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
