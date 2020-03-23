class Board:
    GROUND = 0
    START = 1
    END = 2
    WALL = 3
    NODE_OPEN = 4
    NODE_CLOSED = 6
    PATH = 5

    def __init__(self, width=10, height=10, initial_value=0):
        self.__grid = self.__create_grid(width, height, initial_value)


    @staticmethod
    def __create_grid(width, height, initial_value):
        grid = []
        for column in range(height):
            grid.append([])
            for row in range(width):
                grid[column].append(initial_value)

        return grid

    def get_height(self):
        return len(self.__grid)

    def get_width(self):
        return len(self.__grid[0])

    def set_at(self, row, column, value):
        self.__grid[column][row] = value

    def get_at(self, row, column):
        return self.__grid[column][row]

    def fill_board(self, empty_symbol):
        for row in self.__grid:
            for column in range(len(row)):
                row[column] = empty_symbol

    def set_for_all_nodes(self, nodes, value):
        for node in nodes:
            self.__grid[node.pos_x][node.pos_y] = value

    def print_board(self):
        for row in self.__grid:
            for element in row:
                print(element, end=" ")
            print()


"""
recordatorio: crear getters y setters de la forma pythonica
class P:

    def __init__(self,x):
        self.x = x

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x
"""
