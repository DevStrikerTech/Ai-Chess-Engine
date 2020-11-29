import pygame

# Initialising chessboard size and colors
board_width: int = 800
board_height: int = 800
board_rows: int = 8
board_columns: int = 8
board_square_size = board_width // board_columns
board_brown_square = (252, 204, 116)
board_white_square = (220, 211, 234)

# Initialising chessboard pieces color
black_piece = (0, 0, 0)
white_piece = (255, 182, 193)
position_piece = (0, 0, 255)
highlight_piece_grey = (128, 128, 128)

# Loading image and resize
crown_image = pygame.transform.scale(pygame.image.load('assets/crown.png'), (44, 25))
