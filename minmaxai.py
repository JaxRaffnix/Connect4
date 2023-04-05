import math
import engine as eng
import player as pl
from settings import *


def Ai_Move(board):
    _, bestmove = minmax(board, DEPTH_MAX, True)
    return bestmove

def minmax(board, depth, ai_turn):
    if depth == 0 or eng.Check_Win(board, AI_PLAYER) or eng.Check_Win(board, eng.Switch_Player(AI_PLAYER)):
        return evaluate_board(board), None

    if ai_turn:
        best_score = -math.inf
        best_move = None
        for column in possible_moves(board):
            pl.Set_Mark(board, AI_PLAYER, column)
            score, _ = minmax(board, depth -1, False)
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


def evaluate_board(board):
    if eng.Check_Win(board, AI_PLAYER):
        return 100
    elif eng.Check_Win(board, eng.Switch_Player(AI_PLAYER)):
        return -100
    else:
        return 0


def possible_moves(board):
    available_columns = []
    for col in range(COLUMNS):
        if board[ROWS-1][col] == DEFAULT_MARK:
            available_columns += [col]
    return available_columns
