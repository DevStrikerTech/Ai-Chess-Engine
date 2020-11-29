import pygame
from chess.variable_declaration import board_width, board_height

FPS: int = 60
window = pygame.display.set_mode((board_width, board_height))
pygame.display.set_caption('Chess Engine')


def main():
    start_chess_engine = True
    runtime = pygame.time.Clock()

    while start_chess_engine:
        runtime.tick(FPS)
        pass


main()
