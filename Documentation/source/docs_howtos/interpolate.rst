==================
How to interpolate
==================

RoboFab's interpolation is independent of the interpolation tools provided in FontLab. First of all that means that you can interpolate UFO fonts without the help of FontLab. It also means that the interpolation engine works different than the one in FontLab.

------
Strict
------

RoboFab interpolation is very strict. It won't interpolate unless the point structures of both extremes match. It won't mess with the masters, force points or anything. The user has to get it right.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
aGlyph.isCompatible(otherGlyph, report=True)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Glyph has a method ``isCompatible()`` which reports whether or not the point structures are capable of interpolating. With this method you can run through your proposed interpolation first and see if all glyphs work, and perhaps send feedback to the user::

    >>> from robofab.world import CurrentFont
    >>> f = CurrentFont()
    >>> a = f["a"]
    >>> print a.isCompatible(f["b"], False)
    False

``isCompatible`` has a flag report which if set to ``True`` will return a tuple with a report on the incompatibilities::

    >>> from robofab.world import CurrentFont
    >>> f = CurrentFont()
    >>> a = f["a"]
    >>> print a.isCompatible(f["b"], True)
    (False, ["Fatal error: contour 0 in glyph a and
    glyph b don't have the same number of segments."])

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
aFont.interpolate(factor, minFont, maxFont, suppressError=True, analyzeOnly=False)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Interpolate by factor between ``minFont`` and ``maxFont``. In FontLab the result of the interpolation will be rounded to whole integers. In NoneLab (outside FontLab, operating on a UFO), the result of the interpolation is a font with glyphs with floating point coordinates so if you want to use the result of one interpolation as a master in the next you won't loose precision to rounding errors. It might mean that for some uses of UFO you need to round the glyphs afterwards. ``aFont.interpolate`` also interpolates the positions of components, anchors, ascender, descender, and glyph widths for the whole font.

``factor``
    Either a number or a tuple of numbers. Usually factor is a float number between ``0`` and ``1``. ``0`` produces ``minGlyph``, ``1`` produces ``maxGlyph``. Values ``>`` extrapolate beyond ``maxGlyph``. Values ``<`` extrapolate beyond ``minGlyph``. If you pass ``(x, y)`` to ``factor`` it will interpolate horizontal values differently from vertical values. For instance ``(0, 1)`` as factor produces a font (or a glyph) which horizontally looks like the minimum, but vertically it looks like the maximum.

``minFont``
    ``RFont`` object, the font for the minimum master.

``maxFont``
    ``RFont`` object, the font for the maximum master.

``suppressError`` (optional)
    Will supress all tracebacks it finds on the way. That means that interpolation problems in individual glyphs won't stop the rest of the font from getting done. Default set to ``True``.

``analyzeOnly`` (optional)
    Will do a dry run of the interpolation and do a full analysis of the compatibility and problems. It won't produce any outlines in the font. Default set to ``False``.

:doc:`Kerning objects <../docs_objects/RKerning>` have an interpolation method as well. It is debateable whether an interpolation of two fonts should also automatically interpolate the kerning, so we picked the more explicit approach: in your interpolation script you have to do the interpolation of the kerning objects seperately.

--------
Examples
--------

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Straight interpolating (either FontLab or UFO)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Setting a third font to an interpolation of two others::

    # robofab manual
    # Interpolate howto
    # Straight Interpolating examples
    
    from robofab.world import OpenFont
    minFont = OpenFont(pathToMinFont)
    maxFont = OpenFont(pathToMaxFont)
    # or any other way you like to get two font objects
     
    inbetweenFont = OpenFont(pathToInbetweenFont)
    # so now we have 3 font objects, right?
     
    inbetweenFont.interpolate(.5, minFont, maxFont)
    # presto, inbetweenFont is now 50% of one and 50% of the other
     
    inbetweenFont.interpolate((.92, .12), minFont, maxFont)
    # presto, inbetweenFont is now horizontally
    # vertically interpolated in different ways.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Interpolating two glyphs in the same font
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For any number of reasons you might want to interpolate a glyph within the same font. Here's how to do it::

    >>> File cannot be tokenized by tokenize

^^^^^^^^^^^^
Alternatives
^^^^^^^^^^^^

These are the conventional ways of doing interpolation. Have a look at :doc:`RoboFab's GlyphMath <glyphmath>` for alternatives for blending and interpolating glyphs together.
