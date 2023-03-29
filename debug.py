# The Minimax algorithm is a decision-making algorithm that is used to find the optimal move in a two-player game. It works by recursively analyzing all possible moves that the player and the opponent can make, up to a certain depth, and assigning a score to each possible outcome. The score reflects the likelihood of winning or losing the game from that position.

# To implement the Minimax algorithm for the Connect 4 game, we need to define the following functions:

# evaluate: This function takes a Connect 4 board and a player's mark as input and returns a score that reflects the likelihood of the player winning the game from the current board position.

# minimax: This function takes a Connect 4 board, a player's mark, a depth, and a boolean flag indicating whether the player is the maximizing player or not. It returns the score of the best move that the player can make.

import copy

def minimax(board, player, depth):
    if depth == 0 or is_terminal(board):
        return None, score(board, player)

    best_column = None
    if player == 1:
        best_score = -float('inf')
        for column in range(COLUMNS):
            if is_valid_move(board, column):
                new_board = copy.deepcopy(board)
                drop_mark(new_board, column, player)
                _, score = minimax(new_board, 2, depth-1)
                if score > best_score:
                    best_score = score
                    best_column = column
    else:
        best_score = float('inf')
        for column in range(COLUMNS):
            if is_valid_move(board, column):
                new_board = copy.deepcopy(board)
                drop_mark(new_board, column, player)
                _, score = minimax(new_board, 1, depth-1)
                if score < best_score:
                    best_score = score
                    best_column = column

    return best_column, best_score

def is_valid_move(board,








##############################


def make_best_move():
    bestScore = -math.inf
    bestMove = None
    for move in ticTacBoard.get_possible_moves():
        ticTacBoard.make_move(move)
        score = minimax(False, aiPlayer, ticTacBoard)
        ticTacBoard.undo()
        if (score > bestScore):
            bestScore = score
            bestMove = move
    ticTacBoard.make_move(bestMove)

def minimax(isMaxTurn, maximizerMark, board):
    state = board.get_state()
    if (state is State.DRAW):
        return 0
    elif (state is State.OVER):
        return 1 if board.get_winner() is maximizerMark else -1

    scores = []
    for move in board.get_possible_moves():
        board.make_move(move)
        scores.append(minimax(not isMaxTurn, maximizerMark, board))
        board.undo()

    return max(scores) if isMaxTurn else min(scores)