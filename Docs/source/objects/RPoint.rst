RPoint
======

.. image:: ../../images/RPoint.gif

Usage
-----

.. showcode:: ../../examples/objects/RPoint_00.py

.. code::

    <RPoint for AFont.A[0][0]>

Description
-----------

``RPoint`` is perhaps the smallest object in RoboFab objects. It represents one single point with a particular coordinate in a contour. It is used to access off-curve and on-curve points alike. It's cousin, :doc:`bPoint` also provides access to incoming and outgoing bcps. ``RPoint`` is exclusively only one single point.

Understanding Contours and outlines
-----------------------------------

The way outline data is organised in RoboFab, and how the various objects relate is described here: :doc:`understanding contours <../howtos/understanding_contours>`.

Attributes
----------

.. py:attribute:: x

The ``x`` coordinate of this point.

.. py:attribute:: y

The ``y`` coordinate of this point.

.. py:attribute:: type

The ``type`` of this point.

.. py:attribute:: selected

Boolean for selection state, i.e. ``True`` or ``False``.

UFO only attributes
-------------------

.. py:attribute:: name

The name of the point (UFO only).

Methods
-------

.. py:function:: copy()

Return a deepcopy of the object.

.. py:function:: move((x, y))

Move the anchor of the ``bPoint`` to ``(x,y)``. The relative coordinates of the ``bcpIn`` and ``bcpOut`` will remain the same, which means that in fact, they move the same distance.

.. py:function:: round()

Round the coordinates to whole integers.

.. py:function:: select(state=True)

Select this point.

.. py:function:: transform(matrix)

Transform this point. Use a Transform matrix object to mess with the point.

.. seealso:: :doc:`how to use transformations <../howtos/use_transformations>`.
