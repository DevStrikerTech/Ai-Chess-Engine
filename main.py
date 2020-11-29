import pygame
from chess.variable_declaration import board_width, board_height, board_square_size
from chess.board import Board

# Initialising display
FPS: int = 60
window = pygame.display.set_mode((board_width, board_height))
pygame.display.set_caption('Chess Engine')


# User interaction with mouse
def get_board_row_col_from_mouse(position):
    x, y = position
    board_row = y // board_square_size
    board_column = x // board_square_size
    return board_row, board_column


# Event loop
def main():
    start_chess_engine = True
    runtime = pygame.time.Clock()
    chess_board = Board()

    while start_chess_engine:
        runtime.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start_chess_engine = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                board_row, board_column = get_board_row_col_from_mouse(position)
                piece = chess_board.get_pieces(board_row, board_column)
                chess_board.move_pieces(piece, 4, 3)

        chess_board.draw_pieces(window)
        pygame.display.update()

    pygame.quit()


main()
