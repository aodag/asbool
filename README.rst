==================
asbool
==================

.. image:: https://travis-ci.org/aodag/asbool.svg?branch=master
               :target: https://travis-ci.org/aodag/asbool

``asbool`` is simple converter from ``str`` to ``bool``.

INSTALL
======================

use pip to install ``asbool``.

::

   pip install asbool

USAGE
==================

You can use ``asbool.asbool`` function simply.

::

   >>> from asbool import asbool
   >>> asbool('TRUE')
   True

Or use ``AsBoolConverter`` instance with customized values.

::

   >>> from asbool.converter import AsBoolConverter
   >>> converter = AsBoolConverter(['t'], ['f'])
   >>> converter('t')
   True
   >>> converter('f')
   False
   >>> converter('true')
   Traceback (most recent call last):
       ...
   raise ValueError(ss)
   ValueError: true
