=================================
What is this robofab.world thing?
=================================

RoboFab can operate in many different environments. When RoboFab is running in FontLab it needs to do different things than when you're using it on for instance Linux or Windows or OSX Python. :py:mod:`robofab.world` is a module which helps you by providing the objects and functions which are appropriate for the environment you're working in.

-------------
Portable code
-------------

Rather than include code in your scripts which try to figure out what functionality is available, and what machine, Python version etc. just ask :py:mod:`roboFab.world`. Run a script in FontLab and you'll get RoboFab objects that interface with the FontLab fonts and glyphs. Run the same script outside FontLab, and you need objects that interface with UFO files. :py:mod:`robofab.world` makes the choosing of the right objects a bit more transparent. Just import from the world module and it will pick the right one.

Using :py:mod:`robofab.world` is not compulsory - you can load the objects from the modules yourself. In some cases :py:mod:`robofab.world` doesn't even load the objects you might need. But scripts that import from :py:mod:`robofab.world` can actually work in FontLab, but also outside of it. With a bit of care, your scripts can work on UFO and FontLab fonts without ever noticing the difference. That saves a lot of time and effort.

----------------------
Stuff in robofab.world
----------------------

Here are the objects and functions you can import from :py:mod:`robofab.world`. If you want to see exactly when and which object are selected, have a look in the :py:mod:`robofab.world` source.

^^^^^^^^^^^^^^^^^^^
robofab.world.world
^^^^^^^^^^^^^^^^^^^

A collection of parameters about the world RoboFab works in. When the :py:mod:`robofab.world` module is loaded, the first time you call for it, it creates an instance of a special object which catalogs as much as possible about the environment it woke up in. This object is also called ``world``. It's simpler than it sounds really, have a look at the examples.

In the Python IDE it looks like this:

>>> from robofab.world import world
>>> print world
[Robofab is running on darwin.
Python version: 2.3, 
Mac stuff: X, 
PC stuff: None, 
FontLab stuff: False, 
FLversion: None]

In a FontLab macro (Mac FontLab) it looks like this:

>>> from robofab.world import world
>>> print world
[Robofab is running on mac.
Python version: 2.3,
Mac stuff: pre-X,
PC stuff: None,
FontLab stuff: True,
FLversion: 4.6.1/Mac]

See the difference?

^^^^^^^^^^^^^^
OpenFont(path)
^^^^^^^^^^^^^^

``OpenFont`` is a function which opens a font. When called with a path it will open the font at that location. Without a path it will try to offer some appropriate interface to pick a font. In FontLab, ``OpenFont()`` gives you the standard font-opening-interface, and ``OpenFont(path)`` will open a FontLab font window for that font. Outside FontLab, for instance in the Python IDE, you get a file dialog to point at a UFO package. If you look at the source code of OpenFont, you'll see that it is not just one function, there are several for different kinds of environments. By importing ``OpenFont`` from :py:mod:`robofab.world`, your script always has the right one and you don't have to change it when the script moves from one environment to the other.

In places where there is no UI available, for instance when RoboFab is running on a Linux server, ``OpenFont(path)`` might try to import UI parts and fail. If you already know the path of a font, use :py:class:`RFont(path)` instead.

>>> from robofab.world import OpenFont
>>> f = OpenFont()
>>> # dialog appears
>>> print f
< Font MyFont >

^^^^^^^^^^^^^
CurrentFont()
^^^^^^^^^^^^^^

``CurrentFont`` is an old favorite from RoboFog. It returns a font object for the top most font or the last imported font. It is very useful to write short scripts that manipulate the current font in one way or the other, so you don't have to enter the font's name.

>>> from robofab.world import CurrentFont
>>> f = CurrentFont()
< RFont font for MyFontOT-Regular >

^^^^^^^^^^^^^^
CurrentGlyph()
^^^^^^^^^^^^^^

``CurrentGlyph`` is similar to ``CurrentFont``, except that it returns the top most glyph. ``CurrentGlyph`` returns ``None`` when there isn't a glyph window open.

>>> from robofab.world import CurrentGlyph
>>> g = CurrentGlyph()
< RGlyph for unnamed_font.L >

^^^^^^^^^^
AllFonts()
^^^^^^^^^^

``AllFonts`` returns a list with font objects for all fonts which are 'open' at the moment. In FontLab that means one :py:class:`RFont` object for each font window. Outside FontLab it means a list of all font objects that exist at the moment. Note: it is possible to have more than one font object for the same UFO, so if you use ``AllFonts`` for UFOs you need to take that into account. ``AllFonts`` is easy if you want to do something to all open fonts.

>>> from robofab.world import AllFonts
>>> for f in AllFonts():
>>>     print f
< RFont for aFont-Plain.00 >
< RFont for aFont-Italic.00 >
< RFont for aFont-Bold.00 >

^^^^^^^^^^^^^
RFont, RGlyph
^^^^^^^^^^^^^

:py:class:`RFont` and :py:class:`RGlyph` classes are also loaded by :py:mod:`robofab.world`. In FontLab these objects will be imported from ``objectsFL.py`` (the FontLab implementation of the Unified Font Objects), and otherwise from ``objectsRF.py``, the UFO objects.
