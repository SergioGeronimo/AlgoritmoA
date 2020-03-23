import math
from model.board import Board
from operator import attrgetter

DEFAULT_COST = 10


class Node:
    def __init__(self, parent_node, position, goal_position):
        self.wall = False
        self.open = False
        self.parent_node = parent_node
        self.pos_x = position[0]
        self.pos_y = position[1]
        self.children_nodes = []
        self.global_cost = 0
        self.local_cost = 0
        self.__calculate_costs(goal_position)
        self.total_cost = self.global_cost + self.local_cost

    def __calculate_costs(self, goal_position):
        if self.wall:
            self.global_cost = 10000
            self.local_cost = 10000
        else:
            if self.parent_node is not None:
                self.local_cost = self.parent_node.local_cost + DEFAULT_COST

            square_x = math.pow(goal_position[0] - self.pos_x, 2) * DEFAULT_COST
            square_y = math.pow(goal_position[1] - self.pos_y, 2) * DEFAULT_COST
            self.global_cost = math.trunc(math.sqrt(square_x + square_y))

    def get_total_cost(self):
        return self.global_cost + self.local_cost

    def set_children(self, children: list):
        self.children_nodes.extend(children)

    def __eq__(self, other):
        attributes = ("pos_x", "pos_y")
        return attrgetter(*attributes)(self) == attrgetter(*attributes)(other)

    def set_wall(self, value):
        self.wall = value

    def get_path_root(self):

        if self.parent_node is None:
            return [self]
        else:
            path = [self]
            path.extend(self.parent_node.get_path_root())
            return path


class PathFinder:
    def __init__(self, board, initial_position=None, goal_position=None):
        if initial_position is None:
            initial_position = [0, 0]
        if goal_position is None:
            goal_position = [board.get_width() - 1, board.get_height() - 1]

        self.root = Node(None, initial_position, goal_position)
        self.__initial_position = initial_position
        self.__goal_position = goal_position
        self.__open_nodes = [self.root]
        self.__closed_nodes = []
        self.__wall_nodes = []
        self.__path = []
        self.__board = board
        self.__update_all_board()

    def get_board(self):
        return self.__board

    def create_node_neighbors(self, node: Node) -> list:
        self.__board.get_height()

        node_neighbors = []
        positions = [[node.pos_x, node.pos_y - 1],
                     [node.pos_x - 1, node.pos_y],
                     [node.pos_x, node.pos_y + 1],
                     [node.pos_x + 1, node.pos_y]]
        for position in positions:
            if 0 <= position[0] < self.__board.get_width():
                if 0 <= position[1] < self.__board.get_height():
                    next_node = Node(node, position, self.__goal_position)
                    if self.__board.get_at(next_node.pos_x, next_node.pos_y) == Board.WALL:
                        next_node.set_wall(True)
                    if next_node not in self.__closed_nodes and next_node not in self.__open_nodes:
                        if next_node not in self.__wall_nodes:
                            node_neighbors.append(next_node)

        return node_neighbors

    def __update_all_board(self):
        # self.__board.fill_board(Board.GROUND)
        self.__board.set_for_all_nodes(self.__open_nodes, Board.NODE_OPEN)
        self.__board.set_for_all_nodes(self.__closed_nodes, Board.NODE_CLOSED)
        self.__board.set_for_all_nodes(self.__wall_nodes, Board.WALL)
        self.__board.set_for_all_nodes(self.__path, Board.PATH)
        self.__board.set_at(self.__initial_position[0], self.__initial_position[1], Board.START)
        self.__board.set_at(self.__goal_position[0], self.__goal_position[1], Board.END)

    def set_initial_position(self, x, y):
        self.__board.set_at(self.__initial_position[0], self.__initial_position[1], Board.GROUND)
        self.__initial_position = [x, y]
        self.__board.set_at(self.__initial_position[0], self.__initial_position[1], Board.START)

    def set_goal(self, x, y):
        self.__board.set_at(self.__goal_position[0], self.__goal_position[1], Board.GROUND)
        self.__goal_position = [x, y]
        self.__board.set_at(self.__goal_position[0], self.__goal_position[1], Board.END)

    def next_step(self):
        try:
            min_node = min(self.__open_nodes, key=attrgetter("total_cost", "local_cost"))
        except ValueError:
            # print("No more open nodes")
            pass
        else:
            self.__open_nodes.remove(min_node)
            self.__closed_nodes.append(min_node)
            if min_node.global_cost == 0:
                self.__path = min_node.get_path_root()
                print(self.__path)
            else:
                children_nodes = self.create_node_neighbors(min_node)
                min_node.set_children(children_nodes)
                for child in children_nodes:
                    if child.wall:
                        self.__wall_nodes.append(child)
                    else:
                        self.__open_nodes.append(child)

            self.__update_all_board()
