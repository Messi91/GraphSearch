__author__ = 'mesfinmebrate'

class Problem:

    def __init__(self, states, initial_state, goal_test):
        self.__states = states
        self.initial_state = initial_state
        self.__goal_test = goal_test

    def goal_test(self):
        self.__goal_test

    def initial_state(self):
        self.__states.get_node(self.initial_state)
