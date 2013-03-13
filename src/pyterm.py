'''
@author: Friedrich Paetzke
'''

_TURN_OFF_CHARACTER_ATTS = '\033[0m'
_TURN_BOLD_MODE_ON = '\033[1m'
_TURN_UNDERLINE_MODE_ON = '\033[4m'
_TURN_BLINKING_MODE_ON = '\033[5m'


class Color:
    Black = '\033[0;30m'
    Red = '\033[0;31m'
    Green = '\033[0;32m'
    Brown = '\033[0;33m'
    Blue = '\033[0;34m'
    Purple = '\033[0;35m'
    Cyan = '\033[0;36m'
    LightGrey = '\033[0;37m'
    DarkGrey = '\033[1;30m'
    LightRed = '\033[1;31m'
    LightGreen = '\033[1;32m'
    Yellow = '\033[1;33m'
    LightBlue = '\033[1;34m'
    LightPurple = '\033[1;35m'
    LightCyan = '\033[1;36m'
    White = '\033[1;37m'


class BgColor:
    Black = '\033[40;1m'
    Red = '\033[41;1m'
    Green = '\033[42;1m'
    Brown = '\033[43;1m'
    Blue = '\033[44;1m'
    Purple = '\033[45;1m'
    Cyan = '\033[46;1m'
    Grey = '\033[47;1m'


def fancyPrint(s, bold=False, underline=False, blinking=False, color=None,
               bgcolor=None, end='\n'):
    s = sFancyPrint(s, bold=bold, underline=underline, blinking=blinking,
                    color=color, bgcolor=bgcolor)
    print(s, end=end)


def sFancyPrint(s, bold=False, underline=False, blinking=False, color=None,
                bgcolor=None):
    '''
    @return: str
    '''
    fmt = ''
    for val in [bgcolor, color]:
        if val:
            fmt += val

    if bold:
        fmt += _TURN_BOLD_MODE_ON
    if underline:
        fmt += _TURN_UNDERLINE_MODE_ON
    if blinking:
        fmt += _TURN_BLINKING_MODE_ON

    return fmt + s + _TURN_OFF_CHARACTER_ATTS


def updateLine(s):
    '''
    @type s: str
    '''
    print('\033[2K\r' + s, end='')
