=====
RFont
=====

-----
Usage
-----

.. showcode:: ../../Examples/objects/RFont_00.py

-----------
Description
-----------

Perhaps the first object you get to play with. The ``RFont`` object is the central part that connects all glyphs with font information (like names, key dimensions etc.). In FontLab the ``RFont`` object talks directly to the glyphs and font data in the FontLab font it belongs to. In UFO or NoneLab use, the ``RFont`` object contains the data and saves it to UFO. ``RFont`` object behave like dictionaries: the glyphname is the key and the returned value is a :doc:`RGlyph` object for that glyph. If the glyph does not exist ``RFont`` will raise an ``IndexError``.

``RFont`` has a couple of important sub-objects which are worth checking out. The font's kerning is stored in a :doc:`RKerning` object and can be reached as an attribute at ``RFont.kerning``. Fontnames, key dimensions, flags etc are stored in a :doc:`RInfo` object which is available through ``RFont.info``. The ``RFont.lib`` is an :doc:`RLib <libs>` object which behaves as a dictionary.

---------
Iterating
---------

One of the most important uses of the ``RFont`` object is that it makes it really easy to iterate ("step through") the glyphs in the font.

.. showcode:: ../../Examples/objects/RFont_01.py

This makes the code clear and simple.

-------------
FontLab / UFO
-------------

All basic attributes, methods and behaviour for ``RFont`` objects created in FontLab or in NoneLab are identical. However, the ``RFont`` objects in FontLab have some additional attributes and methods that make special FontLab functionality available. These extra methods and attributes are listed seperately below.

----------------
RFont Attributes
----------------

.. py:attribute:: path

The path to the font. (read only)

.. py:attribute:: kerning

The :doc:`RKerning` object. Cache the ``font.kerning`` object to optimise your script for speed:

.. showcode:: ../../Examples/objects/RFont_02.py

.. py:attribute:: info

The :doc:`RInfo` object with all the font's names and key dimensions.

.. py:attribute:: lib

The lib object which behaves like a dictionary for arbitrary data that needs to be stored with the font. In FontLab the lib is stored in the ``.vfb`` file. In UFO based fonts the lib is a separate ``.plist`` file. Have a look at how to use the lib.

.. py:attribute:: fileName

The filename and path of this font.

.. py:attribute:: psHints

A :doc:`PostScriptFontHintValues <psHints>` object with all font level PostScript hinting information, such as the blue values and stems.

------------------
Attribute examples
------------------

.. showcode:: ../../Examples/objects/RFont_03.py

------------------------------------------
RFont Methods available in FontLab and UFO
------------------------------------------

.. py:function:: RFont[glyphName]

Asking the font for a glyph by ``glyphName`` like a dictionary.

.. py:function:: has_key(glyphName)

Return ``True`` if ``glyphName`` is present in the font.

.. py:function:: keys()

Return a list of all glyph names in this font.

.. py:function:: newGlyph(glyphName, clear=True)

Create a new, empty glyph in the font with ``glyphName``. If clear is ``True`` (by default) this will clear the glyph if it already exists under this name.

.. note:: ``clear=True`` is now default in both FontLab and NoneLab implementations.

.. py:function:: removeGlyph(glyphName)

Remove a glyph from the font. This method will show a slightly different behaviour in FontLab and pure Python. In FontLab, components that reference the glyph that is being removed will be decomposed. In plain Python, the components will continue to point to the glyph.

.. py:function:: insertGlyph(aGlyph, name=None)

Inserts ``aGlyph`` in the font, the new glyph object is returned. If the font already has a glyph with the same name the exisiting data is deleted. The optional as parameter is an alternative glyph name, to be used if you want to insert the glyph with a different name. 

.. note:: As of robofab svn version 200, the ``as`` argument in ``insertGlyph`` has changed to ``name``. Python2.6+ uses ``as`` as a keyword so it can no longer be used.

.. py:function:: compileGlyph(glyphName, baseName, accentNames, adjustWidth=False, preflight=False, printErrors=True)

Compile components into a new glyph using components and anchorpoints. 

``glyphName``
    The name of the glyph where it all needs to go.

``baseName``
    The name of the base glyph.

``accentNames``
    A list of ``accentName``, ``anchorName`` tuples: ``[('acute', 'top'), etc]``.

.. py:function:: generateGlyph(glyphName, replace=True, preflight=False, printErrors=True)

Generate a glyph and return it. Assembled from ``GlyphConstruction.txt``.

``replace=True``
    The font will replace the glyph if there is already one with this name.

``preflight=True``
    The font will attempt to generate the glyph without adding it to the font.

Do this to find out if there are any problems to make this glyph. For instance missing glyphs or components could be a problem. See :doc:`building accents <../docs_howtos/building_accents>`.

.. py:function:: getReverseComponentMapping

Get a reversed map of component references in the font::

    {
        'A' : ['Aacute', 'Aring']
        'acute' : ['Aacute']
        'ring' : ['Aring']
        #etc.
    }

.. py:function:: save(destDir=None, doProgress=False, saveNow=False)

Save the font.

.. py:function:: autoUnicodes

Using ``fontTools.agl``, assign Unicode lists to all glyphs in the font.

.. py:function:: interpolate

See :doc:`how to interpolate <../docs_howtos/interpolate>` for a detailed description of the interpolate method in ``RFont``.

.. py:function:: round

Round all of the coordinates in all of the glyphs to whole integer numbers. For instance a point at ``(12.3, -10.99)`` becomes ``(12, -11)``. UFO based fonts can deal with floating point coordinates, but for use in FontLab everything needs to be rounded otherwise bad things happen.

.. py:function:: update

Call to FontLab to refresh the font. You call ``update()`` after doing lots of manipulating and editing. In UFO based ``RFont`` objects ``update()`` doesn't do anything, but it exists.

.. py:function:: copy

Returns a deep copy of the font, i.e. all glyphs and all associated data is duplicated.

.. py:function:: getCharacterMapping

Returns a dict of unicode values to glyph names.

---------------
Method examples
---------------

.. showcode:: ../../Examples/objects/RFont_04.py

-------
FontLab
-------

The following attributes and methods are only available to RoboFab objects in FontLab as they're based on application specific features.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
RFont Methods only available in FontLab
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. py:function:: naked

Return the wrapped fontlab font object itself. This can be useful if you want to set very specific values in the fontlab font that aren't wrapped or handled by RoboFab objects.

.. py:function:: writeUFO(self, path=None, doProgress=False, glyphNameToFileNameFunc=None, doHints=False, doInfo=True, doKerning=True, doGroups=True, doLib=True, doFeatures=True, glyphs=None, formatVersion=2)

Write the font to UFO at path.

``doProgress=True``
    Gives you a progressbar if you want.

``glyphNameToFileNameFunc``
    An optional callback for alternative naming schemes. See :doc:`How to use glyph naming schemes <../docs_howtos/glifnames>`.

The other flags are new in RoboFab 1.2 and give you detailed control of what should and should not be written to UFO. The ``formatVersion`` flag determines the format of the UFO, ``1`` for UFO1, ``2`` for UFO2.

.. py:function:: close()

Close the font object and the font window in FontLab.

.. py:function:: appendHGuide()

Append a horizontal guide.

.. py:function:: appendVGuide()

Append a vertical guide.

.. py:function:: clearHGuides()

Clear all horizontal guides.

.. py:function:: clearVGuides()

Clear all vertical guides.

.. py:function:: generate(outputType, path=None)

Call FontLab to generate fonts with these parameters and location. Have a look at :doc:`generate fonts <../docs_howtos/generating_fonts>` for a more detailed description of this method and how to use it.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
RFont Attributes available in FontLab only
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. py:attribute:: selection

A list of selected glyph names in the font window.

^^^^^^^^^^^^^^^^^^
Attribute examples
^^^^^^^^^^^^^^^^^^

.. showcode:: ../../Examples/objects/RFont_05.py
