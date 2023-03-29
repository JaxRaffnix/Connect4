import PySimpleGUI as psg
from settings import *
import moves as mv

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
        window["-BOARD-"].update(Ui_Board(mv.Undo_Mark(board, choice_history[turn])))
    elif event in [str(i) for i in range(1, COLUMNS+1)]:
        choice = int(event) - 1
        if choice_history[turn] != None:
            continue
        try:
            choice_history[turn] = choice
            board = mv.Set_Mark(board, player, choice)
            window['-BOARD-'].update(Ui_Board(board))
        except TypeError:
            psg.popup(f"Row {choice+1} is full. Choose a different row.")
            continue
        if mv.Check_Win(board, player):
            winner = player
            break
        elif mv.Check_Draw(turn):
            winner = 0
            break
        turn += 1
        player = mv.Switch_Player(player)
window.close()
return winner
