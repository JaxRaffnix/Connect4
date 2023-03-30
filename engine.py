# import PySimpleGUI as psg
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
            print("DEBUG")
            if winner == -1:
                break
            playerscore[winner] += 1
            window["-SCOREBOARD-"].update(ui.Scoreboard(playerscore))
    window.close()
    return playerscore


def Play_Round(game, aimode):
    player = 1
    turn = 1
    choice_history = [0] * CHOICE_HISTORY_MAX
    board = [[DEFAULT_MARK] * COLUMNS for _ in range(ROWS)]
    window = ui.Round(game, aimode, board, player, turn)

    while True:
        input = ui.Read_Round(window)
        if input == "abort":
            winner =  Switch_Player(player)
            break
        elif input == "exit":
            winner = -1
            break
        elif input == "undo" and turn > 1:
            turn -= 1
            pl.Undo_Mark(board, choice_history[turn])
            window["-BOARD-"].update(ui.Board(board))
            player = Switch_Player(player)
            ui.Update_Turn_Player(window, turn, player)
        elif input in [str(i) for i in range(1, COLUMNS+1)]:
            choice = int(input) - 1
            try:
                pl.Set_Mark(board, player, choice)
            except IndexError:
                ui.Msg_Col(choice)
                continue
            choice_history[turn] = choice
            window['-BOARD-'].update(ui.Board(board))
            if Check_Win(board, player):
                window.refresh()
                ui.Msg_Win(player)
                winner = player
                break
            elif Check_Draw(board, player):
                window.refresh()
                winner = 0
                break
            turn += 1
            player = Switch_Player(player)
            ui.Update_Turn_Player(window, turn, player)
    window.close()
    print("Here DEBUG")
    # return winner


def Check_Win(board: list[list[str]], player: int) -> bool:
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