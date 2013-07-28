=============
Using the lib
=============

The lib is very much like a plain dictionary: you use keys to store stuff in it. The nice thing about them is that they save their contents in the font and are available (after the font is saved) to scripts the next time you open the file again. In FontLab the libs (because there are several) are stored in the ``.vfb`` source. In UFO based fonts the :py:attr:`font.libs` end up in their own, XML based ``.plist`` files, inside th UFO package. The :py:attr:`Glyph.libs` end up in the ``.glif`` files.

----------
Which lib?
----------

Sometimes it is handy to store values directly in the font that needs them. Rather than saving something in a seperate file (which could easily get lost), you can store data like this in the lib. A :py:class:`RFont` has a lib and each single :py:class:`RGlyph` has a lib as well. RoboFog users might remember the various applications. It is likely that stuff will collect in the font and glyph libs, so it is wise to pay some attention to naming the entries. If you use undescriptive or generic names like ``a`` or ``mydata``, there's a chance that another script will overwrite the data. So the RoboFab developers propose to use the 'reverse domain name scheme' which works out something like this::

    # storing something that belongs to a letterror script
    aFont.lib['com.letterror.develop.markers']
     
    # storing something that belongs to a aFoundry script
    aFont.lib['com.aFoundry.bud.notes']

The lib is a flat dictionary. For RoboFog users: the RoboFog lib nested and tried to be very clever. Unfortunately it meant that sometimes data would get lost in confusing situations. A flat dictionary solves that.

.. note :: In FontLab version 4.5 and 4.6 there's a nasty bug which causes FontLab to crash after something has been added to the ``font.customdata`` or ``glyph.customdata`` fields. Unfortunately these fields were used to store the ``robofab.font.lib`` and ``robofab.glyph.lib`` data. We hope future versions of FontLab will address this. In UFO files the libs for font and glyphs work fine.

^^^^^^^^^
aFont.lib
^^^^^^^^^

:: 

    # robofab manual
    # Usethelib howto
    # aFont.lib examples

^^^^^^^^^^^^
anyGlyph.lib
^^^^^^^^^^^^

::

    # robofab manual
    # Usethelib howto
    # anyGlyph.lib examples