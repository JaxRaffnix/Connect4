# Goal: Create the game 4 wins for twoplayermode and singleplayer mode against AI

import engine as eg
import PySimpleGUI as sg

board = eg.board_initialise()

player_current = 1

layout =    [[sg.Text("Current Player:"), sg.Text(eg.player_mark(player_current), key="-PLAYER-")],
            [sg.Text(eg.board_show(board), key="-BOARD-")],
            [sg.Text("Choose a row:"), sg.Input(key='-IN-')],
            [sg.Button("Set Mark"),sg.Button("Abort Round"), sg.Button("Exit Game")]]

window = sg.Window("4 Wins", layout)

while True: 
    event, values = window.read()
    print(event, values)
    if event in (sg.WIN_CLOSED, "Abort Round", "Exit Game"):
        break
    if event == "Set Mark":
        try:
            choice = int(values["-IN-"]) - 1
            window['-BOARD-'].update(eg.board_show(eg.setmark(board, player_current, choice)))
        except ValueError:
            print("Invalid input, choose a number between 1 and 7")
        except IndexError:
            print("Invalid input '{}', choose a row of 1 to 7.".format(choice+1))
            window["-IN-"].update("")
            continue        
        except TypeError:
            print("Row {} has been filled. Choose a different row.".format(choice+1))
            window["-IN-"].update("")
            continue  
        window["-IN-"].update("")
        player_current = eg.player_switch(player_current)
        window["-PLAYER-"].update(eg.player_mark(player_current))
window.close()