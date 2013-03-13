#! /usr/bin/env python3
'''
@author: Friedrich Paetzke
@copyright: Copyright (c) 2013 Friedrich Paetzke
'''

import pyterm
import time


def main():
    pyterm.fancyPrint('123')
    pyterm.fancyPrint('123 bold', bold=True)
    pyterm.fancyPrint('123 underline', underline=True)
    pyterm.fancyPrint('123 blinking', blinking=True)
    pyterm.fancyPrint('123 bold underline', bold=True, underline=True)
    pyterm.fancyPrint('123 bold blinking', bold=True, blinking=True)
    pyterm.fancyPrint('123 bold underline red', bold=True, underline=True, color=pyterm.Color.Red)
    pyterm.fancyPrint('123 underline green', underline=True, color=pyterm.Color.Green)
    pyterm.fancyPrint('123 brown', color=pyterm.Color.Brown)
    pyterm.fancyPrint('123 brown bold', bold=True, color=pyterm.Color.Brown)

    pyterm.fancyPrint('123 black', color=pyterm.Color.Black)
    pyterm.fancyPrint('123 red', color=pyterm.Color.Red)
    pyterm.fancyPrint('123 green', color=pyterm.Color.Green)
    pyterm.fancyPrint('123 brown', color=pyterm.Color.Brown)
    pyterm.fancyPrint('123 blue', color=pyterm.Color.Blue)
    pyterm.fancyPrint('123 purple', color=pyterm.Color.Purple)
    pyterm.fancyPrint('123 cyan', color=pyterm.Color.Cyan)
    pyterm.fancyPrint('123 ligth grey', color=pyterm.Color.LightGrey)

    pyterm.fancyPrint('123 dark grey', color=pyterm.Color.DarkGrey)
    pyterm.fancyPrint('123 light red', color=pyterm.Color.LightRed)
    pyterm.fancyPrint('123 light green', color=pyterm.Color.LightGreen)
    pyterm.fancyPrint('123 yellow', color=pyterm.Color.Yellow)
    pyterm.fancyPrint('123 light blue', color=pyterm.Color.LightBlue)
    pyterm.fancyPrint('123 light purple', color=pyterm.Color.LightPurple)
    pyterm.fancyPrint('123 light cyan', color=pyterm.Color.LightCyan)
    pyterm.fancyPrint('123 white', color=pyterm.Color.White)


    pyterm.fancyPrint('123 black bg', bgcolor=pyterm.BgColor.Black)
    pyterm.fancyPrint('123 red bg', bgcolor=pyterm.BgColor.Red)
    pyterm.fancyPrint('123 green bg', bgcolor=pyterm.BgColor.Green)
    pyterm.fancyPrint('123 brown bg', bgcolor=pyterm.BgColor.Brown)
    pyterm.fancyPrint('123 blue bg', bgcolor=pyterm.BgColor.Blue)
    pyterm.fancyPrint('123 purple bg', bgcolor=pyterm.BgColor.Purple)
    pyterm.fancyPrint('123 cyan bg', bgcolor=pyterm.BgColor.Cyan)
    pyterm.fancyPrint('123 grey bg', bgcolor=pyterm.BgColor.Grey)

    for i in range(3):
        pyterm.updateLine('123' + str(i))
        time.sleep(0.5)

    pyterm.fancyPrint('')

    for i in range(3):
        s = pyterm.sFancyPrint(str(i) + '123' + str(i), color=pyterm.Color.Red)
        pyterm.updateLine(s)
        time.sleep(0.5)

    pyterm.fancyPrint('')

    for i in reversed(range(101)):
        pyterm.updateLine('123' + str(i))
        time.sleep(0.1)
    pyterm.fancyPrint('')


if __name__ == '__main__':
    main()
