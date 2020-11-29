import pygame
from chess.variable_declaration import board_width, board_height
from chess.board import Board

# Initialising display
FPS: int = 60
window = pygame.display.set_mode((board_width, board_height))
pygame.display.set_caption('Chess Engine')


# Event loop
def main():
    start_chess_engine = True
    runtime = pygame.time.Clock()
    chess_board = Board()

    piece = chess_board.get_pieces(0, 1)
    chess_board.move_pieces(piece, 4, 3)

    while start_chess_engine:
        runtime.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start_chess_engine = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        chess_board.draw_pieces(window)
        pygame.display.update()

    pygame.quit()


main()
