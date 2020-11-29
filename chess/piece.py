class Piece:
    def __init__(self, board_row, board_column, piece_color):
        self.board_row = board_row
        self.board_column = board_column
        self.piece_color = piece_color
        self.piece_king = False
        self.piece_direction = 1
