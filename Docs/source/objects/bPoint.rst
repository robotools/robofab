bPoint
======

.. image:: ../../images/bPoint.gif

Usage
-----

.. showcode:: ../../examples/objects/bPoint_00.py

.. code::

    < RbPoint for Special-Bold.A[0][0] >

Description
-----------

The ``bPoint`` is a point object which mimics the old "Bezier Point" from RoboFog. It has attributes for ``bcpIn``, ``anchor``, ``bcpOut`` and ``type``. The coordinates in ``bcpIn`` and ``bcpOut`` are relative to the position of the anchor. For instance, if the ``bcpIn`` is 20 units to the left of the anchor, its coordinates would be ``(-20,0)``, regardless of the coordinates of the anchor itself. Also: ``bcpIn`` will be ``(0,0)`` when it is "on top of the anchor", i.e. when there is no ``bcp`` it will still have a value. The parent of a ``bPoint`` is usually a Contour.

Understanding Contours and outlines
-----------------------------------

The way outline data is organised in RoboFab, and how the various objects relate is described here: :doc:`understanding contours <../howtos/understanding_contours>`

Attributes
----------

.. py:attribute:: anchor

The ``(x, y)`` position of (oncurve) anchor.

.. py:attribute:: bcpIn

The ``(x, y)`` position of the incoming (offcurve) bezier control point.

.. py:attribute:: bcpOut

The ``(x, y)`` position of the outgoing (offcurve) bezier control point.

.. py:attribute:: type

The type of the ``bPoint``. Either ``corner`` or ``curve``.

Attribute examples
------------------

.. showcode:: ../../examples/objects/bPoint_01.py

.. code::

    (0, -175) (611, 337) (0, 175)
    (0, 0) (223, 641) (0, 0)
    etc..

Methods
-------

.. py:function:: copy

Return a deepcopy of the object.

.. py:function:: move((x, y))

Move the anchor of the ``bPoint`` to ``(x,y)``. The relative coordinates of the ``bcpIn`` and ``bcpOut`` will remain the same, which means that in fact, they move the same distance.

.. py:function:: round

Round the coordinates to whole integers.

.. py:function:: select(state=True)

Select this point.

.. py:function:: transform(matrix)

Transform this point. Use a Transform matrix object to mess with the point.

.. seealso:: :doc:`how to use transformations <../howtos/use_transformations>`.

Method examples
---------------

.. code::

    >>> # robofab manual
    >>> # bPoint object
    >>> # method examples
