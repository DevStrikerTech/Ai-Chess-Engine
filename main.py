import pygame
from chess.variable_declaration import board_width, board_height

window = pygame.display.set_mode((board_width, board_height))
pygame.display.set_caption('Chess Engine')