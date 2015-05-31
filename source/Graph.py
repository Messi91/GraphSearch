__author__ = 'mesfinmebrate'

class Node:

    def __init__(self, data, is_goal=False):
        self.__data = data
        self.__vertices = {}
        self.__is_goal = is_goal

    def get_data(self):
        return self.__data

    def get_vertices(self):
        return self.__vertices

    def get_vertex(self, data):
        return self.__vertices[data]

    def set_vertices(self, new_vertices):
        self.__vertices = new_vertices



if __name__ == "__main__":

    s = Node("S")
    a = Node("A")
    b = Node("B")
    c = Node("C")
    g = Node("G", is_goal=True)

    s.set_vertices({"A": a, "B": b, "C": c})
    s.get_vertex("A").set_vertices({"B": b, "C": c})
    s.get_vertex("C").set_vertices({"G": g})
