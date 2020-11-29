import pygame
from chess.board import Board
from .variable_declaration import black_piece, white_piece, position_piece, board_square_size


class Rules:
    def __init__(self, window):
        self._init()
        self.window = window

    def update(self):
        self.chess_board.draw_pieces(self.window)
        self.draw_valid_moves(self.logical_moves)
        pygame.display.update()

    def _init(self):
        self.current_piece = None
        self.chess_board = Board()
        self.turn_taken = black_piece
        self.logical_moves = {}

    def winner(self):
        return self.chess_board.winner()

    def reset(self):
        self._init()

    def select(self, board_row, board_column):
        if self.current_piece:
            result = self._move(board_row, board_column)

            if not result:
                self.current_piece = None
                self.select(board_row, board_column)

        piece = self.chess_board.get_pieces(board_row, board_column)

        if piece != 0 and piece.piece_color == self.turn_taken:
            self.current_piece = piece
            self.logical_moves = self.chess_board.get_logical_moves(piece)
            return True

        return False

    def _move(self, board_row, board_column):
        piece = self.chess_board.get_pieces(board_row, board_column)

        if self.current_piece and piece == 0 and (board_row, board_column) in self.logical_moves:
            self.chess_board.move_pieces(self.current_piece, board_row, board_column)
            skipped = self.logical_moves[(board_row, board_column)]

            if skipped:
                self.chess_board.remove(skipped)

            self.change_turn()

        else:
            return False

        return True

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.window, position_piece,
                               (col * board_square_size + board_square_size // 2,
                                row * board_square_size + board_square_size // 2), 15)

    def change_turn(self):
        self.logical_moves = {}

        if self.turn_taken == black_piece:
            self.turn_taken = white_piece
        else:
            self.turn_taken = black_piece
