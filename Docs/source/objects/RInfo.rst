RInfo
=====

.. image:: ../../images/RInfo.gif

Usage
-----

.. showcode:: ../../examples/objects/RInfo_00.py

.. code::

    MyFont Regular
    Huib van Krimpen
    Jan van Krimpen
    LTTR
    1000
    307
    #etc.

Description
-----------

``RInfo`` contains all names, numbers, URL's, dimensions, values, etc. that would otherwise clutter up the font object. You don't have to create a ``RInfo`` object yourself, ``RFont`` makes one when it is created. In FontLab the ``RInfo`` data is tunneled to the appropriate places in the FontLab font. In UFO land the data ends up in ``info.plist``. In all implementations ``RInfo`` doesn't check the validity of the entries, it just provides storage or access to them.

Complete list of attributes
---------------------------

RoboFab version 1.2 implements new ``RInfo`` objects with extended attributes. The old attributes still work, but print a deprecation warning when they're accessed. Scripts written with UFO1 attributes should work. The specification of UFO2 has its own site, `UnifiedFontObject.org`_. The ``objectsRF.RInfo`` object implements all attributes listed, the ``objectsFL`` implementation misses a couple as the fields are not supported in FontLab. Please have a look at the `overview of the UFO2 font.info attributes`_.

.. _UnifiedFontObject.org: http://unifiedFontObject.org/
.. _overview of the UFO2 font.info attributes: http://unifiedfontobject.org/versions/ufo2/fontinfo.html
