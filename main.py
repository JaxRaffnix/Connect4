# Goal: Create the game connect 4 for twoplayermode and singleplayer mode against AI

import engine as eg
import PySimpleGUI as sg

board = eg.board_initialise()

# start values
player_current = 1
turn = 1
choice_log = [0]*100

layout = [[sg.Text(eg.player_status(player_current), key="-PLAYER-"), sg.Push(), sg.Text(eg.turn_print(turn), key="-TURN-")],
          [sg.Text(eg.board_print(board), key="-BOARD-")],
          [sg.Text(eg.board_index(board))],
        #   [(sg.Button(str(i)), sg.Text("\t")) for i in range(1,8)]]
          [sg.Button(i) for i in range(1,eg.board_size(board))]]
layout += [[sg.Button("Undo"), sg.Button("Abort Round"), sg.Button("Exit Game")]]

window = sg.Window("Connect 4", layout, scaling = 2.5)

while True: 
    event, values = window.read()
    if event in (sg.WIN_CLOSED, "Abort Round", "Exit Game"):
        break
    elif event == "Undo" and turn > 1:
        turn -= 1
        window["-BOARD-"].update(eg.board_print(eg.undo(board, choice_log[turn])))
        window["-TURN-"].update(eg.turn_print(turn))
        player_current = eg.player_switch(player_current)
        window["-PLAYER-"].update(eg.player_status(player_current))
    elif event in ["1","2","3","4","5","6","7"]:
        try:
            choice = int(event) - 1
            choice_log[turn] = choice
            window['-BOARD-'].update(eg.board_print(eg.setmark(board, player_current, choice)))    
        except TypeError:
            print(f"Row {choice+1} has been filled. Choose a different row.")
            continue
        if eg.check_win(board, player_current) == True:
            window.refresh()
            sg.popup(f"Win for player {eg.player_mark(player_current)}!")
            break
        turn += 1
        window["-TURN-"].update(eg.turn_print(turn))
        player_current = eg.player_switch(player_current)
        window["-PLAYER-"].update(eg.player_status(player_current))
window.close()