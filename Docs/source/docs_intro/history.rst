===============
Release History
===============

A brief overview of what happened.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
November 30, 2009 - version 1.2 svn rev. 200
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In Python 2.6 ``as`` became a keyword. Some functions and methods in RoboFab used ``as`` as a parameter. This has been fixed.

^^^^^^^^^^^^^^^^^^^^^^^^^^^
March 1, 2009 - version 1.2
^^^^^^^^^^^^^^^^^^^^^^^^^^^

This version implements and supports the UFO2 specification. Lots of work in the ``font.info`` area, new attributes. Also some renaming and moving of attributes. The ``objectsFL`` and ``objectsRF`` code takes care and does a lot of re-routing, but also prints warnings when you're using deprecated names.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
January 8, 2006 - version 1.1.2
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

RoboFab is now available from a public svn server at ``code.robofab.com``. A couple of fixes and changes were waiting to be checked in. Please look at the svn change log for a detailed list of changes.

- In FontLab, ``AllFonts()`` will return a list of ``robofab.world.RFont`` objects for all open font windows. In NoneLab, ``AllFonts`` will raise a ``NonImplementedError``. ``AllFonts()`` can be imported from ``robofab.world``. The class magic which would also attempt to count font instances without a FontLab window has been removed.

- When exporting to UFO in FontLab, the features are stored in the ``font.lib``. The order of the features is now also recorded. When a UFO is imported into FontLab, the features will be inserted in this order. If the order information is not present (as in all UFOs at the moment), the features are imported in alphanetical order like before.

- Some updates to URLs in the documentation.

- Note: these updates are in the svn version only at the moment. Building the releases and installers is not automatic.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
February 7, 2006 - version 1.1.1
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Some changes in the **online** documentation. Note these changes are not part of the bundled documentation in the 1.1.1 release.

- The default value for clear in ``font.newGlyph(glyphName, clear=True)``. This value is set to ``False`` in the ``objectsFL`` (FontLab) implementaion, but it is set to True in the NoneLab implementation. The documentation reflected the ``objectsRF`` version which led to confusion. The documentation has been updated. The default value for clear in the ``objectsFL`` implementation has been changed to ``True``.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
September 12, 2005 - version 1.1.1
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- The ``save`` argument in ``font.close`` is now ``False`` by default. Any scripts that rely on ``font.close()`` to save fonts should be modified.
- ``font.close(save=False)`` now suppresses the save dialog.
- ``GuessSmoothPointPen`` is now robust against closed contours containing just one point.
- Fixed a bug that was causing ``objectsRF`` to mark glyphs as dirty after simply being loaded.
- The ``GlyphSet`` in ``glifLib`` has a new ``getUnicodes`` method for quickly extracting unicodes from all GLIF files.
- The ``UFOReader`` in ``ufoLib`` has a new ``getCharacterMapping`` method for quickly extracting unicodes from all GLIF files.
- Fixed a ``RContour.clockwise`` bug that was causing incorrect results to be returned if the contour had overlapping points.
- Fixed a ``RFont.insertGlyph(..., as=name)`` bug that was causing the ``as`` name to not be applied in some cases.
- The result of ``glyph.copy()`` no longer has a parent.
- Setting ``italicAngle`` and ``slantAngle`` now forces the values to be floats.
- ``glyphNameSchemes`` now forces the conversion to big endian so the results will be the same on Windows and Mac.
- Components with negative scale values now return correct bounding boxes.
- ``dialogs.py`` no longer has a win32com dependency when used in FontLab Windows.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
February 7, 2005 - version 1.1
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Fixed a minor rounding error in ``flPen.py`` that was allowing unrounded data to be passed to FontLab.
- ``objectsRF.RComponent`` decomposes properly now.
- Added new ``filterPen.py`` to pens: a module with some useful and sample pens illustrating non-drawing applications of pen objects. ``StatsPen``: a pen returning the length of the contour, ``FlattenPen``: a cubic path flattener. And a couple of helpers to make filtering easier.
- ``robofab.features`` but that may be moving to a private location...
- ``RInfo`` now has ``createdBy``, ``weightValue``, ``weightName`` and ``widthName`` attributes. These are also now written into ``info.plist`` in UFOs.
- ``RGlyph`` has a fun new rasterize method.
- ``RContour`` now has rotate and skew methods.
- New ``robofab.path.intersect`` module for calculating intersections.
- New ``FindGlyph`` dialog added to ``dialogs.py``. This dialog is similar to ``SelectGlyph``, but it contains a search field. Very handy when working with large fonts.
- Setting ``objectsFL.unitsPerEm`` is now buffered against possible float values
- Added UNIX ASCII (PFA) as a generating option in ``RFont`` (use ``unixascii`` as the type in the generate method). It has been here all along, but it was incorrectly labeled as PC Type 1 ASCII.
- Retrieving groups from a VFB is now more stable.
- ``RFont.insertGlyph`` has a new ``as=something`` argument in order to easily insert one glyph under a different name.
- ``RGlyph`` interpolation and glyph math have been completely rewritten. Now the methods are much more flexible about point types and off curve point counts. The methods are still very strict regarding the count of on curve points. In addition to being much more flexible, it is also much faster.
- ``RGlyph.isCompatible`` returns results that follow the same logic as ``RGlyph.interpolate``
- ``RContour.interpolate`` and the math methods in ``RContour``, ``RSegment``, ``RPoint``, ``RAnchor`` and ``RComponent`` have all been deprecated.
- ``RGlyph.note`` is now properly encoded.
- A provision for alternate .glif namingschemes has been added. During the writing of UFO the user can now specify a function (for instance ``robofab.tools.glyphNameSchemes.glyphNameToShortFileName``) to create ``.glif`` filenames for glyphs. Previously all glyphnames mapped to filenames directly, which made it impossible to export glyphs with long names in some pythons. The default glif naming scheme in ``ObjectsFL`` has been set to the aforementioned ``glyphNameToShortFileName``, check the module for a detailed description of the algorithm. Note that this only affects new exports. Existing UFO's and ``.glifs`` are not changed. See `How to use glyph naming schemes`_.
- Fixed a bug that could pontially cause a GLIF to be saved outside of the proper UFO.
- New scripts located in ``robofab/Scripts/RoboFabUFO``: ``DumpOneGlyphToGlif.py``, ``DumpOneGlyphToUFO.py``, ``ExportFontToUFO.py``, ``ImportFontFromUFO.py``, ``ImportOneGlyphFromUFO.py``
- Bug in script ``GenerateKernProof.py`` fixed.
- ``RFont`` now has a handy ``getReverseComponentMapping`` method for getting a reversed component mapping.
- ``AllFonts`` bugs squashed.
- ``plistlib`` modified to by Python 2.2 compatible
- Glyph order is now stored and read from ``font.lib["org.robofab.glyphOrder"]``. Importing a UFO into FontLab now follows this order.
- Raw FDK-style OT feature code is now stored in ``font.lib["org.robofab.opentype.classes"]`` and ``font.lib["org.robofab.opentype.features"]`` in UFOs. This data is stored in the OpenType fields in FontLab files.
- ``robofab.world`` no longer prints nag during import.
- Fixed bug in ``objectsRF.RFont.save`` that was occasionally (very, very rarely) forcing save operations to be considered save as operations.
- Added deprecation warnings to ``family.py`` and ``featureLib.py``.
- Added warning to ``nameTable.py``.
- Removed ``properties.py``.
- Removed unused ``Point`` and ``Offset`` classes from ``objectsBase``.
- Fixed a bug that would raise an error in ``robofab.interface.all.dialogs.AskString``.
- Backported RoboFab to Python 2.2.1. This is now the oldest version of Python we support. Python 2.2 is not supported.
- RoboFab now includes a Python 2.2 compatible version of ``sets.py`` (found here). In Python 2.3+ the sets from the standard lib will be used in place of this version.
- Reworked the way ``RPoint`` determines its type attribute in ``objectsFL``.
- Patched a small bug in ``BaseContour.draw`` that occured when a contour begins with a ``qcurve`` in FontLab.
- Removed support for drawing with antique RoboFab pens. Only FontTools pens are supported now.
- Removed support for drawing with antique RoboFab pens. Only FontTools pens are supported now.
- Components now have a read-only ``box`` attribute.

.. _How to use glyph naming schemes : #

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
March 26, 2004 - version 1.01
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Renamed the folder with utility scripts for FontLab to ``RoboFab Utils`` as not to overwrite any other folders named ``Utils`` which might live in the FontLab macros folder.
- Fixed a problem with ``glyph.box`` which would show up in some cases in plain Python use of RoboFab with glyphs which have anchors outside of the horizontal bounds of the glyph.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
March 14, 2004 - version 1.0
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

First public release.

^^^^^^^^^^^^
January 2004
^^^^^^^^^^^^

We've done some projects using RoboFab at the center and it's fast to work with and reliable. We considered ways to reschedule the conference and couldn't plan anything for a couple of unrelated but unchangeable reasons. We decide for a release.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
September 2003: RoboThon '03
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Worked very hard to get RoboFab 1.0b1 ready for the RoboThon conference in September. The RoboThon was cancelled at the last minute to make room for hurricane Isabel. We soon released the beta to a small group but the missed conference made it difficult for folks to get started.

^^^^^^^^^^^^^^^^^^^^^^^^^
July 2003: New Fileformat
^^^^^^^^^^^^^^^^^^^^^^^^^

Summer 2003 we started defining the UFO file format, using GLIF for glyph information and Apple's ``.plist`` (also XML based and entirely cross platform) for any other data as listings, indices, etc.

^^^^^^^^^^^^^^^^^^^^^^^
April 2003: New Objects
^^^^^^^^^^^^^^^^^^^^^^^

April 2003 we started new objects to live on top of the FontLab objects. Just van Rossum started work on the GLIF file format.

^^^^^^^^^^^^^^^^^^^^
February 2003: Start
^^^^^^^^^^^^^^^^^^^^

RoboFab was started sometime during the TypoTechnica in Heidelberg, 2003. Tal Leming, Erik van Blokland and Just van Rossum combined their FontLab code into a new library. At first it was an odd collection of fixes and workarounds.
