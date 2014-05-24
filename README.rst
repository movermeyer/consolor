consolor
========

.. image:: https://travis-ci.org/paetzke/consolor.png?branch=master
  :target: https://travis-ci.org/paetzke/consolor
.. image:: https://coveralls.io/repos/paetzke/consolor/badge.png?branch=master
  :target: https://coveralls.io/r/paetzke/consolor?branch=master
.. image:: https://pypip.in/v/consolor/badge.png
  :target: https://pypi.python.org/pypi/consolor/

Consolor provides highlighting functions for terminals.

It comes with there 3 functions:

get_line
    Returns a string with the given formatting.

print_line
    Prints a string with the given formatting.

update_line
    Overwrites the output of the current line and prints s on the same line without a new line.

All these functions accept the following formatting parameters:

* *bold*: bool, default False
* *underline*: bool, default False
* *blinking*: bool, default False
* *color*: str, default None
* *bgcolor*: str, default None

.. image:: http://vanneva.com/static/images/consolor.png

Some examples:

.. code:: python

    import consolor
    
    consolor.print_line('light green', color=consolor.Color.LightGreen)
    consolor.print_line('underline', underline=True)
    consolor.print_line('green bg', bgcolor=consolor.BgColor.Green)
    consolor.update_line('0%')
    consolor.update_line('100%')
    print()

For more colors and background colors see *consolor.Color* and *consolor.BgColor*.

You can also use it in builtin *print()*:

.. code:: python

    import consolor
    
    print(consolor.Color.Red, 'Red')
    print('Red two')
    print(consolor.Color.Reset, end='') # You have to handle resetting your self.
    print('Not Red')
    
    print(consolor.BgColor.Red, 'Red')
    print('Red two', consolor.BgColor.Reset)
    print('None')

To install ``consolor`` use pip.

.. code:: python

    pip install consolor

CREDITS
-------

Thanks to:

* Benjamin Hedrich (https://github.com/bh)
* Dirk Geschwandtner for testing

CHANGELOG
---------

0.1.2
~~~~~

* Switch from README.org to README.rst This enables you to install this package directly from a git repository.

0.1.1
~~~~~

* Enable usage of foreground and background color at the same time

0.1.0
~~~~~

* Add support for PyPy

0.0.3
~~~~~

* Enable coloring in builtin *print()*

Links
-----

* `http://ascii-table.com/ansi-escape-sequences-vt-100.php <http://ascii-table.com/ansi-escape-sequences-vt-100.php>`_
* `http://wiki.ubuntuusers.de/Bash/Prompt <http://wiki.ubuntuusers.de/Bash/Prompt>`_

Copyright (c) 2013-2014, Friedrich Paetzke (paetzke@fastmail.fm). All rights reserved.

