import pygame
from .variable_declaration import board_white_square, board_rows, board_brown_square, board_square_size, board_columns, \
    white_piece, black_piece
from .piece import Piece


class Board:
    def __init__(self):
        self.board = []
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

    def evaluate(self):
        return self.white_piece_left - self.black_piece_left + \
               (self.white_piece_kings * 0.5 - self.black_piece_kings * 0.5)

    def move_pieces(self, piece, board_row, board_column):
        self.board[piece.board_row][piece.board_column], self.board[board_row][board_column] = \
            self.board[board_row][board_column], self.board[piece.board_row][piece.board_column]
        piece.move_pieces(board_row, board_column)

        if board_row == board_rows - 1 or board_row == 0:
            piece.make_king()

            if piece.piece_color == white_piece:
                self.white_piece_kings += 1
            else:
                self.black_piece_kings += 1

    def get_pieces(self, board_row, board_column):
        return self.board[board_row][board_column]

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

    def draw_pieces(self, window):
        self.draw_squares(window)
        for board_row in range(board_rows):
            for board_column in range(board_columns):
                chess_piece = self.board[board_row][board_column]
                if chess_piece != 0:
                    chess_piece.draw_pieces(window)

    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.board_row][piece.board_column] = 0

            if piece != 0:
                if piece.piece_color == black_piece:
                    self.black_piece_left -= 1
                else:
                    self.white_piece_left -= 1

    def winner(self):
        if self.black_piece_left <= 0:
            return white_piece
        elif self.white_piece_left <= 0:
            return black_piece

        return None

    def get_logical_moves(self, piece):
        moves = {}
        left = piece.board_column - 1
        right = piece.board_column + 1
        row = piece.board_row

        if piece.piece_color == black_piece or piece.piece_king:
            moves.update(self._traverse_left(row - 1, max(row - 3, -1), -1, piece.piece_color, left))
            moves.update(self._traverse_right(row - 1, max(row - 3, -1), -1, piece.piece_color, right))

        if piece.piece_color == white_piece or piece.piece_king:
            moves.update(self._traverse_left(row + 1, min(row + 3, board_rows), 1, piece.piece_color, left))
            moves.update(self._traverse_right(row + 1, min(row + 3, board_rows), 1, piece.piece_color, right))

        return moves

    def _traverse_left(self, start, stop, step, piece_color, left, skipped=[]):
        moves = {}
        last = []

        for index in range(start, stop, step):
            if left < 0:
                break

            current = self.board[index][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(index, left)] = last + skipped
                else:
                    moves[(index, left)] = last

                if last:
                    if step == -1:
                        board_row = max(index - 3, 0)
                    else:
                        board_row = min(index + 3, board_rows)

                    moves.update(self._traverse_left(index + step, board_row,
                                                     step, piece_color, left - 1, skipped=last))
                    moves.update(self._traverse_right(index + step, board_row,
                                                      step, piece_color, left + 1, skipped=last))
                break

            elif current.piece_color == piece_color:
                break

            else:
                last = [current]

            left -= 1

        return moves

    def _traverse_right(self, start, stop, step, piece_color, right, skipped=[]):
        moves = {}
        last = []

        for index in range(start, stop, step):
            if right >= board_columns:
                break

            current = self.board[index][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(index, right)] = last + skipped
                else:
                    moves[(index, right)] = last

                if last:
                    if step == -1:
                        board_row = max(index - 3, 0)
                    else:
                        board_row = min(index + 3, board_rows)

                    moves.update(self._traverse_left(index + step, board_row,
                                                     step, piece_color, right - 1, skipped=last))
                    moves.update(self._traverse_right(index + step, board_row,
                                                      step, piece_color, right + 1, skipped=last))
                break

            elif current.piece_color == piece_color:
                break

            else:
                last = [current]

            right += 1

        return moves
