import PySimpleGUI as psg
from settings import *
import player as pl


def Menu(game, playerscore):
    settings = [psg.Radio("Singleplayer", "-PLAYERS-", key="-AIMODE-", default=True), 
                psg.Radio("Multiplayer", "-PLAYERS-", default=False)]
    layout = [[psg.Text(Games(game), key="-GAMES-")],
              [psg.Frame("Scoreboard", [[psg.Text(Scoreboard(playerscore), key="-SCOREBOARD-")]])],
              [psg.Frame("Settings", [settings])],
              [psg.Button(BUTTON_START), psg.Button(BUTTON_EXIT)]]
    
    window = psg.Window("Connect 4 Menu", layout, scaling=UI_SCALING)
    return window

def Read_Menu(window):
    event, values = window.read()
    if event in (psg.WIN_CLOSED, BUTTON_EXIT):
        return "exit", values["-AIMODE-"]
    elif event == BUTTON_START:
         return "start", values["-AIMODE-"]

def Round(game, aimode, board, player, turn):
    layout = [[psg.Text(Player(player), key="-PLAYER-"), psg.Push(), 
               psg.Text(f"AI: {str(aimode)}"), psg.Text(Game_Current(game)), 
               psg.Text(Turn(turn), key="-TURN-")],
              [psg.Frame("", [[psg.Text(Board(board), key="-BOARD-")]])],
              [psg.Text(COLUMN_SEPERATOR.join(str(i) for i in range(1, COLUMNS+1)))],
              [psg.Button(i) for i in range(1, COLUMNS+1)],
              [psg.Button(BUTTON_UNDO), psg.Button(BUTTON_ABORT), psg.Button(BUTTON_EXIT)]]

    window = psg.Window("Connect 4 Play", layout)
    return window

def Read_Round(window):
    event, values = window.read()
    if event in (psg.WIN_CLOSED, BUTTON_ABORT):
        return "abort"
    elif event == BUTTON_EXIT:
        return "exit"
    elif event == BUTTON_UNDO:
        return "undo"
    elif event in [str(i) for i in range(1, COLUMNS+1)]:
        return str(event)

def Update_Turn_Player(window, player, turn):
    window["-TURN-"].update(Turn(turn))
    window["-PLAYER-"].update(Player(player))

def Board(board):
    return "\n".join([COLUMN_SEPERATOR.join(row) for row in reversed(board)])


def Player(player):
    return "Current Player: " + pl.Get_Mark(player)


def Turn(turn):
    return "Turn: " + str(turn)


def Game_Current(game):
    return "Game: " + str(game)


def Games(game):
    return "Games:" + "\t" + str(game)


def Scoreboard(scoreboard):
    string = ""
    labels = ["Draw ",
              "Player " + str(pl.Get_Mark(1)),
              "Player " + str(pl.Get_Mark(2))]
    for i in range(3):
        string += f"{labels[i]:<10}\t{scoreboard[i]}\n"
    return string

def Msg_Col(choice):
    psg.popup(f"Row {choice+1} is full. Choose a different row.")

def Msg_Win(player):
    psg.popup(f"Win for player {pl.Get_Mark(player)}!")

def Msg_Tie():
    psg.popup(POPUP_TIE)
