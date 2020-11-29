import pygame
from .variable_declaration import board_white_square, board_rows, board_brown_square, board_square_size, board_columns,\
    white_piece, black_piece
from .piece import Piece


class Board:
    def __init__(self):
        self.board = []
        self.current_piece = None
        self.black_piece_left = self.white_piece_left = 12
        self.black_piece_kings = self.white_piece_kings = 0
        self.create_board()

    def draw_squares(self, window):
        window.fill(board_white_square)
        for board_row in range(board_rows):
            for board_column in range(board_row % 2, board_columns, 2):
                pygame.draw.rect(window, board_brown_square, (board_row * board_square_size,
                                                              board_column * board_square_size,
                                                              board_square_size, board_square_size))

    def create_board(self):
        for board_row in range(board_rows):
            self.board.append([])
            for board_column in range(board_columns):
                if board_column % 2 == ((board_row + 1) % 2):
                    if board_row < 3:
                        self.board[board_row].append(Piece(board_row, board_column, white_piece))
                    elif board_row > 4:
                        self.board[board_row].append(Piece(board_row, board_column, black_piece))
                    else:
                        self.board[board_row].append(0)
                else:
                    self.board[board_row].append(0)

    def draw(self, window):
        self.draw_squares(window)
        for board_row in range(board_rows):
            for board_column in range(board_columns):
                chess_piece = self.board[board_row][board_column]
                if chess_piece != 0:
                    chess_piece.draw(window)
