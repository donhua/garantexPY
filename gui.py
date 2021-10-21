#!/usr/bin/env python3

import PySimpleGUI as sg

layout = [[sg.Output(size=(60,10))],
          [sg.Button('Go'), sg.Button('Exit')]  ]




window = sg.Window('Window Title', layout)
while True:             # Event Loop
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Go':
        '''Тут запуск мониторинга'''
        print("Start monitoring")
        print("================")

window.close()