#!/usr/bin/env python3

import PySimpleGUI as sg
from gar_modul import GarantexIo, CalculateFin_1

gi = GarantexIo.GarantexIo()

def thistime():
    named_tuple = time.localtime() # получить struct_time
    time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
    return time_string
ss = 1
layout = [[sg.Output(size=(60,10))],
          [sg.Button('Go'), sg.Button('Pause')]  ]

window = sg.Window('Window Title', layout)

while True:             # Event Loop
    event, values = window.read(timeout=1000)
    if event == sg.WIN_CLOSED:
        exit()
        break

    if event == 'Pause':
        quit()
  
    print(thistime())
window.close()
