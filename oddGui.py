import PySimpleGUI as sg
from odd import decider

# The theme of the gui
sg.theme("DarkAmber")



# Layout matrix
layout = [
    [sg.Text("Number")],
    [sg.Input(key="msemo")],
    [sg.Button("Check")],
    [sg.Button("Exit")],
]

# The window definition
window = sg.Window("Odd or Even",layout)

# Event loop

n = 11

while True:
    event, values = window.read()

    # Closing the window options
    if event == "Check":
        try:
            fin = decider(int(values["msemo"]))
            print(fin)
        except ValueError:
            print("Type a valid integer!!!") 

    if event == sg.WIN_CLOSED or event == "Exit":
        break

# Closing the window when loop is broken
window.close()


'''
Wakatime has not yet worked on VScode but I hope it will
'''