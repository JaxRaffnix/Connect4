import math
import engine as engine
import player as pl
from settings import *

AI_PLAYER = 2
DEPTH_MAX = 3


def Ai_Move(board):
    column = best_move(board)
    pl.Set_Mark(board, AI_PLAYER, column)
    return column


def best_move(board):
    depth = 0
    best_score = - math.inf
    best_move = None
    for column in possible_moves(board):
        pl.Set_Mark(board, column, AI_PLAYER)
        score = minmax(board, False, depth)
        pl.Undo_Mark(board, column)
        if score > best_score:
            best_score = score
            best_move = column
    return best_move


def minmax(board, is_Max_Turn, depth):

    depth += 1
    if depth > DEPTH_MAX:
        return 0
    if pl.Check_Win(board, AI_PLAYER):
        return 1
    elif pl.Check_Win(board, pl.Switch_Player(AI_PLAYER)):
        return -1
    elif pl.Check_Draw(board, AI_PLAYER):
        return 0

    scores = []
    for column in possible_moves(board):
        pl.Set_Mark(board, column, AI_PLAYER)
        scores.append(minmax(board, not is_Max_Turn, depth))
        pl.Undo_Mark(board, column)

    if is_Max_Turn:
        return max(scores)
    else:
        return min(scores)


def possible_moves(board):
    available_columns = []
    for col in range(COLUMNS):
        if board[ROWS-1][col] == DEFAULT_MARK:
            available_columns += [col]
    return available_columns
