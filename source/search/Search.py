__author__ = 'mesfinmebrate'

def graph_search(problem, fringe, strategy):

    closed = []
    fringe = insert(problem, fringe)
    solution = []

    while fringe.count() > 0:

        node = get_next(fringe, strategy)

        if goal_test(problem, node):
            solution.append(node)
            return solution

        if node.get_data() not in closed:
            closed.append(node.get_data())

            for child_node in expand(node):
                fringe = insert(child_node, fringe)

    else:
        return None


def insert(node, fringe):
    fringe.append(node)
    return fringe

def get_next(fringe, strategy):
    return strategy(fringe)

def goal_test(problem, node):
    return problem.goal_test(node)

def expand(node, problem):
    node.get_vertices()
