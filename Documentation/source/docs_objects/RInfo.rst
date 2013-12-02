=====
RInfo
=====

-----
Usage
-----

>>> # robofab manual
>>> # Info object
>>> # usage examples
>>> from robofab.world import CurrentFont
>>> f = CurrentFont()
>>> print f.info.postscriptFullName
>>> print f.info.openTypeNameDesigner
>>> f.info.openTypeNameDesigner = "Jan van Krimpen"
>>> print f.info.openTypeNameDesigner
>>> print f.info.openTypeOS2VendorID
>>> print f.info.unitsPerEm
>>> print f.info.xHeight
>>> print f.info.openTypeNameLicenseURL
>>> # but you can set the values as well
>>> f.info.postscriptUniqueID = 4309359
>>> f.info.openTypeNameDesigner = "Eric Gill"
MyFont Regular
Huib van Krimpen
Jan van Krimpen
LTTR
1000
307
#etc.

-----------
Description
-----------

:py:class:`RInfo` contains all names, numbers, URL's, dimensions, values, etc. that would otherwise clutter up the font object. You don't have to create a :py:class:`RInfo` object yourself, :py:class:`RFont` makes one when it is created. In FontLab the :py:class:`RInfo` data is tunneled to the appropriate places in the FontLab font. In UFO land the data ends up in ``info.plist``. In all implementations :py:class:`RInfo` doesn't check the validity of the entries, it just provides storage or access to them.

---------------------------
Complete list of attributes
---------------------------

RoboFab version 1.2 implements new :py:class:`RInfo` objects with extended attributes. The old attributes still work, but print a deprecation warning when they're accessed. Scripts written with UFO1 attributes should work. The specification of UFO2 has its own site, UnifiedFontObject.org. The :py:mod:`objectsRF` :py:class:`RInfo` object implements all attributes listed, the :py:mod:`objectsFL` implementation misses a couple as the fields are not supported in FontLab. Please have a look at the overview of all RoboFab 1.2 / UFO2 font.Info attributes.