import PySimpleGUI as psg
import engine as eng

def menu():
    scoreboard = [0]*3
    window = psg.Window("Connect 4 Menu", Layout_Menu(scoreboard))
    while True:
        event, values = window.read()
        if event in (psg.WIN_CLOSED, "Exit Game"):
            break
        elif event == "Start Round":
            winner = round.Round()
            if winner == -1:
                break
            scoreboard[winner] += 1
    window.close()

def Layout_Menu(scoreboard):
    layout = [[psg.Text("Scoreboard")],
              [psg.Text(Ui_Scoreboard(scoreboard), key="-Scoreboard-")],
              [psg.Button("Start Round"), psg.Button("Exit Game")]]
    return layout

def Ui_Scoreboard(scoreboard):
    string = "Draw: " + "\t" + str(scoreboard[0]) + "\n" 
    string += "Player " + str(eng.Player_Mark(1)) + "\t" + str(scoreboard[1]) + "\n"
    string += "Player " + str(eng.Player_Mark(2)) + "\t" + str(scoreboard[2]) + "\n"  
    return string
