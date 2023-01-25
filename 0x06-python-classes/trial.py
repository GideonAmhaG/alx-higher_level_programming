#!/usr/bin/python3
""" Module: Node class and SinglyLnkedList class """


class Node:
    """ Node class """
    def __init__(self, data, next_node=None):
        """ Initilize function """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ Getter function """
        return self.__data

    @data.setter
    def data(self, data):
        """ Setter function """
        if type(data) is not int:
            raise TypeError("data must be an integer")
        self.__data = data

    @property
    def next_node(self):
        """ Getter function """
        return self.__next_node

    @next_node.setter
    def next_node(self, next_node):
        """ Setter function """
        if next_node is not None and type(next_node) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node


class SinglyLinkedList:
    """ SinglyLinkedList class: Inserts and prints """
    def __init__(self):
        """ Initilize function """
        self.__head = None

    def sorted_insert(self, value):
        """ Inserts a new Node into the correct sorted position in the
        list (increasing order) """
        new = Node(value, None)
        current = self.__head
        is_start = False
        if not self.__head:
            self.__head = new
        else:
            if value < self.__head.data:
                is_start = True
            while current.next_node and value > current.next_node.data\
                    and not is_start:
                current = current.next_node
            if not is_start:
                new.next_node = current.next_node
                current.next_node = new
            else:
                new.next_node = current
                self.__head = new

    def __str__(self):
        """ Enables calling a print on a SinglyLinkedList object """
        s = ""
        current = self.__head
        while current:
            s += str(current.data) + "\n"
            current = current.next_node
        return s
