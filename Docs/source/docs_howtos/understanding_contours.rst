===================================
Understanding Contours and Segments
===================================

Now, this is an important part of RoboFab so pay attention. In the world of digital font formats we have several different kinds of ways of describing outlines. Bezier curves for PostScript fonts, Quadratic curves for TrueType fonts. Each with their own peculiarities. RoboFab is format agnostic so it should be able to store all PostScript and all TrueType points. The structure here is meant to be able to do all that.

Diagrams by Tal Leming.

--------
Contours
--------

A glyph can contain one or more contours. Depending on what you want to do, there are different ways of looking at the data of the contour, the points, the line segments. The ``RContour`` object is way to the outlines.

.. figure:: ../../images/contours.jpg
   :width: 300 px
   :align: center

   a contour

.. showcode:: ../../Examples/howtos/understandingContours_00.py

.. code::

    < RContour for Mailer-Regular.a[0] >
    15
    # 15? 15 of what?

.. seealso::

    A description of the :doc:`RContour <../docs_objects/RContour>` object.

--------
Segments
--------

This circle consists of a couple of segments, each a piece of of the contour. A contour is a sequence of segments, you can iterate through a contour to get segments. A contour also has methods for adding and deleting segments.

.. figure:: ../../images/contours_segments.jpg
   :width: 300 px
   :align: center

   a contour's segments

.. code::

    # segment code example

In turn, a segment is made up of a sequence of points. Any number of off-curve points followed by an on-curve point. For the PostScript-centric designers: in TrueType outlines it is allowed to have any number of off-curve points before an on-curve. These points know whether they need to be rendered as bezier of quadratic curves.

.. figure:: ../../images/contours_segments_points.jpg
   :width: 300 px
   :align: center

   segments with on-curve and off-curve points

.. seealso::

    A description of the :doc:`RSegment <../docs_objects/RSegment>` object.

------
Points
------

Another way to look at a contour is as a sequence of on-curve and off-curve points. This is the approach taken by ``glyph.drawPoints()`` and ``PointPen``. 

.. figure:: ../../images/contours_points.jpg
   :width: 300 px
   :align: center

   points (on-curve and off-curve)

.. showcode:: ../../Examples/howtos/understandingContours_02.py

.. code::

    < RPoint for Special-Bold.A[0][0] >
    < RPoint for Special-Bold[1][1] >
    etc..

.. seealso:: A description of the :doc:`RPoint <../docs_objects/RPoint>` object.

-------
bPoints
-------

This is another way to look at contours and its parts: ``bPoints`` behave very much like RoboFog points used to do. A point object has an incoming ``bcp``, an on-curve ("anchor point" fog called it) and an outgoing ``bcp``. This approach has been added for folks more at ease with the RoboFog structure.

.. note::

    If the contour contains series of off-curve points, ``bPoints`` won't help you.

.. figure:: ../../images/contours_bpoints.jpg
   :width: 300 px
   :align: center

   bPoints with incoming and outcoming BCPs

.. showcode:: ../../Examples/howtos/understandingContours_03.py

.. code::

    ...

.. seealso:: A description of the :doc:`bPoint <../docs_objects/bPoint>` object.
