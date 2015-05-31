__author__ = 'mesfinmebrate'

class Node:

    def __init__(self, data):
        self.__data = data
        self.__vertices = {}

    def get_data(self):
        return self.__data

    def get_vertices(self):
        return self.__vertices

    def get_vertex(self, data):
        return self.__vertices[data]

    def add_vertex(self, new_vertex):
        self.__vertices[new_vertex.get_data()] = new_vertex


class Edge:

    def __init__(self, data1, data2, cost = 0):
        self.__node1 = Node(data1)
        self.__node2 = Node(data2)
        self.__cost = cost

    def get_first_node(self):
        return self.__node1

    def get_second_node(self):
        return self.__node2

    def get_cost(self):
        return self.cost


class Graph:

    def __init__(self):
