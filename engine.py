import library

def board_initialise():
    board = [
        ["-","-","-","-","-","-","-"],
        ["-","-","-","-","-","-","-"],
        ["-","-","-","-","-","-","-"],
        ["-","-","-","-","-","-","-"],
        ["-","-","-","-","-","-","-"],
        ["-","-","-","-","-","-","-"]]
    return board

def board_show(board):
    outputstring = ""
    for i in range(len(board)):
        for j in range(len(board[i])):
            outputstring = outputstring + board[i][j] + "\t"
        outputstring = outputstring + "\n"
    outputstring = outputstring + "\n" + board_index() 
    return outputstring

def board_index():
    indices = ""
    for i in range(1,8):
        indices = indices + str(i) + "\t"
    return indices
    

def setmark(board, player, choice):
    for i in reversed(range(len(board))):
        if board[i][choice] == player_mark(1) or board[i][choice] == player_mark(2):
            continue
        else:
            board[i][choice] = player_mark(player)
            return board
    

def player_mark(player):
    if player == 1:
        return library.SYMBOL_1
    if player == 2:
        return library.SYMBOL_2
    else:
        ValueError("Unsupported player number: " + str(player) + ".")

def player_switch(player):
    if player == 1:
        return 2
    if player == 2:
        return 1
