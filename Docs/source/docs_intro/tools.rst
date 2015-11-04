=====
Tools
=====

The RoboFab Tools directory contains a groups of useful and sometimes stray bit of code which don't fit anywhere else.

----------------------
robofab.tools.toolsAll
----------------------

ToolsAll contains useful functions for any and all implementation of RoboFab. It does (or should not) contain any platform or version specific code. Some of this code is used by other parts of RoboFab. The user serviceable parts are discussed here.

.. py:function:: toolsAll.readFoundrySettings(dstPath)

Read the foundry settings xml file and return a keyed dict. The idea is that a foundry will have certain, ofter recurring preferences for some fields in fonts. For instance foundry names, codes etc. These can be stored in ``.plist`` format, at a particular location. It's up to the user to make sure the values make sense and to keep track of the file.

.. py:function:: toolsAll.fontToUFO(src, dst, fileType=None)

Open a font binary pointed to by src, decompile it using fontTools and write a UFO at location dst. If no filetype is given, ``fontToUFO`` attempts to guess the type. Valid types are TTF and "Type 1". While this function does a good job at extracting contours and basic font information, it is possible that not all values are extracted. Please refer to the result UFO for a precise overview.

---------------------
robofab.tools.toolsFL
---------------------

Tools for use within FontLab. Some of the functions in ``toolsFL`` are available through ``robofab.world``. The user serviceable parts are discussed here.

.. py:function:: toolsFL.AppFolderRenamer()

``AppFolderRenamer`` renames the directory the FontLab application is in. It attempts to add the version number of the application to the folder name. This can be helpful to keep different versions of FontLab separated.

.. warning:: It messes with the paths of your app, if you have items that hardwired to this path you'd be in trouble.

.. py:function:: toolsFL.MakeTempFont(font, dupemark=None, removeOverlap=True, decompose=True)

Save the current FL Font,

- close the file
- duplicate the file in the Finder (icon looks weird, but it works)
- open the duplicate
- decompose the glyphs
- remove overlaps
- return the ``Font`` object

``font`` is either a FL ``Font`` or RF ``RFont`` object.

.. note:: It will overwrite older files with the same name.

.. warning:: Doesn't check if the filename is getting too long.

.. py:function:: toolsFL.makePSFontName(name)

Create a PostScript filename out of a regular PostScript fontname, using the old fashioned macintosh 5:3:3 convention.

---------------------
robofab.tools.toolsRF
---------------------

These are no special tools for RF or NoneLab use at the moment.
