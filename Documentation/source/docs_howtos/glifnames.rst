============================
Glyphnames versus GLIF-names
============================

The names of the GLIF xml files, in the UFO are related to the glyph names. It used to be a 1:1 relationship, but then glyphnames grew really long and some file systems don't support long filenames. So something had to give.

------------------
GlyphNamingSchemes
------------------

The ``objectsFL.RFont.writeUFO()`` method can take a special callback function in order to convert the actual glyphname to a suitable filename. The goal is to create unique filenames so that glyphs won't overwrite each other's exports, also comply to certain filesystems which require filenames to be shorter than a certain number of characters, while retaining a high level of human-readability. Have a look at ``robofab/tools/glyphNameSchemes.py`` for the currently available callbacks. With ``glyphNameSchemes``, the ``glyphName`` and the ``.glif`` filename no longer have a direct relationship.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
glyphNameToShortFileName(glyphName, glyphSet)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Features a guaranteed maximum filename (default 31 characters) for really long glyphnames, and clash testing.

- All non-ascii characters are converted to ``_`` (underscore), including ``.`` (period).
- All glyphnames which are too long are truncated and a hash is added at the end.
- The hash is generated from the whole glyphname.
- Finally, the candidate glyphname is checked against the ``contents.plist`` and a incrementing number is added at the end if there is a glyph with that name already.

``glyphNameToShortFileName`` is the **default naming scheme** for exporting UFOs from FontLab. For most everyday use, this callback does all the work and there is no need to tweak it. Below are some examples to give you an idea of what the callback does::

    >>> # robofab manual
    >>> # Glifnames howto
    >>> # glyphNameToShortFileName examples
    >>> 
    >>> # examples of glyphname to glif name transformations
    >>> from robofab.tools.glyphNameSchemes import glyphNameToShortFileName
    >>>  
    >>> # a short name
    >>> print glyphNameToShortFileName("accent", None)
    >>>  
    >>> # a short name, starting with capital letter
    >>> print glyphNameToShortFileName("Accent", None)
    >>>  
    >>> # a really long name - note the hexadecimal hash at the end
    >>> print glyphNameToShortFileName("this_is_a_very_long_glyph_name.altswash2", None)
    >>>  
    >>> # a name with a period in it, 1
    >>> print glyphNameToShortFileName("a.alt", None)
    >>>  
    >>> # a name with a period in it, 2
    >>> print glyphNameToShortFileName(".notdef", None)
    "accent.glif"
    "A_ccent.glif"
    "this_is_a_very_lon340a8fa5.glif"
    "a_alt.glif"
    "_notdef.glif"
    "_nic_de.glif"
