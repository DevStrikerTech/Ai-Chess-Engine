from copy import deepcopy
import pygame

black_piece = (0, 0, 0)
white_piece = (255, 182, 193)


def minimax(position, depth, max_player, game):
    if depth == 0 or position.winner() is not None:
        return position.evaluate(), position

    if max_player:
        max_evaluation = float('-inf')
        best_move = None

        for move in get_all_moves(position, white_piece, game):
            evaluation = minimax(move, depth - 1, False, game)[0]
            max_evaluation = max(max_evaluation, evaluation)

            if max_evaluation == evaluation:
                best_move = move

        return max_evaluation, best_move

    else:
        min_evaluation = float('inf')
        best_move = None

        for move in get_all_moves(position, black_piece, game):
            evaluation = minimax(move, depth - 1, True, game)[0]
            min_evaluation = min(min_evaluation, evaluation)

            if min_evaluation == evaluation:
                best_move = move

        return min_evaluation, best_move


def simulate_move(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])

    if skip:
        board.remove(skip)

    return board


def get_all_moves(board, color, game):
    moves = []

    for piece in board.get_all_pieces(color):
        logical_moves = board.get_valid_moves(piece)

        for move, skip in logical_moves.item():
            temp_board = deepcopy(board)
            new_board = simulate_move(piece, move, temp_board, game, skip)
            moves.append(new_board)

    return moves
