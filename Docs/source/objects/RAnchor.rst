RAnchor
=======

.. image:: ../../images/RAnchor.gif

Usage
-----

.. showcode:: ../../examples/objects/RAnchor_00.py

.. code::

    < RGlyph for RoboFab Demo Font.A >
    [< RAnchor for RoboFab Demo Font.A.anchors[0] >]

Description
-----------

Anchors are single points in a glyph which are not part of a contour. Anchors have a name and a position, and they're used as connection points for :doc:`Components <RComponent>`. In FontLab the anchors have a special appearance and can be edited. Anchors are stored in GLIF as single, named, ``moveto``'s. i.e. any single, named ``moveto`` in GLIF will become an anchor in FontLab. RoboFab's own ``font.generateGlyph()`` also uses the anchors to assemble the components.

Attributes
----------

.. py:attribute:: index

The index of the anchor. (read only)

.. py:attribute:: position

The position of the anchor ``(x, y)``.

.. py:attribute:: x

The ``x`` position of the anchor.

.. py:attribute:: y

The ``y`` position of the anchor.

.. py:attribute:: name

The name of the anchor.

Attribute examples
------------------

.. showcode:: ../../examples/objects/RAnchor_01.py

Methods
-------

.. py:function:: copy()

Return a deepcopy of the object.

.. py:function:: move((x, y))

Move the anchor of the ``bPoint`` to ``(x,y)``. The relative coordinates of the ``bcpIn`` and ``bcpOut`` will remain the same, which means that in fact, they move the same distance.

.. py:function:: scale((x, y), center=(0, 0))

Scale the anchor.

.. py:function:: round()

Round the coordinates to whole integers.

.. py:function:: draw(aPen)

Draw the object with a RoboFab segment pen.

.. py:function:: drawPoints(aPen)

Draw the object with a point pen. See :doc:`how to use pens <../howtos/use_pens>`.

.. py:function:: transform(matrix)

Transform this point. Use a Transform matrix object to mess with the point. See :doc:`how to use transformations <../howtos/use_transformations>`.

Method examples
---------------

.. code::

    # robofab manual
    # Font object
    # method examples
