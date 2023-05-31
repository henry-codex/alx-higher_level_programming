#!/usr/bin/python3
class Node:
    """Constructor to initialize the element"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter for data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter for data"""
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        else:
            self.__data = value

    @property
    def next_node(self):
        """Getter for next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter for next_node"""
        if value is not None and not isinstance(value, Node):
            raise TypeError('next_node must be a Node object')
        else:
            self.__next_node = value


class SinglyLinkedList:
    """Class for the single linked list"""
    def __init__(self):
        """Constructor to initialize this object"""
        self.__head = None

    def sorted_insert(self, value):
        """Function to handle the single linked list"""
        if self.__head is not None:
            node_data = Node(value)
            node_data.data = value
            node_data.next_node = self.__head
            self.__head = node_data
        else:
            node_data = Node(value, None)
            node_data.data = value
            node_data.next_node = self.__head
            self.__head = node_data

    def __str__(self):
        """String representation of the linked list"""
        result = self.__head
        show_list = []

        while result is not None:
            show_list.append(str(result.data))
            result = result.next_node
        show_list.sort(key=int)
        return '\n'.join(show_list)

