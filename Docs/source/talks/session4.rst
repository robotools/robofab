Adventures in NoneLab, scripting outside the box
================================================

Working with text sources UFO, and GLIFs. FontLab export and import of UFO. Processing UFOs outside FontLab.

UFO
---

Scripting a font editor without the font editor? RoboFab can export and import to the text based `UFO format`_ for font sources. You can export a FontLab font to ``.ufo``, and you can import a ``.ufo`` to FontLab easily. Read the :doc:`how-to <../howtos/makeufo>`. UFO export and import scripts are available from the RoboFab Scripts menu. But what do you do with ufos then?

.. _UFO format: http://unifiedfontobject.org/

Scripting with fonts outside FontLab
------------------------------------

The nice thing about UFO is that RoboFab can read the files even when it is not running in FontLab. The Python interpreter that you use for FontLab, can run RoboFab scripts and apply them to font and glyphs stored in a UFO rather than a ``.vfb``. That opens possibilities for batch processing, storage in databases or version management systems, archiving or connecting your own tools to your workflow. FontLab specific functionality, such as generating font binaries, and complex path manipulations are not available in the **NoneLab** RoboFab, but you can make fonts, create and move glyphs, generate and manipulate kerning. We've taken great care to make sure that RoboFab based scripts work in both worlds.

NoneLab
-------

NoneLab is a word we coined to describe RoboFab/Python environments outside FontLab. Let's have a look at main the differences.

+---------------------------+-----------------------------+-----------------------------------------------------------+
|                           | FontLab                     | NoneLab                                                   |
+===========================+=============================+===========================================================+
| Font binary generation    | All formats. Import,        | Read, write UFO. Read TT, OTF, PS T1 (through             |
|                           | export UFO.                 | ``fontTools``). Experimental support for SVG fonts.       |
+---------------------------+-----------------------------+-----------------------------------------------------------+
| ``CurrentFont``,          | Yes.                        | No. Use ``OpenFont(aPathToUFO)`` instead, or open the     |
| ``CurrentGlyph``,         |                             | ``.ufo`` fonts with ``RFont(aPathToUFO)``.                |
| ``AllFonts``              |                             |                                                           |
+---------------------------+-----------------------------+-----------------------------------------------------------+
| Interpolation             | Yes.                        | Yes -- quite a bit faster too.                            |
+---------------------------+-----------------------------+-----------------------------------------------------------+
| Make new fonts, move      | Yes.                        | Yes.                                                      |
| glyphs, merge, split      |                             |                                                           |
| files                     |                             |                                                           |
+---------------------------+-----------------------------+-----------------------------------------------------------+
| Build accented glyphs     | Yes.                        | Yes.                                                      |
+---------------------------+-----------------------------+-----------------------------------------------------------+
| Manipulate kerning        | Yes.                        | Yes.                                                      |
+---------------------------+-----------------------------+-----------------------------------------------------------+
| Remove overlap            | Yes.                        | No.                                                       |
+---------------------------+-----------------------------+-----------------------------------------------------------+
| API                       | All RoboFab objects.        | All RoboFab objects.                                      |
|                           | Plus the underlying         |                                                           |
|                           | FontLab objects.            |                                                           |
+---------------------------+-----------------------------+-----------------------------------------------------------+
| Platform                  | Mac OSX, Windows,           | All platforms which support Python, Mac OSX, Windows,     |
|                           | within FontLab              | Linux, Unix.                                              |
+---------------------------+-----------------------------+-----------------------------------------------------------+
| Open file format          | No, ``.vfb`` is a           | Yes. UFO and GLIF formats are XML based, open and         |
|                           | proprietary, binary         | documented. You can build your own tools and use          |
|                           | file format.                | these formats.                                            |
+---------------------------+-----------------------------+-----------------------------------------------------------+
| Widgets, UI toolkit       | DialogKit, plus the         | When run as a window-less user in OSX or linux the        |
|                           | set of basic windows        | interface things are disabled. In some Python IDE's:      |
|                           | from ``robofab.interface``. | the set of basic windows from ``robofab.interface``.      |
|                           |                             | On OSX: Vanilla.                                          |
+---------------------------+-----------------------------+-----------------------------------------------------------+

The UFO
-------

A UFO is not really a single file, but rather a whole folder full of stuff with a ``.ufo`` extension in the name. So you can open up a ``.ufo`` and have a look inside. Some data is stored in ``.plist`` format. This is a flavor of XML and contains kerning, lib and font info. The glyphs are stored level deeper, in the glyphs folder.

.. image:: ../../images/ufo.jpg

The ``MyFont.ufo/glyphs/`` folder contains a list of ``.glif`` files and a single ``contents.plist`` file. This is the table of contents for the folder, it contains a table of glyph name to file name mappings. So when you start working with a ``.ufo`` and you want a particular glyph, RoboFab can find it faster.

The GLIF
--------

GLyph Interchange Format, a readable XML based file with all data for a single glyph: width, unicode value, all contours, points and components. The ``glyph.lib`` is also stored here.

.. image:: ../../images/cent.gif

These screenshots are taken on an OSX machine, but the data is platform independent. Basically you can take any text editor and mess around with the points. While this is not a very efficient way to design type, it shows that the data is still there, accessible forever.

Exporting UFO
-------------

In the FontLab scripts folder that is distributed with RoboFab, you will find a set of scripts for importing and exporting UFO and GLIF. Open a test font and run this script from the Macro menu. It will generate a ``.ufo`` in the same folder as the source font file.

.. image:: ../../images/exportmenu.gif

FontLab Remote
--------------

If you happen to be using FontLab in Mac, you can use the FontLab Remote module to make FontLab receive Python instructions and data by **AppleEvents**. You need to start the AppleEvent handler by importing the ``robofab.tools.remote`` module. After importing it, FontLab can receive instructions by AppleEvent. You need to call remote once after starting FontLab. Now external scripts running outside FontLab can call the FontLab application, send it glyphs, get results back::

    # start the AppleEvent handler
    import robofab.tools.remote
    FontLabRemote is on.

The following script needs to be run in a python IDE. It will ask FontLab for its current glyph, and then it will store this glyph in a new font object outside FontLab.

.. showcode:: ../../examples/talks/nonelab_00.py

.. code::

    <RGlyph for None.parenright>
    ['parenright']
