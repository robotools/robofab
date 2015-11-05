UFO Overview
============

Another font format?
--------------------

No. The RoboFab developers felt the need for a flexible, text based (XML) format to store data related to typedesign. RoboFab Python objects work with UFO files, but the UFO specification is open: others can write implementations of the UFO format in other languages for other purposes. The UFO format is documented `here`_.

.. _here: http://unifiedfontobject.org/

.. _glif:

GLIF
----

Glyphs and glyph related data is stored in a GLIF file which lives with its friends in a folder. Just van Rossum developed the XML format and described the tags in great detail here. A GLIF file describes all parts of the glyph: contours, points, off curves, on curves, width, even the glyph lib is stored here. RoboFab reads and writes GLIF. You could email a glyph by including the text in the email body. GLIFs have been sent through text chats and even SMS text messaging. GLIFs could be printed out on paper, stored, typed in after a 1000 years and all the data would still be present.

GlyphSet
--------

A GlyphSet is an object which manages the GLIF files. It can make an index of all GLIF files in a folder and store it in a seperate .plist file in which glyph names are mapped to GLIF file names. When a GlyphSet is asked for a particular Glyph, it can refer to the index and retrieve the right file. GlyphSet is "lazy loading", it will only read and parse XML for Glyphs that are asked for. Font objects in NoneLab use GlyphSet to access and write the GLIFs.

Pen Protocol
------------

The Pen Protocol is a fast and versatile way to get data in and out of glyphs, without having to know their internal structure. RoboFab uses Pen objects a lot. More on the Pen Protocol here.
Unified Font Objects

By standardising the API of the RoboFab objects, scripts become more portable between different font applications. This means saving time and effort which can be spent more creatively. Fonts, glyphs and contours aren't going to change a lot. More likely, stuff will be added to it and exist next to the other data. RoboFab and UFO can deal with the future.
Unified Font Objects Consortium

The RoboFab developers extend an invitation to all other font tool developers to support the UFO file format, and perhaps if possible the UFO object API as well.
