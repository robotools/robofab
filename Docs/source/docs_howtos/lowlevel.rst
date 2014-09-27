=================================
How to get to FontLab's internals
=================================

If you're using RoboFab in FontLab, it can happen that you need to access a method or attribute of a glyph or font object which does not seem to have an equivalent in RoboFab. What to do?

---------
Get Naked
---------

RoboFab ``Glyph`` and ``Font`` objects have a special method, ``naked()`` which returns the actual, low level FontLab object. This object can then be used with the documented FontLab methods and attributes. The methods and attributes of these FontLab objects are very different from RoboFab:

.. showcode:: ../../Examples/howtos/lowLevel_00.py

.. code::

    < RFont font for TemplatefontPro Rg Regular >
    < Font 'TemplatefontPro Rg Regular' >
