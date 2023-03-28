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

def board_print(board):
    string = ""
    for i in range(len(board)):
        for j in range(len(board[i])):
            string = string + board[i][j] + "\t"
        string += "\n"
    return string

def board_index(board):
    indices = ""
    for i in range(1,board_size(board)):
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
    elif player == 2:
        return library.SYMBOL_2

def player_switch(player):
    if player == 1:
        return 2
    elif player == 2:
        return 1

def player_status(player):
    return "Current Player: " + player_mark(player)

def turn_print(turn):
    return "Turn: " + str(turn)

def board_size(board):
    return len(board[0]) +1

def check_win(board, player):
    for i in range(len(board)):
        for j in range(len(board[i])):
            try:
                # horizontal
                if player_mark(player) == board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3]:
                    return True
                # vertical            
                elif player_mark(player) == board[i][j] == board[i-1][j] == board[i-2][j] == board[i-3][j]:
                    return True
                # diagonal left-right ascending
                elif player_mark(player) == board[i][j] == board[i+1][j-1] == board[i+2][j-2] == board[i+3][j-3]:
                    return True
                # diagonal right-left descending
                elif player_mark(player) == board[i][j] == board[i-1][j+1] == board[i-2][j+2] == board[i-3][j+3]:
                    return True
                # diagonal left-right descending
                elif player_mark(player) == board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3]:
                    return True
                # diagonal right-left ascending
                elif player_mark(player) == board[i][j] == board[i-1][j-1] == board[i-2][j-2] == board[i-3][j-3]:
                    return True
                else:
                    return False
            except IndexError:
                continue

def undo(board, choice):
    for i in reversed(range(len(board))):
        try:
            if board[i][choice] == player_mark(1) or board[i][choice] == player_mark(2):
                continue
            else:
                board[i+1][choice] = "-"
        except IndexError:
            continue        
        return board
        