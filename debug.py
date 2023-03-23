import PySimpleGUI as sg

layout = []
layout = [[sg.Button(str(i)) for i in range(1,6)]]
layout += [[sg.Button("Exit")]]

window = sg.Window("Debug", layout)

event, values = window.read()