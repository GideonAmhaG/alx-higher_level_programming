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
        if next_node != None or type(next_node is not Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node

class SinglyLinkedList:
    """ SinglyLinkedList class: Inserts and prints """
    __head = Node()
    def __init__(self)
    def sorted_insert(self, value):
        """ Inserts a new Node into the correct sorted position in the
        list (increasing order) """
        new_node = Node(value, None)
        if __head == None:
            __head = new_node
        if value < __head.data:
            new_node.next_node = __head
            __head = new_node
        while True:
            if __head != None:

                __head = __head.next_node

            


            

