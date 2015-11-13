PostScript font hint values
===========================

The ``font.psHints`` object, introduced in RoboFab 1.1.3 rev.89 showed it was useful to have access to the various PostScript blues values. But it also proved it was necessary to store them elsewhere. So in RoboFab 1.2 rev.172, the blues values found a permanent home in the new ``RInfo`` object. The ``font.psHints`` object is still functional, all fields are rerouted to their new places. The ``font.psHint`` attribute might be deprecated in the future.

Note on accessing blues data in FontLab Studio
----------------------------------------------

A bug in FontLab's own Python attributes relating to blues, ``otherBlues``, ``familyBlues`` and ``familyOtherBlues`` fields, makes it impossible to set the full number of zones using Python. The actual number of zones which can be set from Python is one less than the number in the Adobe specification. A warning will be printed when a zone will be dropped. Using the FontLab font info dialog, all zones can be set.

The font.info attributes (since RoboFab 1.2)
--------------------------------------------

.. py:attribute:: font.info.postscriptBlueValues

(number list) A list of up to 14 integers or floats specifying the values that should be in the Type 1/CFF ``BlueValues`` field. This list must contain an even number of integers following the rules defined in the Type 1/CFF specification.

.. py:attribute:: font.info.postscriptOtherBlues

(number list) A list of up to 10 integers or floats specifying the values that should be in the Type 1/CFF ``OtherBlues`` field. This list must contain an even number of integers following the rules defined in the Type 1/CFF specification.

.. py:attribute:: font.info.postscriptFamilyBlues

(number list) A list of up to 14 integers or floats specifying the values that should be in the Type 1/CFF ``FamilyBlues`` field. This list must contain an even number of integers following the rules defined in the Type 1/CFF specification.

.. py:attribute:: font.info.postscriptFamilyOtherBlues

(number list) A list of up to 10 integers or floats specifying the values that should be in the Type 1/CFF ``FamilyOtherBlues`` field. This list must contain an even number of integers following the rules defined in the Type 1/CFF specification.

.. py:attribute:: font.info.postscriptStemSnapH

(number list) List of horizontal stems sorted in increasing order. Up to 12 integers or floats are possible. This corresponds to the Type 1/CFF ``StemSnapH`` field.

.. py:attribute:: font.info.postscriptStemSnapV

(number list) List of vertical stems sorted in increasing order. Up to 12 integers or floats are possible. This corresponds to the Type 1/CFF ``StemSnapV`` field.

.. py:attribute:: font.info.postscriptBlueFuzz

(integer or float) BlueFuzz value. This corresponds to the Type 1/CFF ``BlueFuzz`` field.

.. py:attribute:: font.info.postscriptBlueShift

(integer or float) BlueShift value. This corresponds to the Type 1/CFF ``BlueShift`` field.

.. py:attribute:: font.info.postscriptBlueScale

(float) BlueScale value. This corresponds to the Type 1/CFF ``BlueScale`` field.

.. py:attribute:: font.info.postscriptForceBold

(boolean) Indicates how the Type 1/CFF ``ForceBold`` field should be set.

Example, some font.info blues attrs, usage
------------------------------------------

.. showcode:: ../../examples/objects/psHints_00.py

.. code::

    [-8, 0, 200, 208, 214, 114]
    [-136, -128, -86, -84, 376, 386]
    [-8, 0, 200, 208, 214, 224]
    [-136, -128, -86, -84, 376, 386]

Description of the font.psHint object
-------------------------------------

``PostScriptFontHintValues`` is the class of the object found at ``font.psHints``. It has a couple of attributes of its own which give you access to the font level PostScript hinting information. For exact information on the meaning and usage of these values, please refer to the developer resources at `adobe.com`_.

.. _adobe.com: <http://adobe.com>

The ``PostScriptFontHintValues`` objects, in FontLab and NoneLab flavor, can respond to ``add``, ``sub``, ``mul``, ``rmul``, ``div`` and ``rdiv``, so you can do math with them, for instance interpolations. Available since `ChangeSet 44`_.

.. _ChangeSet 44: http://code.robofab.com/changeset/44

Example, the font.psHints object, usage
---------------------------------------

.. showcode:: ../../examples/objects/psHints_01.py

.. code::

    { 'forceBold': False, 'blueScale': 0.25, 'blueFuzz': 0,
    'blueShift': 4, 'hStems': [24, 50], 'vStems': [66, 4, 30, 72, 50],
    'blueValues': [[-8, 0], [200, 208], [214, 224]],
    'otherBlues': [[-136, -128], [-86, -84], [376, 386]],
    'familyOtherBlues': [[-136, -128], [-86, -84], [376, 386]],
    'familyBlues': [[-8, 0], [200, 208], [214, 224]], }

.. showcode:: ../../examples/objects/psHints_02.py

Attributes
----------

.. py:attribute:: blueShift

Value for blue shift. Integer in FontLab, float or int in NoneLab.

.. py:attribute:: blueScale

Value for blue scale. Float in FontLab and NoneLab.

.. py:attribute:: blueFuzz

Value for blue fuzz. Integer in FontLab, float or int in NoneLab.

.. py:attribute:: forceBold

Value for force bold. Boolean in FontLab and NoneLab.

.. py:attribute:: blueValues

List of pairs of numbers indicating the primary alignment zones. Integers in FontLab, floats or ints in NoneLab.

.. py:attribute:: otherBlues

List of pairs of numbers indicating the secondary alignment zones. Integers in FontLab, floats or ints in NoneLab.

.. py:attribute:: familyBlues

List of pairs of numbers indicating the primary family alignment zones. Integers in FontLab, floats or ints in NoneLab.

.. py:attribute:: familyOtherBlues

List of pairs of numbers indicating the secondary family alignment zones. Integers in FontLab, floats or ints in NoneLab.

.. py:attribute:: vStems

List of numbers for the vertical stems. Integers in FontLab, floats or ints in NoneLab.

.. py:attribute:: hStems

List of numbers for the horizontal stems. Integers in FontLab, floats or ints in NoneLab.

Methods
-------

.. py:function:: copy

Returns a copy of the object. Both in FontLab and NoneLab the copy will be an ``objectsRF.PostScriptFontHintValues``.

.. py:function:: round

Round the values to ints as much as the nature of the values allows. Note: ``blueScale`` is not rounded, it is a ``float``, ``forceBold`` is set to ``False`` if ``-0.5 < value < 0.5``. Otherwise it will be ``True``, ``blueShift``, ``blueFuzz`` are rounded to ``int``, stems are rounded to ``int``, blues are rounded to ``int``.

.. py:function:: asDict

Returns a dictionary with all attributes and values of this object.

.. py:function:: fromDict(aDict)

This will look for familiar attributes in ``aDict`` and assign the value to the object.

.. py:function:: update(anotherPSHintsObject)

This will copy values from the other object.

Examples
--------

.. showcode:: ../../examples/objects/psHints_03.py
