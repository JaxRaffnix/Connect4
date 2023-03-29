from settings import *


def Set_Mark(board: list[list[str]], player: int, column: int) -> list[list[str]]:
    for row in range(ROWS):
        if board[row][column] == DEFAULT_MARK:
            board[row][column] = Get_Mark(player)
            break
    return board


def Get_Mark(player: int) ->str:
    symbol = {1: SYMBOL_1,
              2: SYMBOL_2}
    return symbol.get(player)


def Switch_Player(player: int) -> int:
    return 3 - player


def Undo_Mark(board: list[list[str]], column: int) -> list[list[str]]:
    for row in reversed(range(ROWS)):
        if board[row][column] != DEFAULT_MARK:
            board[row][column] = DEFAULT_MARK
            break
    return board

def Check_Win(board: list[list[str]], player: int) -> bool:
    mark = Get_Mark(player)
    # horizontal
    for row in range(ROWS):
        for col in range(COLUMNS - 3):
            if all(cell == mark for cell in board[row][col:col+4]):
                return True
    # vertical
    for row in range(ROWS - 3):
        for col in range(COLUMNS):
            if all(board[row][col] == mark for row in range(row, row+4)):
                return True
    # diagonal right-left descending
    for row in range(ROWS - 3):
        for col in range(COLUMNS - 3):
            if all(board[row+i][col+i] == mark for i in range(4)):
                return True
    # diagonal left-right ascending
    for row in range(3, ROWS):
        for col in range(COLUMNS - 3):
            if all(board[row-i][col+i] == mark for i in range(4)):
                return True
    return False


def Check_Draw(turn: int) -> bool:
    return turn >= ROWS * COLUMNS
