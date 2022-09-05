import PySimpleGUI as sg
from odd import decider

# The theme of the gui
sg.theme("DarkAmber")


#To preview all available themes
# sg.theme_previewer()


# Layout matrix
layout = [
    [sg.T(' '  * 5),sg.Text("Type the Integer:", font=("Serif", 14))],
    [sg.T(' '  * 15)],
    [sg.Input(key="msemo", size=(30,15))],
    [sg.T(' '  * 15)],
    [sg.T(' '  * 15),sg.Button("Check", font='Serif')],
    [sg.T(' '  * 15)],
    [sg.T(' '  * 10),sg.Text('', size=(10, 5), font=('Serif'), justification='center', key='output')]
]

# The window definition
window = sg.Window("Odd or Even",layout)

# Event loop

n = 11

while True:
    event, values = window.read()

    # Closing the window options
    if event == "Check":
        # Catching non integer entered by the user
        try:
            # Return output from the engine
            fin = decider(int(values["msemo"]))

            # Update display with different colors
            if fin == "ODD!":
                window["output"].update(fin, text_color='gray')
            else:
                window["output"].update(fin, text_color='green')


        except ValueError:
              # Update the display
            window["output"].update("Type a valid integer!!!", text_color='red')

    if event == sg.WIN_CLOSED or event == "Exit":
        break

# Closing the window when loop is broken
window.close()


'''
Wakatime has not yet worked on VScode but I hope it will
'''