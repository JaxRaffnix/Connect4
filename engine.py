# import PySimpleGUI as psg
from time import sleep
import MinMaxAi as mma
import player as pl
from settings import *
import interface as ui


def Menu():
    playerscore = [0, 0, 0]
    game = 0

    window= ui.Menu(game, playerscore)
    while True:
        input, aimode = ui.Read_Menu(window)
        if input == "exit":
            break
        elif input == "start":
            game += 1
            window["-GAMES-"].update(ui.Games(game))
            window.refresh()
            winner = Play_Round(game, aimode)
            if winner == -1:
                break
            playerscore[winner] += 1
            window["-SCOREBOARD-"].update(ui.Scoreboard(playerscore))
    window.close()
    return playerscore


def Play_Round(game, aimode):
    player = 1
    turn = 1
    choice_log = [0] * CHOICE_LOG_MAX
    board = [[DEFAULT_MARK] * COLUMNS for _ in range(ROWS)]
    window = ui.Round(game, aimode, board, player, turn)

    while True:
        ui_input = ui.Read_Round(window)
        if ui_input == "abort":
            winner =  Switch_Player(player)
            break
        elif ui_input == "exit":
            winner = -1
            break 
        elif ui_input == "undo" and turn > 1:
            turn -= 1
            pl.Undo_Mark(board, choice_log[turn])
            player = Switch_Player(player)
            window["-BOARD-"].update(ui.Board(board))
            ui.Update_Turn_Player(window, turn, player)
        elif valid_input(ui_input):
            choice = int(ui_input) - 1
            try:
                place_mark(window, choice_log, board, player, turn, choice)
            except IndexError:
                ui.Msg_Col(choice)
                continue            
            if check_endgame(window, board, player):
                if Check_Win(board, player):
                    winner = player
                    break
                else:
                    winner = 0
                    break
            turn += 1
            player= Switch_Player(player)
            
            if turn % 2 == 0 and aimode:
                window.refresh()
                choice = mma.Ai_Move(board) 
                place_mark(window, choice_log, board, player, turn, choice)
                if check_endgame(window, board, player):
                    if Check_Win(board, player):
                        winner = player
                        break
                    else:
                        winner = 0
                        break
                turn += 1
                player = Switch_Player(player)
            ui.Update_Turn_Player(window, turn, player)
    window.close()
    return winner

def place_mark(window, choice_log, board, player, turn, choice):
    pl.Set_Mark(board, player, choice)
    choice_log[turn] = choice
    window["-BOARD-"].update(ui.Board(board))


def valid_input(ui_input):
    return ui_input in [str(i) for i in range(1, COLUMNS+1)]

def check_endgame(window, board, player):
    if Check_Win(board, player):
        window.refresh()
        ui.Msg_Win(player)
        return True
    elif Check_Draw(board, player):
        window.refresh()
        ui.Msg_Tie()
        return True
    return False

def Check_Win(board: list[list[str]], player: int):
    mark = pl.Get_Mark(player)
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


def Check_Draw(board, player) -> bool:
    mark_1 = pl.Get_Mark(player)
    mark_2 = pl.Get_Mark(Switch_Player(player))
    if all(board[row][col] in (mark_1, mark_2) for row in range(ROWS) for col in range(COLUMNS)):
        return True
    return False

def Switch_Player(player: int) -> int:
    return 3 - player