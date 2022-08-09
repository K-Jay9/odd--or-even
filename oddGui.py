import PySimpleGUI as sg


# Layout matrix
layout = [
    [sg.Text("Number")],
    [sg.Button("Check")],
    []
]

# The window definition
window = sg.Window("Odd or Even",layout)

# Event loop

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break


window.close()