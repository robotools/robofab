Pen objects
===========

Pens are very useful and powerful objects. The idea is this: a glyph contains drawing information like contours, components etc. There is a lot of code that wants to work with this drawing information. But rather than to give access to these contours directly, the glyph and pen work together. Each glyph has a ``draw()`` method which takes a pen as a parameter. The pen object has a couple of standard methods (along the lines of ``lineto``, ``moveto``, ``curveto`` etc.) which are called by the glyph in the right order and with the right coordinates.

Abstraction
-----------

Using the pen as an intermediate, the code that just wants to draw a glyph doesn't have to know the internal functions of the glyph, and in turn, the glyph doesn't have to learn anything about specific drawing environments. Different kinds of glyph object (for instance the ``objectsFL.RGlyph`` and the ``objectsRF.RGlyph``) work very different on the inside. One stores data in FontLab, the other stores the coordinates itself and writes to GLIF. But both ``RGlyph`` objects have a draw method which follows the same abstract drawing procedures. So the code that uses the ``RGlyph.draw(pen)`` is not aware of the difference between the two kinds of glyphs.

Why pens?
^^^^^^^^^

In order to make a glyph draw in for instance a new graphics environment, you only need to write a new pen and implement the standard methods for the specifics of the environment. When that's done, all RoboFab glyphs can draw in the new world. But pens have also proven to be very useful as a means to get access to the outline data stored in a glyph without messing with the internal workings of a glyph. So even if you don't want to actually draw something on screen, the pen and ``draw()`` interface can help in for instance conversion, transformations, etc. One glyph can draw itself into another glyph as a way of copying itself while avoiding nasty dependencies, and circular references.

Flavors of Pen
--------------

RoboFab has two different kinds of pen which do different things for different purposes and they're intended for different methods in Glyph. Have a look in robofab/pens/ to see different kinds of pen objects for different purposes. RoboFab already has a fair number of pens in stock, chances are you'll find something you need. Examples of Penmanship at the :doc:`How to use Pens <../howtos/use_pens>`.

Pen()
^^^^^

The normal Pen object and pen that descend from it can be passed to ``aGlyph.draw(aPen)``. The Glyph calls these methods of the pen object to draw. It's very similar to "Drawing like PostScript".

.. py:function:: moveTo(pt, smooth=False)

Move the pen to the ``(x, y)`` in ``pt``.

.. py:function:: lineTo(pt, smooth=False)

Draw a straight line to the ``(x, y)`` coordinate in ``pt``.

.. py:function:: curveTo(pt1, pt2, pt3, smooth=False)

Draw a classic Cubic Bezier ("PostScript") curve through ``pt1`` (offcurve), ``pt2`` (also offcurve) and ``pt3`` which is oncurve again.

.. py:function:: qCurveTo(*pts, **kwargs)

Draw a Quadratic ("TrueType") curve through, well, any number of offcurve points. This is not the place to discuss Quadratic esoterics, but at least: this pen can deal with them and draw them.

.. py:function:: closePath

Tell the pen the path is finished.

.. py:function:: addComponent(baseName, offset=(0, 0), scale=(1, 1))

Tell the pen to add a component of ``baseName``, at ``offset`` and with ``scale``.

.. py:function:: addAnchor(name, (x, y))

Tell the pen to add an Anchor point with a name and a position.

.. py:function:: setWidth(width)

Tell the pen to set the width of the glyph. (deprecated)

.. py:function:: setNote(note)

Tell the pen to add a note to the glyph. (deprecated)

.. py:function:: doneDrawing

Tell the pen the drawing is done.

PointsPen()
^^^^^^^^^^^

Where the normal pen is an easy tool to think about drawing, the ``PointsPen`` is geared towards accessing all the data in the contours of the glyph. A ``PointsPen`` has a very simple interface, it just steps through all the points in a Glyph. Too complicated if you just want your script to draw in a glyph somewhere, but very useful for conversions of one thing to another, and when you're dealing with more elaborate point structures like several consecutive offcurve points. Again, have a look in the robofab/pens to see the available pens. Also the `LettError wiki <#>`_ has an in-depth description of the pen protocols. The ``PointsPen`` is passed to the ``aGlyph.drawPoints(aPointsPen)``

.. py:function:: beginPath

Start a new sub path.

.. py:function:: endPath

End the current sub path.

.. py:function:: addPoint(pt, segmentType=None, smooth=False, name=None, **kwargs)

Add a point to the current sub path.

.. py:function:: addComponent(self, baseGlyphName, transformation)

Add a sub glyph.

Need a pen?
-----------

If you need a pen to do some drawing in a ``Glyph`` object, you can ask the glyph to get you one. Depending on the environment you're in RoboFab will get you the right kind of pen object to do the drawing:

.. showcode:: ../../examples/objects/pen_00.py
 
See also a more in depth look at pens :doc:`here <../howtos/use_pens>`.
