
import pygame

from model.a_star import PathFinder
from model.board import Board
import threading

BACKGROUND_COLOR = (81, 162, 0)


def __map_mouse_to_grid():
    pos = pygame.mouse.get_pos()
    x_column = pos[0] // WIDTH
    y_row = pos[1] // HEIGHT
    return [x_column, y_row]


# Dimensiones de cada sprite
WIDTH = 32
HEIGHT = 32


path_finder = PathFinder(Board())
board = path_finder.get_board()

pygame.init()

WINDOW_SIZE = [board.get_width() * WIDTH, board.get_height() * HEIGHT]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_icon(pygame.image.load("resources/goal.png"))

GROUND = pygame.image.load("resources/ground.png")
SEEKER_IMG = pygame.image.load("resources/seeker.png")
GOAL_IMG = pygame.image.load("resources/goal.png")
WALL_IMG = pygame.image.load("resources/wall.png")
NODE_OPEN_IMG = pygame.image.load("resources/node_open.png")
NODE_CLOSED_IMG = pygame.image.load("resources/node_closed.png")
PATH_IMG = pygame.image.load("resources/path.png")

pygame.display.set_caption("Algoritmo A*")

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        x, y = __map_mouse_to_grid()
        modifier_pressed = pygame.key.get_mods()

        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[0] and modifier_pressed == pygame.KMOD_LCTRL:
                board.set_at(x, y, board.WALL)
            if pygame.mouse.get_pressed()[0] and modifier_pressed == pygame.KMOD_LALT:
                board.set_at(x, y, board.GROUND)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0] and modifier_pressed == pygame.KMOD_NONE:
                path_finder.set_initial_position(x, y)
            elif pygame.mouse.get_pressed()[2] and modifier_pressed == pygame.KMOD_NONE:
                path_finder.set_goal(x, y)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                pygame.time.set_timer(pygame.USEREVENT + 1, 100)

        if event.type == pygame.USEREVENT+1:
            path_finder.next_step()

    screen.fill(BACKGROUND_COLOR)

    for row_index in range(board.get_width()):
        for column_index in range(board.get_height()):

            if board.get_at(row_index, column_index) == board.START:
                sprite = SEEKER_IMG
            elif board.get_at(row_index, column_index) == board.END:
                sprite = GOAL_IMG
            elif board.get_at(row_index, column_index) == board.WALL:
                sprite = WALL_IMG
            elif board.get_at(row_index, column_index) == board.NODE_OPEN:
                sprite = NODE_OPEN_IMG
            elif board.get_at(row_index, column_index) == board.NODE_CLOSED:
                sprite = NODE_CLOSED_IMG
            elif board.get_at(row_index, column_index) == board.PATH:
                sprite = PATH_IMG
            else:
                sprite = GROUND

            sprite_rect = sprite.get_rect()
            sprite_rect.move_ip(WIDTH * row_index, HEIGHT * column_index)
            screen.blit(sprite, sprite_rect)

    # Limitar a 60 fps
    clock.tick(60)

    pygame.display.flip()

pygame.quit()
