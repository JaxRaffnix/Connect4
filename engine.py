import library

def board_initialise():
    board = [
        ["-","-","-","-","-","-","-"],
        ["-","-","-","-","-","-","-"],
        ["-","-","-","-","-","-","-"],
        ["-","-","-","-","-","-","-"],
        ["-","-","-","-","-","-","-"],
        ["-","-","-","-","-","-","-"],
        ["1","2","3","4","5","6","7"]]
    return board

def board_show(board):
    outputstring = ""
    for i in range(len(board)):
        for j in range(len(board[i])):
            outputstring = outputstring + board[i][j] + "\t"
        outputstring = outputstring + "\n"
    return outputstring
    

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
