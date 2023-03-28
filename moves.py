import library
from settings import *


def Board_Init():
    board = [[DEFAULT_MARK] * COLUMNS for i in range(ROWS)]
    return board


def Player_Setmark(board, player, choice):
    for row in range(ROWS):
        if board[row][choice] in (Player_Symbol(player), Player_Symbol(Player_Switch(player))):
            continue
        else:
            board[row][choice] = Player_Symbol(player)
            return board


def Player_Symbol(player):
    if player == 1:
        return library.SYMBOL_1
    elif player == 2:
        return library.SYMBOL_2


def Player_Switch(player):
    return 3 - player


def Player_Undo(board, choice):
    for row in reversed(range(ROWS)):
        if board[row][choice] == DEFAULT_MARK:
            continue
        else:
            board[row][choice] = DEFAULT_MARK
            break
    return board


def Check_Win(board, player):
    for row in range(ROWS):
        for col in range(COLUMNS - 3):
            if Player_Symbol(player) == board[row][col] == board[row][col+1] == board[row][col+2] == board[row][col+3]:
                return True
    # vertical
    for row in range(ROWS - 3):
        for col in range(COLUMNS):
            if Player_Symbol(player) == board[row][col] == board[row+1][col] == board[row+2][col] == board[row+3][col]:
                return True
    # diagonal right-left descending
    for row in range(ROWS - 3, ROWS):
        for col in range(COLUMNS - 3):
            if Player_Symbol(player) == board[row][col] == board[row-1][col+1] == board[row-2][col+2] == board[row-3][col+3]:
                return True
    # diagonal left-right ascending
    for row in range(ROWS - 3):
        for col in range(COLUMNS - 3):
            if Player_Symbol(player) == board[row][col] == board[row+1][col+1] == board[row+2][col+2] == board[row+3][col+3]:
                return True
    return False


def Check_Draw(turn):
    if turn >= 42:
        return True
    return False
