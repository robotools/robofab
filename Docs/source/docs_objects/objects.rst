================
Objects Overview
================

The most detailed information about RoboFab objects is available in **robofabDocs** in the RoboFab distribution. This overview here focusses on a couple of the more important objects and offers examples on how to use them.

-----
Model
-----

Here is a :doc:`handy map <model>` of the RoboFab objects.

*[img]*

----------------------------
RoboFab Unified Font Objects
----------------------------

- :doc:`Map <model>`: The objects and their relations.
- :doc:`Pen objects <pens>`: About Pen objects.
- :doc:`PostScript Glyph Hints <psHintsGlyph>`: Glyph attribute, contains glyph level PostScript hint data.
- :doc:`RAnchor <RAnchor>`: A connection point for Components.
- :doc:`RComponent <RComponent>`: Belongs to a Glyph, refers to other Glyphs.
- :doc:`RContour <RContour>`: Belongs to a Glyph, contains Segments.
- :doc:`RFont <RFont>`: Contains Glyphs, names, kerning, data.
- :doc:`RGlyph <RGlyph>`: Belongs to a Font, contains contours, components etc.
- :doc:`RInfo <RInfo>`: Part of a Font, contains all names, dimensions.
- :doc:`RKerning <RKerning>`: Part of a Font, contains all kerning data.
- :doc:`RLib <libs>`: Part of a Font, contains all arbitrary data.
- :doc:`RPoint <RPoint>`: A point on a Contour.
- :doc:`RSegment <RSegment>`: A part of a Contour, a series of severall off and one oncurve Points.
- :doc:`bPoint <bPoint>`: A point on a Contour with attributes for ``bcpIn``, ``bcpOut`` and ``anchor``.
- :doc:`psHints <psHints>`: Part of a Font, contains font level PostScript hinting data.

-----
Scope
-----

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Naming conventions in RoboFab
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Attributes and method names follow a couple of consistent rules which make it easier to remember what they're called.

- Class names start with a capital: ``RGlyph``, ``BasePen`` etc.

- Method and attribute names start with lowercase: ``glyph.center()``, ``glyph.width``.

- Private attributes and methods start with underscore: ``point._index``.

.. note:: Private methods and attributes are needed to make the objects work, but they're not intended for users to mess with, that's why they're called private. The description of the objects in this manual then do not list them.

- All names follow ``camelCaseNaming`` as much as possible. So 'glyph name' becomes ``glyphName``

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Availability of methods, attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Unless noted otherwise, the examples, methods and attributes should work in all implementations of RoboFab, so within FontLab as well as NoneLab. These reference pages are written by an experienced RoboFab user, not a robot. All the objects have more attributes and methods than listed here. But these are the most important ones to get started with. For a full list refer to the **robofabDocs** in the RoboFab distribution.

^^^^^^^^^^^^^^^^^^^^^^^^^^
Perhaps not documented yet
^^^^^^^^^^^^^^^^^^^^^^^^^^

As noted earlier, this documentation is written by a person, not a machine. So it is possible attributes, objects, methods are missing. Drop us a line if you're missing something.
