How to make a UFO
=================

Exporting a FontLab font to UFO is easy:

1. Open the ``.vfb``.
2. Select the *RoboFabUFO* menu in the Macro toolbar.
3. Select the *Export Current Font to UFO Format* script.
4. Run it.

The ``.ufo`` will be in the same directory as the original ``.vfb`` file. Have an in-depth look at the :doc:`ufo format here <../intro/ufo>`.

.. note:: If you want to export a new FontLab font to UFO, **it is important that you save the font to .vfb first**.

Importing a UFO into FontLab
----------------------------

1. Select the *RoboFabUFO* menu in the Macro toolbar.
2. Select the *Import .ufo File into FontLab* script.
3. Run it.

This script create a new, empty FontLab font, then proceed to ask you for a ``.ufo`` directory.

.. note:: Due to some limitations in how FontLab keeps track of new, untitled, unsaved fonts, it is vital to **make sure that there are no other unsaved, untitled fonts open** when you run this script. Because if there are, FontLab will be confused about where to import the glyphs from the ``.ufo`` and none of the fonts will show the new glyphs. It's ok to have other fonts open when importing ``.ufo``, they just to have been saved previously.

Importing a bunch of UFO's into FontLab
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

What if you need to import a whole family of UFO's?

1. Select the *RoboFabUFO* menu in the Macro toolbar.
2. Select the *Import all UFOs in a folder* script.
3. Run it.

This script will prompt you for a folder with UFO's. Pick one. The script will proceed to import the UFO's one by one.

.. note:: Sometimes, some versions of FontLab can get a bit tired of importing UFO's in a batch. When this happens not all UFO's will be imported and FontLab may crash. When this happens, just import the fonts one by one.

Making a UFO from a font binary
-------------------------------

Using ``fontTools`` you can make a UFO directly from a font binary. This is very fast, and it works outside of FontLab, but not all data (for instance kerning and apparently metrics) is imported. So your mileage may vary:

.. showcode:: ../../examples/howtos/makeUFO_00.py
