# -*- coding: utf-8 -*-
"""
consolor

Copyright (c) 2013, Friedrich Paetzke (f.paetzke@gmail.com)
All rights reserved.

"""
import unittest

import consolor


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


if __name__ == '__main__':
    unittest.main()
