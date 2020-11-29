import pygame
from .variable_declaration import board_white_square, board_rows, board_brown_square, board_square_size


class Board:
    def __init__(self):
        self.board = []
        self.current_piece = None
        self.black_piece_left = self.white_piece_left = 12
        self.black_piece_kings = self.white_piece_kings = 0

    def draw_squares(self, window):
        window.fill(board_white_square)
        for board_row in range(board_rows):
            for board_column in range(board_row % 2, board_rows, 2):
                pygame.draw.rect(window, board_brown_square, (board_row*board_square_size,
                                                              board_column*board_square_size,
                                                              board_square_size, board_square_size))
