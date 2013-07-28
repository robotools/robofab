==========
RComponent
==========

-----
Usage
-----

>>> # the easiest way to get to a component
>>> # is to get one from a glyph
>>> from robofab.world import CurrentFont
>>> f = CurrentFont()
>>> g = f['adieresis']
>>> for c in g.components:
>>>     print c
< RComponent for Excellent-Regular.adieresis.components[0] >
< RComponent for Excellent-Regular.adieresis.components[1] >

-----------
Description
-----------

A component can be a part of a glyph and it is a reference to another glyph in the same font. With components you can make glyphs depend on other glyphs. Changes to the ``baseGlyph`` will reflect in the component as well. Fontographer and RoboFog called them composites. The parent of a component is usually a glyph. Components can be decomposed: they replace themselves with the actual outlines from the ``baseGlyph``. When that happens the link between the original and the component is broken: changes to the ``baseGlyph`` will no longer reflect in the glyph that had the component.

----------
Attributes
----------

.. py:attribute:: baseGlyph

The name of the glyph the component points to. The glyph is assumed to be present in the same font. Note: in FontLab this attribute is readonly.

.. py:attribute:: index

The index of the component in the list of components in the parent glyph. i.e. the first component in a glyph has index ``0``.

.. py:attribute:: offset

The offset vector ``(x, y)``. The distance the component has been moved.

.. py:attribute:: scale

The scale ``(x, y)``. The distance the component has been moved.

.. py:attribute:: box

The bounding box for the component (read only).

------------------
Attribute examples
------------------

>>> # robofab manual
>>> # Component object
>>> # attribute examples
>>> print f['adieresis'].components[0].baseGlyph
>>> print f['adieresis'].components[1].baseGlyph
>>> # move the component in the base glyph
>>> f['adieresis'].components[1].offset = (100,100)
>>> # scale the component in the base glyph
>>> f['adieresis'].components[0].scale = (.5, .25)
a
dieresis

-------
Methods
-------

.. py:function:: decompose

In the parent glyph replace this component object with the actual contours. This practically ends the existence of the component object.

.. py:function:: move((x, y))

Move the component to position ``(x, y)``.

.. py:function:: draw(aPen)

Draw this component with ``aPen``.

.. py:function:: drawPoints(aPointPen)

Draw this component with ``aPointPen``. Note: both these drawing methods are usually called by ``aGlyph.draw()`` and ``aGlyph.drawPoints()`` as part of the drawing process.

.. py:function:: copy

Return a deep copy of the object.

.. py:function:: setChanged

Call to indicate that something about the component has changed.

---------------
Method examples
---------------

::

    # robofab manual
    # Component object
    # method examples
