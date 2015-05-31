__author__ = 'mesfinmebrate'

from graph import graph

def main():

    s = graph.Node("S")
    a = graph.Node("A")
    b = graph.Node("B")
    c = graph.Node("C")
    g = graph.Node("G")

    s.add_vertex(a)
    s.add_vertex(b)
    s.add_vertex(c)
    s.get_vertex("A").add_vertex(b)
    s.get_vertex("A").add_vertex(c)
    s.get_vertex("C").add_vertex(g)

    print "A"


if __name__ == "__main__":

    main()
