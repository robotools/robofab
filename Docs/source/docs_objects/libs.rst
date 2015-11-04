====
RLib
====

-----
Usage
-----

.. showcode:: ../../Examples/objects/RLib_00.py

.. code::

    < RLib for Salmiak-Regular >
    ['org.robofog.ufoExport.date',
     'org.robofog.ufoExport.encoding.current',
     'org.robofog.ufoExport.font.italicOffset',
     'org.robofog.ufoExport.sourcePath']

-----------
Description
-----------

``RFont`` and ``RGlyph`` objects get lib objects when they're created, so you don't have to explicxitly make one. Lib objects behave like normal dictionaries.

^^^^^^^^^^^^^^^^^^^^^^^^^^
Where is this data stored?
^^^^^^^^^^^^^^^^^^^^^^^^^^

In RoboFab 1.0 and FontLab 4.6.1, the lib is saved inside the (FontLab native attributes!) ``glyph.customdata`` and ``font.customdata`` in the ``.vfb`` file.

.. note::

 A bug in FontLab 4.6.1 prevents the ``glyph.lib`` from being used: when data is stored in this field, the font can no longer be edited. FontLab Studio 5 introduces a new attribute customdict which is exclusively for storing Python data. Early tests indicate that RoboFab storage of lib data can move to this attribute, but further testing and introduction of the MacOS version are needed before RoboFab's Lib support can move to it. In UFO based fonts the libs are stored as ``.plist`` in the UFO. Have a look at :doc:`how to use the lib <../docs_howtos/use_lib>`.

-------
Methods
-------

.. py:function:: keys()

Return a list of the keys. Normal dictionary stuff.
