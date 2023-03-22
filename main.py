# Goal: Create the game 4 wins for twoplayermode and singleplayer mode against AI

import engine as eg
import PySimpleGUI as sg

board = eg.board_initialise()

# start values
player_current = 1
turn = 1

layout =    [[sg.Text("Current Player: "), sg.Text(eg.player_mark(player_current), key="-PLAYER-"),
              sg.Push(), sg.Text("Turn: "), sg.Text(turn, key="-TURN-"),],
            [sg.Text(eg.board_show(board), key="-BOARD-")],
            [sg.Text("Choose a row:"), sg.Input(key='-IN-')],
            [sg.Button("Set Mark"),sg.Push(), sg.Button("Abort Round"), sg.Button("Exit Game")]]

# sg.set_options(font=("Courier New",12))

window = sg.Window("4 Wins", layout, scaling = 2.5, finalize=True)
window["-IN-"].bind("<Return>", "_Enter")

while True: 
    event, values = window.read()
    print(event, values)
    if event in (sg.WIN_CLOSED, "Abort Round", "Exit Game"):
        break
    if event == "Set Mark" or event ==("-IN-"+"_Event"):
        try:
            choice = int(values["-IN-"]) - 1
            if choice < 0:
                print("Invalid input '{}', choose a number between 1 and 7.".format(choice+1))
                window["-IN-"].update("")
                continue  
            window['-BOARD-'].update(eg.board_show(eg.setmark(board, player_current, choice)))
        except ValueError:
            print("Invalid input, choose a number between 1 and 7")
        except IndexError:
            print("Invalid input '{}', choose a row bewteen 1 to 7.".format(choice+1))
            window["-IN-"].update("")
            continue        
        except TypeError:
            print("Row {} has been filled. Choose a different row.".format(choice+1))
            window["-IN-"].update("")
            continue  
        window["-IN-"].update("")
        player_current = eg.player_switch(player_current)
        window["-PLAYER-"].update(eg.player_mark(player_current))
        turn += 1
        window["-TURN-"].update(turn)
window.close()