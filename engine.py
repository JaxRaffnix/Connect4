import PySimpleGUI as psg
import moves as mv
from settings import *


def Start_Menu():
    # start values
    scores = [0, 0, 0]
    game = 0

    layout = [[psg.Text("Scoreboard")],
              [psg.Text(Ui_Games(game), key="-GAMES-")],
              [psg.Text(Ui_Scoreboard(scores), key="-SCOREBOARD-")],
              [psg.Button(BUTTON_START), psg.Button(BUTTON_EXIT)]]

    window = psg.Window("Connect 4 Menu", layout, scaling=UI_SCALING)
    while True:
        event, values = window.read()
        if event in (psg.WIN_CLOSED, BUTTON_EXIT):
            break
        elif event == BUTTON_START:
            game += 1
            window["-GAMES-"].update(Ui_Games(game))
            window.refresh()
            winner = Play_Round(game)
            if winner == -1:
                break
            scores[winner] += 1
            window["-SCOREBOARD-"].update(Ui_Scoreboard(scores))

    window.close()
    return scores


def Play_Round(game):
    # start values
    player = 1
    turn = 1
    choice_history = [0] * CHOICE_HISTORY_MAX
    board = [[DEFAULT_MARK] * COLUMNS for _ in range(ROWS)]

    layout = [[psg.Text(Ui_Player(player), key="-PLAYER-"), psg.Push(), psg.Text(Ui_Game_Current(game)), psg.Text(Ui_Turn(turn), key="-TURN-")],
              [psg.Text(Ui_Board(board), key="-BOARD-")],
              [psg.Text(Ui_Index())],
              [psg.Button(i) for i in range(1, COLUMNS+1)],
              [psg.Button(BUTTON_UNDO), psg.Button(BUTTON_ABORT), psg.Button(BUTTON_EXIT)]]

    window = psg.Window("Connect 4 Play", layout)
    while True:
        event, values = window.read()
        if event in (psg.WIN_CLOSED, BUTTON_ABORT):
            winner = mv.Switch_Player(player)
            break
        elif event == BUTTON_EXIT:
            winner = -1
            break
        elif event == BUTTON_UNDO and turn > 1:
            turn -= 1
            window["-BOARD-"].update(Ui_Board(mv.Undo_Mark(board,
                                     choice_history[turn])))
            player = Update_Turn_Player(window, turn, player)
        elif event in [str(i) for i in range(1, COLUMNS+1)]:
            try:
                choice = int(event) - 1
                choice_history[turn] = choice
                window['-BOARD-'].update(
                    Ui_Board(mv.Set_Mark(board, player, choice)))
            except TypeError:
                psg.popup(f"Row {choice+1} is full. Choose a different row.")
                continue
            if mv.Check_Win(board, player):
                window.refresh()
                psg.popup(f"Win for player {mv.Get_Mark(player)}!")
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


def Update_Turn_Player(window, turn, player):
    window["-TURN-"].update(Ui_Turn(turn))
    player = mv.Switch_Player(player)
    window["-PLAYER-"].update(Ui_Player(player))
    return player


def Ui_Board(board):
    return "\n".join(["\t".join(row) for row in reversed(board)])


def Ui_Index():
    return '\t'.join(str(i) for i in range(1, COLUMNS+1))


def Ui_Player(player):
    return "Current Player: " + mv.Get_Mark(player)


def Ui_Turn(turn):
    return "Turn: " + str(turn)


def Ui_Game_Current(game):
    return "Game " + str(game)

def Ui_Games(game):
    return "Games:" + "\t\t" + str(game)

def Ui_Scoreboard(scoreboard):
    string = ""
    labels = ["Draw\t", 
              "Player " + str(mv.Get_Mark(1)), 
              "Player " + str(mv.Get_Mark(2))]
    for i in range(3):
        string += f"{labels[i]:<10}\t{scoreboard[i]}\n"
    return string
