============================
PostScript glyph hint values
============================

-----
Usage
-----

.. code::

    # example of accessing the hint data.
    # from robofab.world import CurrentFont

-----------
Description
-----------

``PostScriptGlyphHintValues`` is the class of the object found at ``aGlyph.psHints``. It has a couple of attributes of its own which give you access to the glyph level PostScript hint information. 

The ``PostScriptGlyphHintValues`` objects, in FontLab and NoneLab flavor, can respond to ``add``, ``sub``, ``mul``, ``rmul``, ``div`` and ``rdiv``, so you can do math with them, for instance interpolations. Available since `ChangeSet 44`_.

.. _ChangeSet 44: http://code.robofab.com/changeset/44

^^^^^^^^^^
Attributes
^^^^^^^^^^

.. py:attribute:: hHints

List of (position, width) tuples for horizontal.

.. py:attribute:: vHints

List of (position, width) tuples.

^^^^^^^
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

^^^^^^^^
Examples
^^^^^^^^

.. code::

    #FLM: Get and set font level PostScript hint data.
    from robofab.world import CurrentFont
     
    """
    This script shows the way to get to the font level postscript hint values.
    These values were available from the fl layer, but not in RoboFab.
    Now they're available in RoboFab in a slightly easier to use format.
    The values also export to UFO and import from UFO.
    
    Check the FontLab FontInfo panel / Hinting Settings
     
    """
 
    f = CurrentFont()
     
    # the fontlevel postscript hint data is accessible through the psHints attribute
     
    print
    print "This script shows the attributes of psHints:", f.psHints
     
    # now let's have a look at the values
    # blueScale, blueShift, blueFuzz and forceBold are all single values.
     
    print "blueScale", f.psHints.blueScale
    f.psHints.blueScale = .5
    print "blueScale changed", f.psHints.blueScale
     
    print "blueShift", f.psHints.blueShift
    f.psHints.blueShift = 5
    print "blueShift changed", f.psHints.blueShift
     
    print "blueFuzz", f.psHints.blueFuzz
    f.psHints.blueFuzz = 0
    print "blueFuzz changed", f.psHints.blueFuzz
     
    print "forceBold", f.psHints.forceBold
    f.psHints.forceBold = 1
    print "forceBold changed", f.psHints.forceBold
     
    # the following values are represented as lists.
    # Important Note: you can only set the whole list, not individual items.
    # So get the list, make changes to it, then set the list
    # Zones are represented as tuples of integers, so it's easier to
    # see which values belong together. FL stores the values as
    # a single list of numbers.
     
    # T1 spec says blueValues, FL says Primary Alignment Zones, under "Set Local Alignment Zones".
    print "blueValues", f.psHints.blueValues
    # remove the last zone
    f.psHints.blueValues = f.psHints.blueValues[:-1]
    print "blueValues changed", f.psHints.blueValues
    # add a new zone
    f.psHints.blueValues = f.psHints.blueValues + [(750, 770)]
    print "blueValues changed", f.psHints.blueValues
     
    # T1 spec says otherBlues, FL says Secondary Alignment Zones, under "Set Local Alignment Zones".
    print "otherBlues", f.psHints.otherBlues
    # remove the last zone
    f.psHints.otherBlues = f.psHints.otherBlues[:-1]
    print "otherBlues changed", f.psHints.otherBlues
    # add a new zone
    f.psHints.otherBlues = f.psHints.otherBlues + [(750, 770)]
    print "otherBlues changed", f.psHints.otherBlues
     
    # T1 spec says familyBlues, FL says Primary Alignment Zones, under "Set Family Alignment Zones".
    print "familyBlues", f.psHints.familyBlues
    # remove the last zone
    f.psHints.familyBlues = f.psHints.familyBlues[:-1]
    print "familyBlues changed", f.psHints.familyBlues
    # add a new zone
    f.psHints.familyBlues = f.psHints.familyBlues + [(750, 770)]
    print "familyBlues changed", f.psHints.familyBlues
     
    # T1 spec says familyOtherBlues, FL says Seconday Alignment Zones, under "Set Family Alignment Zones".
    print "familyOtherBlues", f.psHints.familyOtherBlues
    # remove the last zone
    f.psHints.familyOtherBlues = f.psHints.familyOtherBlues[:-1]
    print "familyOtherBlues changed", f.psHints.familyOtherBlues
    # add a new zone
    f.psHints.familyOtherBlues = f.psHints.familyOtherBlues + [(750, 770)]
    print "familyOtherBlues changed", f.psHints.familyOtherBlues
     
    # The horizontal stems are represented as a list of single values.
    print "hStems", f.psHints.hStems
    f.psHints.hStems = f.psHints.hStems[:-1]
    print "hStems changed", f.psHints.hStems
    # add a new stem
    f.psHints.hStems = f.psHints.hStems + [100]
    print "hStems changed", f.psHints.hStems
     
    # The vertical stems are represented as a list of single values.
    print "vStems", f.psHints.vStems
    f.psHints.vStems = f.psHints.vStems[:-1]
    print "vStems changed", f.psHints.vStems
    # add a new stem
    f.psHints.vStems = f.psHints.vStems + [100]
    print "vStems changed", f.psHints.vStems
     