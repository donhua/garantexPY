#!/usr/bin/env python3

import PySimpleGUI as sg
import time
exit()
layout = [[sg.Output(size=(60,10))],
          [sg.Button('Go'), sg.Button('Exit')]  ]




window = sg.Window('Window Title', layout)
while True:             # Event Loop
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Go':
        while True:
            print(f"This time: {time.gmtime()}")
            print("================")

window.close()