================
Objects Overview
================

The most detailed information about RoboFab objects is available in robofabDocs in the RoboFab distribution. This overview here focusses on a couple of the more important objects and offers examples on how to use them.

-----
Model
-----

Here is a handy map of the RoboFab objects.

----------------------------
RoboFab Unified Font Objects
----------------------------

- Map: of the objects and their relations.
- Pen objects: about Pen objects
- PostScript Glyph Hints: glyph attribute, contains glyph level PostScript hint data.
- RAnchor: a connection point for Components
- RComponent: belongs to a Glyph, refers to other Glyphs
- RContour: belongs to a Glyph, contains Segments
- RFont: contains Glyphs, names, kerning, data
- RGlyph: belongs to a Font, contains contours, components etc.
- RInfo: part of a Font, contains all names, dimensions
- RKerning: part of a Font, contains all kerning data
- RLib: part of a Font, contains all arbitrary data
- RPoint: a point on a Contour
- RSegment: a part of a Contour, a series of severall off and one oncurve Points
- bPoint: a point on a Contour with attributes for bcpIn, bcpOut and anchor.
- psHints: part of a Font, contains font level PostScript hinting data.

-----
Scope
-----

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Naming conventions in RoboFab
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Attributes and method names follow a couple of consistent rules which make it easier to remember what they're called.

- Class names start with a capital: ``RGlyph``, ``BasePen`` etc.
- method and attribute names start with lowercase: ``glyph.center()``, ``glyph.width``
- private attributes and methods start with underscore: ``point._index``. Note: private methods and attributes are needed to make the objects work, but they're not intended for users to mess with, that's why they're called private. The description of the objects in this manual then do not list them.
- all names follow ``camelCaseNaming`` as much as possible. So 'glyph name' becomes ``glyphName``

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Availability of methods, attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Unless noted otherwise, the examples, methods and attributes should work in all implementations of RoboFab, so within FontLab as well as NoneLab. These reference pages are written by an experienced RoboFab user, not a robot. All the objects have more attributes and methods than listed here. But these are the most important ones to get started with. For a full list refer to the robofabDocs in the RoboFab distribution.

^^^^^^^^^^^^^^^^^^^^^^^^^^
Perhaps not documented yet
^^^^^^^^^^^^^^^^^^^^^^^^^^

As noted earlier, this documentation is written by a person, not a machine. So it is possible attributes, objects, methods are missing. Drop us a line if you're missing something.
