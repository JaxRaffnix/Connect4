import math
import engine as engine
import moves as mv
from settings import *

# import math

PLAYER = 2
DEPTH_MAX = 3


def minmax(mm_board, is_Max_Turn, depth):

    depth += 1
    if depth > DEPTH_MAX:
        return 0
    if mv.Check_Win(mm_board, PLAYER):
        return 1
    elif mv.Check_Win(mm_board, mv.Switch_Player(PLAYER)):
        return -1
    elif mv.Check_Draw(mm_board):
        return 0

    scores = []
    for col in possible_moves(mm_board):
        mv.Set_Mark(mm_board, col, PLAYER)
        scores.append(minmax(mm_board, not is_Max_Turn, depth))
        mv.Undo_Mark(mm_board, col)

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


def best_move(board):
    depth = 0
    best_score = - math.inf
    best_move = None
    for column in possible_moves(board):
        mv.Set_Mark(board, column, PLAYER)
        score = minmax(board, False, depth)
        mv.Undo_Mark(board, column)
        if score > best_score:
            best_score = score
            best_move = column
    return best_move

def aiturn(board):
    column = best_move(board)
    return mv.Set_Mark(board, PLAYER, column)