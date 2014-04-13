========
RSegment
========

-----
Usage
-----

.. code::

    >>> # robofab manual
    >>> # Segment object
    >>> # usage examples
    >>> f = OpenFont()
    >>> for c  in f:
    >>>     for contour in c:
    >>>         for segment in contour:
    >>>             print segment
    < RSegment for RoboFab Demo Font.R[0][0] >
    < RSegment for RoboFab Demo Font.R[0][1] >
    < RSegment for RoboFab Demo Font.R[0][2] >
    < RSegment for RoboFab Demo Font.R[0][3] >
    < RSegment for RoboFab Demo Font.R[0][4] >

-----------
Description
-----------

A Contour object is a list of segments. A segment is a list of points with some special attributes and methods.

-----------------------------------
Understanding Contours and outlines
-----------------------------------

The way outline data is organised in RoboFab, and how the various objects relate is described here: :doc:`understanding contours <../docs_howtos/understanding_contours>`.

----------
Attributes
----------

.. py:attribute:: type

Type of segment.

.. py:attribute:: smooth

``True`` if the segment is ``smooth``, ``False`` if not.

.. py:attribute:: selected

Returns ``True`` if the segment is selected, ``False`` if not.

.. py:attribute:: points

List of points in the segment.

.. py:attribute:: onCurve

Returns the oncurve point associated with the segment.

.. py:attribute:: offCurve

Returns a list of offcurve points associated with the segment.

------------------
Attribute examples
------------------

.. code::

    # robofab manual
    # Segment object
    # attribute examples
    f = OpenFont()
    for c  in f:
        for contour in c:
            for segment in contour:
                print len(segment)
                print segment.type
                print segment.smooth
                print segment.points
                print segment.onCurve
                print segment.offCurve
                print segment.selected

-------
Methods
-------

.. py:function:: copy

Return a deepcopy of the object.

.. py:function:: move((x, y))

Move the anchor of the ``bPoint`` to ``(x,y)``. The relative coordinates of the ``bcpIn`` and ``bcpOut`` will remain the same, which means that in fact, they move the same distance.

.. py:function:: round

Round the coordinates to whole integers.

.. py:function:: transform(matrix)

Transform this point. Use a Transform matrix object to mess with the point.

.. seealso:: :doc:`how to use transformations <../docs_howtos/use_transformations>`.

---------------
Method examples
---------------

>>> # robofab manual
>>> # Segment object
>>> # method examples
>>> f = OpenFont()
>>> for c  in f:
>>>     for contour in c:
>>>         for segment in contour:
>>>             segment.move((50, 25))

