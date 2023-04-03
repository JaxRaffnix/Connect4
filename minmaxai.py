import math
import engine as eng
import player as pl
from settings import *


def Ai_Move(board):
    i, bestmove = minmax(board, DEPTH_MAX, True)
    return bestmove

def minmax(board, depth, is_max_turn):
    if depth == 0 or eng.Check_Win(board, AI_PLAYER) or eng.Check_Win(board, eng.Switch_Player(AI_PLAYER)):
        return evaluate_board(board), None

    if is_max_turn:
        best_score = -math.inf
        best_move = None
        for column in possible_moves(board):
            pl.Set_Mark(board, AI_PLAYER, column)
            score, _ = minmax(board, depth - 1, False)
            pl.Undo_Mark(board, column)
            if score > best_score:
                best_score = score
                best_move = column
        return best_score, best_move
    else:
        best_score = math.inf
        best_move = None
        for column in possible_moves(board):
            pl.Set_Mark(board, eng.Switch_Player(AI_PLAYER), column)
            score, _ = minmax(board, depth - 1, True)
            pl.Undo_Mark(board, column)
            if score < best_score:
                best_score = score
                best_move = column
        return best_score, best_move


# def best_move(board):
#     # depth = 0
#     best_score = - math.inf
#     best_move = None
#     for column in possible_moves(board):
#         score = get_score(board, column, DEPTH_MAX, True)
#         if score > best_score:
#             best_score = score
#             best_move = column
#     return best_move

# def get_score(board, column, depth, is_max_turn):
#     if depth == 0 or eng.Check_Win(board, AI_PLAYER) or eng.Check_Win(board, eng.Switch_Player(AI_PLAYER)):
#         return evaluate_board(board)

#     pl.Set_Mark(board, AI_PLAYER if is_max_turn else eng.Switch_Player(AI_PLAYER), column)

#     if is_max_turn:
#         score = -math.inf
#         for c in possible_moves(board):
#             score = max(score, get_score(board, c, depth - 1, False))
#     else:
#         score = math.inf
#         for c in possible_moves(board):
#             score = min(score, get_score(board, c, depth - 1, True))

#     pl.Undo_Mark(board, column)

#     return score


def evaluate_board(board):
    if eng.Check_Win(board, AI_PLAYER):
        return 100
    elif eng.Check_Win(board, eng.Switch_Player(AI_PLAYER)):
        return -100
    else:
        return 0


# def minmax(board, is_Max_Turn, depth):

#     depth += 1
#     if depth > DEPTH_MAX:
#         return 0
#     if eng.Check_Win(board, AI_PLAYER):
#         return 1
#     elif eng.Check_Win(board, eng.Switch_Player(AI_PLAYER)):
#         return -1
#     elif eng.Check_Draw(board, AI_PLAYER):
#         return 0

#     scores = []
#     for column in possible_moves(board):
#         pl.Set_Mark(board, AI_PLAYER, column)
#         scores.append(minmax(board, not is_Max_Turn, depth))
#         pl.Undo_Mark(board, column)

#     if is_Max_Turn:
#         return max(scores)
#     else:
#         return min(scores)
    

# def minmax(board, is_max_turn, depth, alpha=-math.inf, beta=math.inf):
#     if depth == DEPTH_MAX:
#         return 0
#     if eng.Check_Win(board, AI_PLAYER):
#         return 1
#     elif eng.Check_Win(board, eng.Switch_Player(AI_PLAYER)):
#         return -1
#     elif eng.Check_Draw(board, AI_PLAYER):
#         return 0

#     if is_max_turn:
#         value = -math.inf
#         for column in possible_moves(board):
#             pl.Set_Mark(board, AI_PLAYER, column)
#             value = max(value, minmax(board, False, depth+1, alpha, beta))
#             pl.Undo_Mark(board, column)
#             alpha = max(alpha, value)
#             if alpha >= beta:
#                 break
#     else:
#         value = math.inf
#         for column in possible_moves(board):
#             pl.Set_Mark(board, eng.Switch_Player(AI_PLAYER), column)
#             value = min(value, minmax(board, True, depth+1, alpha, beta))
#             pl.Undo_Mark(board, column)
#             beta = min(beta, value)
#             if beta <= alpha:
#                 break

#     return value





def possible_moves(board):
    available_columns = []
    for col in range(COLUMNS):
        if board[ROWS-1][col] == DEFAULT_MARK:
            available_columns += [col]
    return available_columns
