========
RContour
========

-----
Usage
-----

>>> # robofab manual
>>> # Contour object
>>> # usage examples
>>> # take a glyph (one with outlines obviously)
>>> c = CurrentGlyph()
>>> # get to contours by index:
>>> print c[0]
< RContour for Mailer-Regular.a[0] >

-----------
Description
-----------

:py:class:`RContour` is an object for, well, contours. A contour is a single path of any number of points and shape. A glyph usually consists of a couple of contours, and this the object that represents each one. The :py:class:`RContour` object offers access to the outline matter in various ways. The parent of :py:class:`RContour` is usually :py:class:`RGlyph`.

-----------------------------------
Understanding Contours and outlines
-----------------------------------

The way outline data is organised in RoboFab, and how the various objects relate is described here: `understanding contours`_.

If you want to add new contours to a glyph it's easier to draw them with a pen than to construct the shapes from segments.

----------
Attributes
----------

.. py:attribute:: index

The index of the contour in the Glyph.

.. py:attribute:: selected

Returns ``1`` if the contour is selected, ``0`` if it isn't.

.. py:attribute:: box

The bounding box for the contour (read only).

.. py:attribute:: clockwise

Direction of contour: ``1=clockwise``, ``0=counterclockwise``.

.. py:attribute:: points

The contour as a list of :py:class:`Point`s.

.. py:attribute:: bPoints

The contour as a list of :py:class:`bPoint`s.

------------------
Attribute examples
------------------

:: 

    # Examples with contours and points here.

--------------------
Methods for segments
--------------------

For regular drawing in glyphs: please use Pens. If you want to mess with segments on a lower level, be our guest:

.. py:function:: appendSegment(segmentType, points, smooth=False)

Add a segment to the contour. Parameters?

.. py:function:: insertSegment(index, segmentType, points, smooth=False):

Insert a segment into the contour.

.. py:function:: removeSegment(index):

Remove a segment from the contour.

.. py:function:: setStartSegment(segmentIndex):

Set the first node on the contour.

------------------
Methods for points
------------------

.. py:function:: appendBPoint(pointType, anchor, bcpIn=(0, 0), bcpOut=(0, 0))

Append a :py:class:`bPoint` to the contour.

.. py:function:: autoStartSegment

Automatically set the lower left point of the contour as the first point.

.. py:function:: insertBPoint(index, pointType, anchor, bcpIn=(0, 0), bcpOut=(0, 0))

Insert a :py:class:`bPoint` at index on the contour.

-------------
Other methods
-------------

.. py:function:: reverseContour()

Reverse contour direction.

.. py:function:: copy

Duplicate this contour.

.. py:function:: draw(aPen)

Draw the object with a RoboFab segment pen.

.. py:function:: drawPoints(aPen)

Draw the object with a point pen.

.. py:function:: move((x, y))

Move the contour.

.. py:function:: pointInside((x, y), evenOdd=0)

Determine if the point is inside or ouside of the contour.

.. py:function:: round()

Round the value of all points in the contour.

.. py:function:: scale((x, y), center=(0, 0))

Scale the contour by ``x`` and ``y``. Optionally set the center of the scale.

.. py:function:: rotate(angle, offset=None)

Rotate the contour by ``angle`` (in degrees). Optionally set an ``offset`` value.

.. py:function:: skew(angle, offset=None)

Skew the contour by ``angle`` (in degrees). Optionally set an ``offset`` value.

.. py:function:: transform(matrix)

Transform this contour. Use a Transform matrix object to mess with the contour. See also `how to use transformations`_.

---------------
Method examples
---------------

::

    # robofab manual
    # Contour object
    # method examples
