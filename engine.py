import PySimpleGUI as psg
import moves as mv
from settings import *


def Menu():
    # start values
    scores = [0, 0, 0]
    game = 0

    window = psg.Window("Connect 4 Menu", Menu_Layout(
        scores, game), scaling=UI_SCALING)
    while True:
        event, values = window.read()
        if event in (psg.WIN_CLOSED, BUTTON_EXIT):
            break
        elif event == BUTTON_START:
            game += 1
            winner = Round(game)
            if winner == -1:
                break
            scores[winner] += 1
            window["-SCOREBOARD-"].update(Ui_Scoreboard(scores))
            window["-GAMES-"].update(Ui_Games(game))
    window.close()
    print(scores)


def Menu_Layout(scores, game):
    layout = [[psg.Text("Scoreboard")],
              [psg.Text(Ui_Games(game), key="-GAMES-")],
              [psg.Text(Ui_Scoreboard(scores), key="-SCOREBOARD-")],
              [psg.Button(BUTTON_START), psg.Button(BUTTON_EXIT)]]
    return layout


def Round(game):
    # start values
    player = 1
    turn = 1
    choice_history = [0] * CHOICE_HISTORY_MAX
    board = mv.Board_Init()

    window = psg.Window("Connect 4 Game", Round_Layout(
        board, player, turn, game))
    while True:
        event, values = window.read()
        if event in (psg.WIN_CLOSED, BUTTON_ABORT):
            winner = mv.Player_Switch(player)
            break
        elif event == BUTTON_EXIT:
            winner = -1
            break
        elif event == BUTTON_UNDO and turn > 1:
            turn -= 1
            window["-BOARD-"].update(Ui_Board(mv.Player_Undo(board,
                                     choice_history[turn])))
            player = Update_Turn_Player(window, turn, player)
        elif event in [str(i) for i in range(1, COLUMNS+1)]:
            try:
                choice = int(event) - 1
                choice_history[turn] = choice
                window['-BOARD-'].update(
                    Ui_Board(mv.Player_Setmark(board, player, choice)))
            except TypeError:
                psg.popup(f"Row {choice+1} is full. Choose a different row.")
                continue
            if mv.Check_Win(board, player):
                window.refresh()
                psg.popup(f"Win for player {mv.Player_Symbol(player)}!")
                winner = player
                break
            elif mv.Check_Draw(turn):
                window.refresh()
                psg.popup(POPUP_TIE)
                winner = 0
                break
            turn += 1
            player = Update_Turn_Player(window, turn, player)
    window.close()
    return winner


def Round_Layout(board, player_current, turn, game):
    layout = [[psg.Text(Ui_Player(player_current), key="-PLAYER-"), psg.Push(), psg.Text(Ui_Game_Current(game)), psg.Text(Ui_Turn(turn), key="-TURN-")],
              [psg.Text(Ui_Board(board), key="-BOARD-")],
              [psg.Text(Ui_Index())],
              [psg.Button(i) for i in range(1, COLUMNS+1)],
              [psg.Button(BUTTON_UNDO), psg.Button(BUTTON_ABORT), psg.Button(BUTTON_EXIT)]]
    return layout


def Update_Turn_Player(window, turn, player_current):
    window["-TURN-"].update(Ui_Turn(turn))
    player_current = mv.Player_Switch(player_current)
    window["-PLAYER-"].update(Ui_Player(player_current))
    return player_current


def Ui_Board(board):
    string = ""
    for row in reversed(range(ROWS)):
        for col in range(COLUMNS):
            string += board[row][col] + "\t"
        string += "\n"
    return string


def Ui_Index():
    indices = ""
    for i in range(1, COLUMNS+1):
        indices = indices + str(i) + "\t"
    return indices


def Ui_Player(player):
    return "Current Player: " + mv.Player_Symbol(player)


def Ui_Turn(turn):
    return "Turn: " + str(turn)


def Ui_Games(game):
    return "Game:" + "\t\t" + str(game)


def Ui_Game_Current(game):
    return "Game " + str(game)


def Ui_Scoreboard(scoreboard):
    string = "Draw: " + "\t\t" + str(scoreboard[0]) + "\n"
    string += "Player " + str(mv.Player_Symbol(1)) + \
        "\t" + str(scoreboard[1]) + "\n"
    string += "Player " + str(mv.Player_Symbol(2)) + \
        "\t" + str(scoreboard[2]) + "\n"
    return string
