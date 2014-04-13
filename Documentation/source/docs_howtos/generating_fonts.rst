================
Generating Fonts
================

A ``RFont`` object in FontLab can call FontLab to generate fonts. Generating fonts can be time consuming, even when all the right parameters are set. So this is a nice candidate for automation. First of all a generator script will give you consistency between generations and versions. But also it means you can set a machine to work to generate batches of fonts and focus on more creative tasks.

.. note::

    The generate method only calls on FontLab to generate the fonts in a particular format. It does not prepare the font data for that specific format, i.e. for example when you're generating for PC Truetype, ``generate()`` won't select the appropriate encodings or special windows flags. You need to do that.

-------------------------------------
RFont.generate(outputType, path=None)
-------------------------------------

Generate the font. ``outputType`` is the type of font to output. An overview of available output types in FontLab:

pctype1
    PC Type 1 font (binary/PFB)

pcmm
    PC MultipleMaster font (PFB).

pctype1ascii
    PC Type 1 font (ASCII/PFA).

pcmmascii
    PC MultipleMaster font (ASCII/PFA).

mactype1
    Mac Type 1 font (generates suitcase and LWFN file).

otfcff
    PS OpenType (CFF-based) font (OTF).

otfttf
    PC TrueType/TT OpenType font (TTF).

macttf
    Mac TrueType font (generates suitcase).

macttdfont
    Mac TrueType font (generates suitcase with resources in data fork).

Docs adapted from the `Unofficial FontLab/Python API Reference <http://e-font.de/flpydoc/>`_.

.. note::

    The value of ``path`` can be a directory or a directory file name combo:

    - ``path="DirectoryA/DirectoryB"``
    - ``path="DirectoryA/DirectoryB/MyFontName"``
    - ``path="DirectoryA/DirectoryB/<filename>"``

    If no ``path`` is given, the file will be output in the same directory as the ``.vfb`` file. If no file name is given, the generated file name will be the same as the ``.vfb`` file, with the appropriate suffix.

--------
Examples
--------

FontLab can generate many different formats for different platforms. Please refer to the FontLab manual for specifics. Some formats generate several files, others only one. Some formats are not available in all versions of FontLab::

    # robofab manual
    # Generatefonts howto
    # usage examples
    import os.path
    from robofab.world import CurrentFont
    font = CurrentFont()
    path = font.path
    dir, fileName = os.path.split(path)
    path = os.sep.join([dir, font.info.fullName])
    font.generate('mactype1', path)
