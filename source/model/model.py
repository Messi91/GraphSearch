__author__ = 'mesfinmebrate'


class Graph:

    def __init__(self):
        self.__nodes = {}
        self.__edges = {}

    def add_edge(self, data1, data2, cost = 0):
        node1 = self.__nodes[data1] if self.__nodes.has_key(data1) else Node(data1)
        node2 = self.__nodes[data2] if self.__nodes.has_key(data2) else Node(data2)
        self.__nodes[data1] = node1
        self.__nodes[data2] = node2
        self.__nodes[data1].add_vertex(node2)
        self.__nodes[data2].add_vertex(node1)
        self.__edges[(data1, data2)] = Edge(self.__nodes[data1], self.__nodes[data2], cost)

    def get_edge(self, data1, data2):
        return self.__edges[(data1, data2)] if self.__edges.has_key((data1, data2)) else None

    def get_edges(self):
        return self.__edges

    def get_node(self, name):
        return self.__nodes[name] if self.__edges.has_key(name) else None

class Node:

    def __init__(self, data):
        self.__data = data
        self.__vertices = {}

    def get_data(self):
        return self.__data

    def get_vertices(self):
        return self.__vertices

    def get_vertex(self, data):
        return self.__vertices[data] if self.__vertices.has_key(data) else None

    def add_vertex(self, new_vertex):
        if not self.__vertices.has_key(new_vertex.get_data()):
            self.__vertices[new_vertex.get_data()] = new_vertex

    def __str__(self):
        return self.__data


class Edge:

    def __init__(self, data1, data2, cost):
        self.__node1 = Node(data1)
        self.__node2 = Node(data2)
        self.__cost = cost

    def get_first_node(self):
        return self.__node1

    def get_second_node(self):
        return self.__node2

    def get_cost(self):
        return self.cost

    def __str__(self):
        return str(self.__node1.get_data()) + "<-->" + str(self.__node2.get_data())
