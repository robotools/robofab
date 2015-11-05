Limitations
===========

An overview of known problems, bugs and implementation limits. These are issues we are aware of. Some of them are things we have to fix in RoboFab, others are limitations that are just part of the world we have to work in.

FontLab
-------

Known problems in FontLab 4.6.1

flfont.customdata, flglyph.customdata
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There is a bug in FontLab which caused FontLab to crash shortly after Python has written something in the ``flfont.customdata`` or ``flglyph.customdata`` fields. RoboFab uses the customdata fields to store the ``font.lib`` and ``glyph.lib``. RoboFab is just using the functionality of these fields in FontLab, there's nothing we can do to fix it in RoboFab. The problem has been reported to the FontLab developers.

.. note:: FontLab Studio 5 probably has a new attribute for font and glyph objects to store arbitrary Python data. This attribute will replace the customdata attribute. At the time of the 1.1.1 release we have not tested this attribute. We expect a future release to make use of them.

Multiple Master
^^^^^^^^^^^^^^^

RoboFab glyphs do not offer direct access to FontLab's Multiple Master-masters. If you need access to that data, use the ``glyph.naked()`` method to get to the FontLab glyph object which have access.

.. note:: If you're considering scripting complex interpolation systems, have a look at `Superpolation`_.

.. _Superpolation: http://superpolator.com/

UFO format
----------

Known problems or limitations in the UFO format, RoboFab version 1.0b1 and 1.0.

Export of OT features
^^^^^^^^^^^^^^^^^^^^^

RoboFab does not automatically export the feature descriptions from FontLab to UFO. The ``featureLib.py`` offers some tools to export the feature text to the ``font.lib`` and import them from the lib as well, but this needs to be called separately after reading and before writing the UFO. Or export all features to a separate ``.fea`` file.

Macroman encoded XML files from UFO Exporter in RoboFog
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Not a problem, but just something to be aware of: UFO files exported from the UFO Exporter scripts in **RoboFog** are text files with macroman text encoding. The XML files identify the encoding as such and XML interpreters seem to respect and understand this. UFO files exported written by the UFO writers in RoboFab use UTF-8 as default encoding for the XML text. The macroman export is necessary because encodings are not supported in Python 1.5.2.

Objects
-------

Known problems with Objects.

GlypMath on Contour, Segment, Point in FontLab
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``Contour``, ``Segment``, ``Point`` and ``BPoint`` objects in ``objectsFL`` (the objects you get when you use RoboFab in FontLab) do not have GlyphMath operators. All GlyphMath operations in FontLab are handled by the ``Glyph`` object and then quickly deferred to objects from ``objectsRF`` which do know how to handle GlyphMath operations. This is not necessarily a bug, but an effect of differences between the way RoboFab objects work in FontLab and how they work in plain Python.
