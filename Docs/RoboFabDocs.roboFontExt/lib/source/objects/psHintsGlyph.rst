PostScript glyph hint values
============================

Usage
-----

.. code::

    # example of accessing the hint data.
    # from robofab.world import CurrentFont

Description
-----------

``PostScriptGlyphHintValues`` is the class of the object found at ``aGlyph.psHints``. It has a couple of attributes of its own which give you access to the glyph level PostScript hint information. 

The ``PostScriptGlyphHintValues`` objects, in FontLab and NoneLab flavor, can respond to ``add``, ``sub``, ``mul``, ``rmul``, ``div`` and ``rdiv``, so you can do math with them, for instance interpolations. Available since `ChangeSet 44`_.

.. _ChangeSet 44: http://code.robofab.com/changeset/44

Attributes
^^^^^^^^^^

.. py:attribute:: hHints

List of (position, width) tuples for horizontal.

.. py:attribute:: vHints

List of (position, width) tuples.

Methods
^^^^^^^

.. py:function:: copy()

Returns a copy of the object. Both in FontLab and NoneLab the copy will be an ``objectsRF.PostScriptFontHintValues``.

.. py:function:: round()

Round the values to ints as much as the nature of the values allows.

.. note::

    - ``blueScale`` is not rounded, it is a float.
    - ``forceBold`` is set to ``False`` if ``-0.5 < value < 0.5``. Otherwise it will be ``True``.
    - ``blueShift``, ``blueFuzz`` are rounded to integers.
    - ``stems`` are rounded to integers.
    - ``blues`` are rounded to integers.

.. py:function:: asDict()

Returns a dictionary with all attributes and values of this object.

.. py:function:: fromDict(aDict)

Rhis will look for familiar attributes in ``aDict`` and assign the value to the object.

.. py:function:: update(anotherPSHintsObject)

This will copy values from the other object.
