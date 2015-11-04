==========
RComponent
==========

-----
Usage
-----

.. showcode:: ../../Examples/objects/RComponent_00.py

.. code::

	< RComponent for Excellent-Regular.adieresis.components[0] >
	< RComponent for Excellent-Regular.adieresis.components[1] >

-----------
Description
-----------

A component can be a part of a glyph and it is a reference to another glyph in the same font. With components you can make glyphs depend on other glyphs. Changes to the ``baseGlyph`` will reflect in the component as well. Fontographer and RoboFog called them **composites**. The **parent** of a component is usually a glyph. Components can be decomposed: they replace themselves with the actual outlines from the ``baseGlyph``. When that happens the link between the original and the component is broken: changes to the ``baseGlyph`` will no longer reflect in the glyph that had the component.

----------
Attributes
----------

.. py:attribute:: baseGlyph

The name of the glyph the component points to. The glyph is assumed to be present in the same font.

.. note:: In FontLab this attribute is read-only.

.. py:attribute:: index

The index of the component in the list of components in the parent glyph. i.e. the first component in a glyph has index ``0``.

.. py:attribute:: offset

The offset vector ``(x, y)``. The distance the component has been moved.

.. py:attribute:: scale

The scale ``(x, y)``. The distance the component has been moved.

.. py:attribute:: box

The bounding box for the component. (read only)

------------------
Attribute examples
------------------

.. showcode:: ../../Examples/objects/RComponent_01.py

.. code::

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

Draw this component with ``aPointPen``.

.. note:: Both these drawing methods are usually called by ``aGlyph.draw()`` and ``aGlyph.drawPoints()`` as part of the drawing process.

.. py:function:: copy

Return a deep copy of the object.

.. py:function:: setChanged

Call to indicate that something about the component has changed.

---------------
Method examples
---------------

.. code::

    # robofab manual
    # Component object
    # method examples
