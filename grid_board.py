
import pygame

from model.a_star import PathFinder
from model.board import Board
import threading

BACKGROUND_COLOR = (81, 162, 0)


# obtener la posicion del mouse en la cuadricula
def __map_mouse_to_grid():
    pos = pygame.mouse.get_pos()
    x_column = pos[0] // WIDTH
    y_row = pos[1] // HEIGHT
    return [x_column, y_row]


# Dimensiones de cada sprite
WIDTH = 32
HEIGHT = 32

board = Board()
path_finder = PathFinder(board)


pygame.init()

WINDOW_SIZE = [board.get_width() * WIDTH, board.get_height() * HEIGHT]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_icon(pygame.image.load("resources/goal.png"))
pygame.display.set_caption("Algoritmo A*")

done = False
clock = pygame.time.Clock()
seconds = 0
pygame.time.set_timer(pygame.USEREVENT+1, 1000)
while not done:
    for event in pygame.event.get():
        x, y = __map_mouse_to_grid()
        modifier_pressed = pygame.key.get_mods()
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.MOUSEMOTION:
            print(pygame.key.get_mods())
            if pygame.mouse.get_pressed()[0] and modifier_pressed == pygame.KMOD_LCTRL:
                board.set_at(x, y, board.WALL)
            if pygame.mouse.get_pressed()[0] and modifier_pressed == pygame.KMOD_LALT:
                board.set_at(x, y, board.GROUND)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0] and modifier_pressed == pygame.KMOD_NONE:
                board.set_at(x, y, board.START)
            elif pygame.mouse.get_pressed()[2] and modifier_pressed == pygame.KMOD_NONE:
                board.set_at(x, y, board.END)

# hace un evento custom cada segundo
  #      if event.type == pygame.USEREVENT+1:
   #         seconds += 1
    #        # pathfinder.next_step
     #       print(seconds)

    screen.fill(BACKGROUND_COLOR)

    for row_index in range(board.get_width()):
        for column_index in range(board.get_height()):

            sprite = pygame.image.load("resources/ground.png").convert()

            if board.get_at(row_index, column_index) == board.START:
                sprite = pygame.image.load("resources/seeker.png")
            if board.get_at(row_index, column_index) == board.END:
                sprite = pygame.image.load("resources/goal.png")
            if board.get_at(row_index, column_index) == board.WALL:
                sprite = pygame.image.load("resources/wall.png")
            if board.get_at(row_index, column_index) == board.STEP:
                sprite = pygame.image.load("resources/step.png")
            if board.get_at(row_index, column_index) == board.PATH:
                sprite = pygame.image.load("resources/path.png")

            sprite_rect = sprite.get_rect()
            sprite_rect.move_ip(WIDTH * row_index, HEIGHT * column_index)
            screen.blit(sprite, sprite_rect)

    # Limitar a 60 fps
    clock.tick(60)

    pygame.display.flip()

pygame.quit()
