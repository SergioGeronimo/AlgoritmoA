import math

from model.board import Board

DEFAULT_COST = 10


class Node:
    def __init__(self, parent_node, position, goal_position):
        self.__wall = False
        self.__open = False
        self.__parent_node = parent_node
        self.__children_nodes = []
        self.__global_cost = 0
        self.__local_cost = 0
        self.__calculate_costs(self.__parent_node, position, goal_position)

    @staticmethod
    def __calculate_costs(self, parent_node, position, goal_position):
        if parent_node is not None:
            self.__local_cost = parent_node.get_costs[1] + DEFAULT_COST

        square_x = math.pow(goal_position[1] - position[1], 2) * DEFAULT_COST
        square_y = math.pow(goal_position[1] - position[1], 2) * DEFAULT_COST
        self.__global_cost = math.trunc(math.sqrt(square_x + square_y))

    def get_costs(self):
        all_cost = self.__global_cost = self.__local_cost
        return [self.__global_cost, self.__local_cost, all_cost]

    def add_child(self, node):
        self.__children_nodes.append(node)

    def get_children(self):
        return self.__children_nodes

    def get_parent(self):
        return self.__parent_node


class PathFinder:
    def __init__(self, board, initial_position=None, goal_position=None):
        if goal_position is None:
            goal_position = []
        if initial_position is None:
            initial_position = [0, 0]
        self.initial_position = initial_position
        self.__goal_position = goal_position
        self.__selected_path_nodes = [Node(None)]
        self.__path_nodes = []
        self.__board = board

    def get_board(self):
        return self.__board

    def start(self):
        pass
