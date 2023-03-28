import PySimpleGUI as psg
import engine as eng

CHOICE_HISTORY_MAX = 43
UI_SCALING = 2.5
GAME_STRING = "Connect 4"
UNDO_STRING = "Undo Move"
ABORT_STRING = "Abort Round"
EXIT_STRING = "Exit Game"
TIE_STRING = "Tie Game!"

def Round():
    # start values
    player = 1
    turn = 1
    choice_history = [0] * CHOICE_HISTORY_MAX
    board = eng.Board_Initialise()

    window = psg.Window(GAME_STRING, Ui_Layout(board, player, turn), scaling = UI_SCALING)
    while True:
        event, values = window.read()
        if event in (psg.WIN_CLOSED, ABORT_STRING):
            winner = eng.Player_Switch(player)
            break
        elif event == EXIT_STRING:
            winner = -1
            break
        elif event == UNDO_STRING and turn > 1:
            turn -= 1
            window["-BOARD-"].update(eng.Board_Print(eng.Undo(board, choice_history[turn])))
            player = Ui_Turn_Player(window, turn, player)
        elif event in [str(i) for i in range(8)]:
            try:
                choice = int(event) - 1
                choice_history[turn] = choice
                window['-BOARD-'].update(eng.Board_Print(eng.Setmark(board, player, choice)))
            except TypeError:
                psg.popup(f"Row {choice+1} is full. Choose a different row.")
                continue
            if eng.Check_Win(board, player):
                window.refresh()
                psg.popup(f"Win for player {eng.Player_Mark(player)}!")
                winner = player
                break
            elif eng.Check_Draw(turn):
                window.refresh()
                psg.popup(TIE_STRING)
                winner = 0
                break
            turn += 1
            player = Ui_Turn_Player(window, turn, player)
    window.close()
    return winner

def Ui_Turn_Player(window, turn, player_current):
    window["-TURN-"].update(Ui_Turn(turn))
    player_current = eng.Player_Switch(player_current)
    window["-PLAYER-"].update(Ui_Player(player_current))
    return player_current

def Ui_Layout(board, player_current, turn):
    layout = [[psg.Text(Ui_Player(player_current), key="-PLAYER-"), psg.Push(), psg.Text(Ui_Turn(turn), key="-TURN-")],
              [psg.Text(eng.Board_Print(board), key="-BOARD-")],
              [psg.Text(Ui_Index())],
              [psg.Button(i) for i in range(1,8)],
              [psg.Button(UNDO_STRING), psg.Button(ABORT_STRING), psg.Button(EXIT_STRING)]]
    return layout

def Ui_Player(player):
    return "Current Player: " + eng.Player_Mark(player)

def Ui_Turn(turn):
    return "Turn: " + str(turn)

def Ui_Index():
    indices = ""
    for i in range(1,8):
        indices = indices + str(i) + "\t"
    return indices