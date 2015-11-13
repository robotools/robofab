Scripting for production
========================

Production
----------

In the production phase of a font it all comes together: moving stuff around, naming, interpolations, quality control, generating, database work, it pays to invest some time (or money) in some really good scripts. Each foundry and designer has their own preferred ways of doing things. It's impossible to describe one production process and please everyone. So instead we're going to look at some of the things you probably have to do anyway. You will have to match and adapt for your own methods.

Production scripts can save a lot of time. But be careful: it is costly to make mistakes with your production sources. Make sure to *test* production scripts first on duplicate data, preferably in a different folder. Doing something "quickly" to a massive kerning table only to discover it was your only copy, and the action was wrong -- will not save you any time. Like carpentry: measure twice, cut once.

Batch processing
----------------

Here are some examples of applying changes to several fonts at once using ``AllFonts()``. Keep in mind that this applies to all fonts you have open in FontLab. So make sure to close any fonts that you don't want treated this way before running the script:

.. showcode:: ../../examples/talks/session6_00.py

Obviously you can extend these to do lots more:

.. showcode:: ../../examples/talks/session6_01.py

This is a more complex script. It iterates through all open fonts, collects some data in each and finally asks for a place to save all the data in a text file:

.. showcode:: ../../examples/talks/session6_02.py

This asks for a folder, then proceeds to save all open fonts in this folder:

.. showcode:: ../../examples/talks/session6_03.py

Here you can pick two fonts from the open fonts. The script will create a new, third font, and make interpolations with the interpolation factors in the ``values = [.3, .6]`` list. The interpolated font is then saved in the same folder as the first master.

This touches on a slippery problem which can cause a lot of confusion. Robofab can only tell FontLab fonts apart from their path attribute, the place where each font is saved. A newly created font has not been saved yet, so it has no path. The effect is that when you have more than one new, unsaved font open, Robofab can't tell them apart (for a couple of reasons) and will continue to work with the first one. It will look like nothing is happening when you run a script. The way around this is to make sure you save each font you created with a script before creating another one. This is safer anyway.

Here are some useful bits for batch processing fonts which are not open, but in a file. This script is a way to make python collect all files of a particular kind in a folder or folders within that folder. You can use the ``walker`` function outside of this script too, it's a useful thing to know:

.. showcode:: ../../examples/talks/session6_04.py

.. code::

    ['/Applications/FontLab/Samples/FREESANS.VFB', '/Applications/FontLab/Samples/FREESERF.VFB']

Moving stuff around
-------------------

The moving, merging and splitting of fonts. The first example moves selected glyphs in the same font and renames them. Note that if you remove the line ``f.removeGlyph(g.name)`` the same script effectively **copies** the glyphs. Also new in this script: it iterates through the whole font and checks for each glyph if the ``g.selected`` attribute is ``1`` or ``0``. If it is ``0``, the glyph is not selected in the font window. If it is ``1``, is is selected. It then proceeds to create a new glyph name, and calls ``f.insertGlyph()`` method which takes a glyph as parameter. The optional parameter ``name`` is to be able to insert the glyph under a different name. If you don't pass a parameter for ``name``, the font will insert the glyph under its own name. The glyph can come from the same font, or a different font, or be an orphan glyph:

.. showcode:: ../../examples/talks/session6_05.py

.. code::

    moving A to A.sc
    moving C to C.sc
    moving B to B.sc

Generating font binaries
------------------------

.. showcode:: ../../examples/talks/session6_06.py

This will generate CFF flavored OpenType fonts for all open files.

.. showcode:: ../../examples/talks/session6_07.py

The script above generates fonts too, but is a bit more robust. FontLab sometimes crashes when it has to generate a long list of fonts and they're all open at the same time. This script asks you for a folder of ``.vfb`` sources (which in itself can be a useful ingredient for your own scripts). Then it will open them one by one and generate the fonts in the flavor indicated in the line ``f.generate('mactype1', dstDir)``. A list of types and their names can be found in the robofab documentation how-to page on generating fonts. This script also creates a new folder to store the generated fonts in, sorted by type.

Merging
-------

Here's a script, quite complex, for combining two fonts into one. Maybe not for the newbie, but if you're into it try to figure out how it works. It uses a couple of new concepts, like ``Sets`` and ``DigestPens``. If it is too complicated: don't worry:

.. showcode:: ../../examples/talks/session6_08.py

Dealing with Robofab limitations
--------------------------------

A handful of FontLab's own glyph and font methods are not supported in RoboFab. The reasons for this vary, some of them are very FontLab specific (for instance ``fl.productnumber`` or ``fl.username``), but most of the missing stuff was just not needed very often -- the following examples show how to get access to all functionality and attributes in the FontLab layer.

FontLab layer
-------------

To get to the FontLab layer, Robofab's Font and Glyph objects have a ``naked()`` method which returns the FontLab object. Note that you can still use the Robofab functionality like ``CurrentFont``, ``CurrentGlyph``, pens etc. The FontLab layer is documented here_. Maybe you remember the ``naked()`` method from the cookie cutter example:

.. showcode:: ../../examples/talks/session6_09.py

.. code::

    <Font: 'MyFont'>
    <Glyph: 'A', 0 nodes, parent: 'MyFont'>

.. _here: http://dev.fontlab.net/flpydoc/view_html.html

Other things you need to dig deeper for. Note that some of these objects appear to be broken.

PostScript hints
^^^^^^^^^^^^^^^^

The vertical and horizontal hint zones as well as blue values can be read and set:

.. showcode:: ../../examples/talks/session6_10.py

.. code::

    [<VHint: p=25, w=163, parent: "a">,<VHint: p=42, w=146, parent: "a">]

All name fields
^^^^^^^^^^^^^^^

The FontLab table of OpenType names, the naming record, is available. See also the `FontLab reference for NameRecord`_:

.. showcode:: ../../examples/talks/session6_11.py

.. code::

    256 1 0 0 Bold
    256 3 1 1033 Bold

.. _FontLab reference for NameRecord: http://dev.fontlab.net/flpydoc/html/NameRecord.xml.html

Encodings
^^^^^^^^^

The FontLab ``Encoding`` object. See also the `FontLab reference for Encoding`_:

.. showcode:: ../../examples/talks/session6_12.py

.. code::

    <Encoding: parent: "MyDemoRegular">
    ...
    <EncodingRecord: "eacute", unicode: 233> eacute 233
    <EncodingRecord: "ecircumflex", unicode: 234> ecircumflex 234
    <EncodingRecord: "edieresis", unicode: 235> edieresis 235
    <EncodingRecord: "igrave", unicode: 236> igrave 236
    <EncodingRecord: "iacute", unicode: 237> iacute 237
    <EncodingRecord: "icircumflex", unicode: 238> icircumflex 238
    ..etc..

.. _FontLab reference for Encoding: http://dev.fontlab.net/flpydoc/html/Encoding.xml.html
