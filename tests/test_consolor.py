# -*- coding: utf-8 -*-
"""
consolor

Copyright (c) 2013-2014, Friedrich Paetzke (f.paetzke@gmail.com)
All rights reserved.

"""
from __future__ import print_function

from consolor import BgColor, Color, get_line

try:
    from unittest.mock import call, patch
except ImportError:
    from mock import call, patch


def mockable_print(*args, **kwargs):
    print(*args, **kwargs)


def test_print_bold():
    result = get_line('123 bold', bold=True)
    expected = '\x1b[1m123 bold\x1b[0m'
    assert result == expected


def test_print_underline():
    result = get_line('123 underline', underline=True)
    expected = '\x1b[4m123 underline\x1b[0m'
    assert result == expected


def test_get_bgcolor():
    result = get_line('123 green bg', bgcolor=BgColor.Green)
    expected = '\x1b[42;1m123 green bg\x1b[0m'
    assert result == expected


def test_get_color():
    result = get_line('123 light green', color=Color.LightGreen)
    expected = '\x1b[1;32m123 light green\x1b[0m'
    assert result == expected


def test_update_line():
    for i in reversed(range(101)):
        line = get_line('123%d' % i, update_line=True)
        expected = '\x1b[2K\r%s%d\x1b[0m' % ('123', i)
        assert line == expected


@patch('tests.test_consolor.mockable_print')
def test_print_color(mocked_print):
    mockable_print(Color.Red, 'Red')
    mockable_print('Red two')
    mockable_print(Color.Reset, end='')
    mockable_print('Not Red')

    mocked_print.assert_has_calls([call('\x1b[0;31m', 'Red'),
                                   call('Red two'),
                                   call('\x1b[0m', end=''),
                                   call('Not Red')])


@patch('tests.test_consolor.mockable_print')
def test_print_concat_color(mocked_print):
    mockable_print(Color.Red, 'Red')
    mockable_print('Red two')
    mockable_print(Color.Blue, 'Blue')
    mockable_print(Color.Reset, end='')
    mockable_print('Not Blue')

    mocked_print.assert_has_calls([call('\x1b[0;31m', 'Red'),
                                   call('Red two'),
                                   call('\x1b[0;34m', 'Blue'),
                                   call('\x1b[0m', end=''),
                                   call('Not Blue')])


@patch('tests.test_consolor.mockable_print')
def test_print_bgcolor(mocked_print):
    mockable_print(BgColor.Red, 'Red')
    mockable_print('Red two', BgColor.Reset)
    mockable_print('None')

    mocked_print.assert_has_calls([call('\x1b[41;1m', 'Red'),
                                   call('Red two', '\x1b[0m'),
                                   call('None')])


@patch('tests.test_consolor.mockable_print')
def test_print_concat_bgcolor(mocked_print):
    mockable_print(BgColor.Red, 'Red')
    mockable_print('Red two')
    mockable_print(BgColor.Cyan, 'None')
    mockable_print(BgColor.Reset)

    mocked_print.assert_has_calls([call('\x1b[41;1m', 'Red'),
                                   call('Red two'),
                                   call('\x1b[46;1m', 'None'),
                                   call('\x1b[0m')])


def test_color_and_bgcolor():
    result = get_line('1', bgcolor=BgColor.Green, color=Color.Red)
    expected = '\x1b[0;31m\x1b[42;1m1\x1b[0m'
    assert result == expected
