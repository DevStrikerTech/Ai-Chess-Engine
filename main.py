import pygame
from chess.variable_declaration import board_width, board_height, board_square_size, black_piece, white_piece
from chess.rules import Rules
from minimax.algorithm import minimax

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
    game_rules = Rules(window)

    while start_chess_engine:
        runtime.tick(FPS)

        if game_rules.turn_taken == white_piece:
            value, new_board = minimax(game_rules.get_board(), 3, white_piece, game_rules)
            game_rules.algorithm_move(new_board)

        if game_rules.winner() is not None:
            print(game_rules.winner())
            start_chess_engine = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start_chess_engine = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                board_row, board_column = get_board_row_col_from_mouse(position)
                game_rules.select(board_row, board_column)

        game_rules.update()

    pygame.quit()


main()
