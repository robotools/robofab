==========
Glyph Math
==========

``RGlyph`` objects have methods that allow the objects to behave a bit like variables in simple math. These methods do not do additions or substractions of the surface area of the glyphs, like layering two glyphs on top of each other and than doing "remove overlap". Instead, they return new glyph objects in which each coordinate in each contour is the product of the two glyphs.

-------
Objects
-------

All glyph math operations in have new, orphaned, objects as result. For instance a substraction of two FontLab RoboFab glyphs will result in a new glyph object, but it won't be part of the font. If you want the result to be part of the font you have to add it explicitly, see the example at the bottom of this page. There are several reasons for this:

- The result might not even come from glyphs in the same font, i.e. you can substract a glyph in one font from a glyph in another font. Where should the result live? You decide.

- You might not want the result to be part of your font when you're using it for further calculations. So: results from glyphmath operations are orphan glyphs that do not belong to any font.

- The results need to use floating point (``19.234943``) numbers for precision, FontLab only stores integer numbers (``19``).

If you want to add a glyph (of any flavor, FontLab or UFO) to a font use the appendGlyph method::

    someNewGlyph = aFont.newGlyph("someNewGlyph")
    someNewGlyph.appendGlyph(restultFromGlyphMath)
     
    # note you have to set the width, appendGlyph does not automatically
    # take the value.
    someNewGlyph.width = restultFromGlyphMath.width

-----------
Subtraction
-----------

Substraction returns a new glyph object with contours which represent the **difference** between the two previous glyphs. As a glyph itself, it's not much to look at. If you draw the result of a substraction it will probably look like a crumpled outline.

^^^^^^^^^^^^^^^^^^^
Example Subtraction
^^^^^^^^^^^^^^^^^^^

.. code::

    f = CurrentFont()
    g = f["a"]
    h = f["b"]
    # suppose g and h have compatible point structures
    myRelativeGlyph = g - h

--------
Addition
--------

Addition returns a new glyph object with the contours which is the product of the two previous glyphs. If you just add two "normal" glyphs from a font (or multiple fonts for that matter) it will look odd. But you can also easily add a relative glyph (a result of substracting one glyph from another), which effectively means you're applying the difference between two glyphs to a third. And that can be a very useful action.

^^^^^^^^^^^^^^^^
Example Addition
^^^^^^^^^^^^^^^^

.. code::

    # continue with myRelativeGlyph from the previous example
    newglyph = f["x"] + myRelativeGlyph

--------------
Multiplication
--------------

When a normal glyph is multiplied it looks as if the glyph has been scaled. For instance multiplying a glyph with ``0.5`` scales the shapes 50%.

^^^^^^^^^^^^^^^^^^^^^^
Example Multiplication
^^^^^^^^^^^^^^^^^^^^^^

.. code:: 

    # continue with myRelativeGlyph from the previous example
    newglyph = f["x"] + 0.25 * myRelativeGlyph

--------
Division
--------

Divisions works just like multiplications, you just need to make sure not to divide by zero.

^^^^^^^^^^^^^^^^
Example Division
^^^^^^^^^^^^^^^^

.. code::

    # continue with myRelativeGlyph from the previous example
    newglyph = f["x"] + myRelativeGlyph / 4

------------
Combinations
------------

These examples are simple enough, but when you combine them the operations can become really powerful. You could recreate font interpolation using GlyphMath, or construct new networks of interpolations, additions, shifts, deltas that were impossible to build.

^^^^^^^^^^^^^^^^
All together now
^^^^^^^^^^^^^^^^

This is from the ``demo_GlyphMath.py`` which should be in the ``Scripts/RoboFabIntro`` folder::

    # robofab manual
    # Glyphmath howto
    # Fun examples

    #FLM: Fun with GlyphMath
     
    # this example is meant to run with the RoboFab Demo Font
    # as the Current Font. So, if you're doing this in FontLab
    # import the Demo Font UFO first.
     
    from robofab.world import CurrentFont
    from random import random
     
    f = CurrentFont()
    condensedLight = f["a#condensed_light"]
    wideLight = f["a#wide_light"]
    wideBold = f["a#wide_bold"]
     
    diff = wideLight - condensedLight
     
    destination = f.newGlyph("a#deltaexperiment")
    destination.clear()
    x = wideBold + (condensedLight-wideLight)*random()
     
    destination.appendGlyph( x)
    destination.width = x.width
     
    f.update()

---------------------
Implementation limits
---------------------

In ``objectsFL`` (for use in FontLab), only ``RGlyph`` has glyphmath operators implemented. The result of a glyphmath operation in FontLab is **always** an object from ``objectsRF``. In ``ObjectsRF`` most objects have ``*``, ``+`` and ``-`` implemented. But considering the operators are mainly used for Glyph stuff, the ``RGlyph`` object is a bit more kitted out with division as well.
