__author__ = 'mesfinmebrate'

from model import model

def main():

    s, a, b, c, g = "S", "A", "B", "C", "G"

    graph = model.Graph()
    graph.add_edge(s, a)
    graph.add_edge(s, b)
    graph.add_edge(s, c)
    graph.add_edge(a, b)
    graph.add_edge(a, c)
    graph.add_edge(c, g)

    print graph.get_node(a)


if __name__ == "__main__":

    main()
