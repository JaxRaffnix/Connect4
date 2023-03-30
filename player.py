from settings import *


def Set_Mark(board: list[list[str]], player: int, column: int) -> list[list[str]]:
    for row in range(ROWS):
        if board[row][column] == DEFAULT_MARK:
            board[row][column] = Get_Mark(player)
            return 
    raise IndexError(f"No empty rows in column {column} found.")


def Get_Mark(player: int) ->str:
    symbol = {1: SYMBOL_1,
              2: SYMBOL_2}
    return symbol.get(player)


def Undo_Mark(board: list[list[str]], column: int) -> list[list[str]]:
    for row in reversed(range(ROWS)):
        if board[row][column] != DEFAULT_MARK:
            board[row][column] = DEFAULT_MARK
            break
