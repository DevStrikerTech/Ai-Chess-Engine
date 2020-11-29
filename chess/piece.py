import pygame
from .variable_declaration import black_piece, white_piece, board_square_size, highlight_piece_grey


class Piece:
    # Inner padding for chess pieces
    padding: int = 10
    outline: int = 2

    def __init__(self, board_row, board_column, piece_color):
        self.board_row = board_row
        self.board_column = board_column
        self.piece_color = piece_color
        self.piece_king = False

        # Chess piece position check by piece color
        if self.piece_color == black_piece:
            self.piece_direction = -1
        else:
            self.piece_direction = 1

        self.x = 0
        self.y = 0
        self.calculate_piece_position()

    def calculate_piece_position(self):
        self.x = board_square_size * self.board_column + board_square_size // 2
        self.y = board_square_size * self.board_row + board_square_size // 2

    def make_king(self):
        self.piece_king = True

    def draw(self, window):
        radius = board_square_size // 2 - self.padding
        pygame.draw.circle(window, highlight_piece_grey, (self.x, self.y), radius + self.outline)
        pygame.draw.circle(window, self.piece_color, (self.x, self.y), radius)

    def __repr__(self):
        return str(self.piece_color)
