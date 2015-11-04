========================
OpenType features in UFO
========================

The UFO specification does not have an explicit place or format for OpenType features. This has lead to some misunderstanding that it is not possible to work with OpenType features in UFO. This is not the case. Feature data can be stored in the ufo and manipulated. For instance, FontLab exports and imports feature data to and from UFO, storing the data in the ``font.lib`` (``font.ufo/lib.plist``) at ``com.robofab.features``. This page describes how the data is currently managed. It's likely this will improve in the future.

--------
Features
--------

Feature data in UFO is stored in ``font.lib['com.robofab.features']``. This is a dictionary with the four-letter feature tag as key and the feature text as value. As of RoboFab version 1.1.2, the order of the features is stored in ``font.lib['com.robofab.featureorder']``. Older UFO's without this entry will get their features imported in alphabetical order. OpenType classes are stored in ``font.groups`` (``ufo/groups.plist``):

.. showcode:: ../../Examples/howtos/otFeatures_00.py

.. code::

    ["com.robofab.features"]
    ['ss01', 'liga', 'dlig']
    "feature liga {
        sub f f i by ffi;
        sub f f l by ffl;
    } liga;"
    ['liga', 'dlig', 'ss01']

Note that the feature data in the lib is used for storage in UFO. This data won't be available in robofab font objects in FontLab, where it makes more sense to address the FL objects directly. `Check the FL docs here <http://dev.fontlab.net/flpydoc/>`_.

.. showcode:: ../../Examples/howtos/otFeatures_01.py

.. code::

    [<TagObject: tag=liga, value=feature ln..., parent: 'MyFont'>,
    <TagObject: tag=dlig, value=feature ln..., parent: 'MyFont'>]

------------
Kerning data
------------

Kerning is stored in ``font.kerning``, an object which behaves like a dictionary. A ``(name, name)`` tuple is the key. This can either be a glyph name or a group name. A number is the value. Can be floating point or integer:

.. showcode:: ../../Examples/howtos/kerning_00.py

.. code::

    [('a', 'v'), ('MMK_L_baseserif', 'n')]
    -100

------------------------------------
Why no RoboFab objects for features?
------------------------------------

Features are tricky things. On one level they're stored as simple pieces of text. On another level they're sets of complex rules which need to be executed. When the RoboFab API and UFO spec started, writing an interpreter for feature language was too far off. So we chose for a loose method of storing the data, just bits of text, which would get the data where it needed to go and back again. And leave the interpreting and executing to other applications.
