# -*- coding: utf-8 -*-
"""
consolor

Copyright (c) 2013-2014, Friedrich Paetzke (f.paetzke@gmail.com)
All rights reserved.

"""
from __future__ import print_function
import unittest

import consolor

try:
    from unittest.mock import call, patch
except ImportError:
    from mock import call, patch


def mockable_print(*args, **kwargs):
    print(*args, **kwargs)


class TestConsolor(unittest.TestCase):

    def test_print_bold(self):
        result = consolor.get_line('123 bold', bold=True)
        expected = '\x1b[1m123 bold\x1b[0m'
        self.assertEqual(result, expected)

    def test_print_underline(self):
        result = consolor.get_line('123 underline', underline=True)
        expected = '\x1b[4m123 underline\x1b[0m'
        self.assertEqual(result, expected)

    def test_get_bgcolor(self):
        result = consolor.get_line('123 green bg', bgcolor=consolor.BgColor.Green)
        expected = '\x1b[42;1m123 green bg\x1b[0m'
        self.assertEqual(result, expected)

    def test_get_color(self):
        result = consolor.get_line('123 light green', color=consolor.Color.LightGreen)
        expected = '\x1b[1;32m123 light green\x1b[0m'
        self.assertEqual(result, expected)

    def test_update_line(self):
        for i in reversed(range(101)):
            line = consolor.get_line('123%d' % i, update_line=True)
            expected = '\x1b[2K\r%s%d\x1b[0m' % ('123', i)
            self.assertEqual(line, expected)

    def test_print_color(self):
        with patch('tests.test_consolor.mockable_print') as mocked_print:
            mockable_print(consolor.Color.Red, 'Red')
            mockable_print('Red two')
            mockable_print(consolor.Color.Reset, end='')
            mockable_print('Not Red')

            mocked_print.assert_has_calls([call('\x1b[0;31m', 'Red'),
                                           call('Red two'),
                                           call('\x1b[0m', end=''),
                                           call('Not Red')])

    def test_print_concat_color(self):
        with patch('tests.test_consolor.mockable_print') as mocked_print:
            mockable_print(consolor.Color.Red, 'Red')
            mockable_print('Red two')
            mockable_print(consolor.Color.Blue, 'Blue')
            mockable_print(consolor.Color.Reset, end='')
            mockable_print('Not Blue')

            mocked_print.assert_has_calls([call('\x1b[0;31m', 'Red'),
                                           call('Red two'),
                                           call('\x1b[0;34m', 'Blue'),
                                           call('\x1b[0m', end=''),
                                           call('Not Blue')])

    def test_print_bgcolor(self):
        with patch('tests.test_consolor.mockable_print') as mocked_print:
            mockable_print(consolor.BgColor.Red, 'Red')
            mockable_print('Red two', consolor.BgColor.Reset)
            mockable_print('None')

            mocked_print.assert_has_calls([call('\x1b[41;1m', 'Red'),
                                           call('Red two', '\x1b[0m'),
                                           call('None')])

    def test_print_concat_bgcolor(self):
        with patch('tests.test_consolor.mockable_print') as mocked_print:
            mockable_print(consolor.BgColor.Red, 'Red')
            mockable_print('Red two')
            mockable_print(consolor.BgColor.Cyan, 'None')
            mockable_print(consolor.BgColor.Reset)

            mocked_print.assert_has_calls([call('\x1b[41;1m', 'Red'),
                                           call('Red two'),
                                           call('\x1b[46;1m', 'None'),
                                           call('\x1b[0m')])
