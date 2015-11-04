===================
Font & Info objects
===================

.. image:: ../../images/RFont.gif

-----
Code!
-----

So now then, you should have your editor fired up. Your RoboFab installed. Locate the output window as well::

    import robofab.world

If that runs without problems you're good to go. If a new window pops up with a traceback like this it means there's something wrong with the installation::

    Traceback (most recent call last):
    File "<string>", line 1, in ?
    ImportError: No module named robofab.world

In this documentation, stuff in the output window is indicated with a tinted background. Whenever something is printed in Python code it will end up in the output window.

------------
Huh, import?
------------

Python can do a lot of different things. Some of its functionality is always available (the **built-in** things) but most of it is stored in separate **modules**. When you want to use code from a different module, you need to **import** it first so that Python knows it needs to look somewhere else for objects, functions and stuff. Most of the Robofab stuff is stored in the ``robofab.world`` module. Notice that dot there? The dot syntax also works for modules and modules within modules. If you want to import a module and Python can't find it, you will get a traceback with an ``ImportError``. You can also import specific things from another module, then you write::

    from someModule import oneSpecificThing
    from someModule.subModule import oneSpecificThing
    from someModule import anotherSpecificThing, andAnotherThing
     
    # and these:
    import someModule
    import someModule.subModule

We'll need to import a couple of useful functions from the robofab module to get started. To begin with, we'll look at ``CurrentFont`` and ``CurrentGlyph``. 

-------------
CurrentFont()
-------------

So, suppose you have FontLab, and a font file open. Make sure it is a font you can trash if you have to, and not the single copy of the production master of your newest bestseller. How do you get started talking to that font in Python? Use ``CurrentFont()``. This is a special function which will return an object for the font which is at the front. When there are no fonts it will return ``None``::

    >>> from robofab.world import CurrentFont
    >>> print CurrentFont()
    <RFont font for DemoFont Italic>

A :doc:`Font <../docs_objects/RFont>` object! We'll be using ``CurrentFont`` and that font object shortly, but first let's have a look at ``CurrentFont``'s siblings: ``CurrentGlyph`` and ``AllFonts``::

    >>> # open a glyph in FL first!
    >>> from robofab.world import CurrentGlyph
    >>> print CurrentGlyph()
    <RGlyph for DemoFont.ograve>

``CurrentGlyph()`` returns a :doc:`Glyph <../docs_objects/RGlyph>` object for the glyph which is at the front. So this is a useful place to start if you want to write a script which manipulates a single glyph and you want an object for that glyph::

    >>> # open a couple of fonts in FL first!
    >>> from robofab.world import AllFonts
    >>> print AllFonts()
    [<RFont font for MyDemoFont>,
    <RFont font for AnotherFont Plain>,
    <RFont font for AnotherFont Italic>]

``AllFonts()`` returns a list with Font objects, one object for each open font. ``CurrentFont``, ``CurrentGlyph`` and ``AllFonts`` are three very useful functions, and they all live in the ``robofab.world`` module. We'll be using them a lot.

--------------------
Some Font attributes
--------------------

So what are attributes of fonts objects? Let's have a look (at the documentation!)::

    >>> # open a couple of fonts in FL first!
    >>> from robofab.world import CurrentFont
    >>> font = CurrentFont()
    >>> print font.path
    >>> print font.kerning
    >>> print font.info
    /aFolder/anotherFolder/demoStuff/myFont.vfb
    <RKerning for MyFont Plain>
    <RInfo for MyFont Plain>

Hang on! that didn't print anything that looks like kerning, and what's that ``font.info`` thing? Remember that objects can contain objects? The object model splits all font related data into smaller, easier to manage pieces. So a ``Font`` object has one single ``Info`` object which in turn stores all of the naming and dimensions. Same for ``font.kerning``, it's an object which represents all kerning data of the font. We'll get back to the :doc:`kerning object <../docs_objects/RKerning>` later.

--------------------
Some Info attributes
--------------------

The Info object stores all of the :doc:`font's names, key dimensions <../docs_objects/RInfo>` etc::

    >>> # robothon06
    >>> # getting data from the info object
    >>> from robofab.world import CurrentFont
    >>> font = CurrentFont()
    >>> # naming attributes
    >>> print font.info.familyName
    >>> print font.info.styleName
    >>> print font.info.fullName
    >>> # dimension attributes
    >>> print font.info.unitsPerEm
    >>> print font.info.ascender
    >>> print font.info.descender
    MyDemo
    Plain
    MyDemo Plain
    1000
    720
    -280

Almost all attributes can also be set to new values. This is when it starts getting interesting. But it also opens new ways of messing your font up::

    >>> # robothon06
    >>> # setting data in the info object
    >>> from robofab.world import CurrentFont
    >>> font = CurrentFont()
    >>> # naming attributes
    >>> font.info.familyName = "MyFamily"
    >>> print font.info.familyName
    >>> font.info.styleName = "Roman"
    >>> print font.info.styleName
    >>> font.info.fullName = font.info.familyName + '-' + font.info.styleName
    >>> print font.info.fullName
    >>> # dimension attributes
    >>> font.info.ascender = 600
    >>> print font.info.ascender
    >>> font.info.descender = -400
    >>> print font.info.descender
    >>> font.update()
    MyFamily
    Roman
    MyFamily-Roman
    600
    -400

A useful method of the Info object is ``autoNaming()``. It assumes you have entered correct data for ``familyName`` and ``styleName``. Based on these two values, a bunch of variations and permutations are generated and stored in the appropriate fields. These are the basic names, no fancy OpenType stuff::

    >>> # robothon06
    >>> # get a particular glyph
    >>> from robofab.world import CurrentFont
    >>> font = CurrentFont()
    >>> font.info.familyName = "myFamilyName"
    >>> font.info.styleName = "myStyleName"
    >>> font.info.autoNaming()
    >>> print font.info.fullName
    >>> print font.info.fontName
    >>> print font.info.fondName
    myFamilyName myStyleName
    myFamilyName-myStyleName
    myFamilyName

-----------------
Getting to glyphs
-----------------

We've seen ``CurrentGlyph`` and ``CurrentFont``, but how do you we get to other glyphs in a font? A ``Font`` object contains glyphs and this is what you do to get to them::

    >>> # robothon06
    >>> # get a particular glyph
    >>> from robofab.world import CurrentFont
    >>> font = CurrentFont()
    >>> print font['A']
    >>> print font['Adieresis']
    >>> print font['two']
    >>> print font['afii12934']
    <RGlyph for MyFamily-Roman.A>
    <RGlyph for MyFamily-Roman.Adieresis>
    <RGlyph for MyFamily-Roman.two>
    <RGlyph for MyFamily-Roman.afii12934>

The ``Font`` object in this case behaves like a Python dictionary object. Between the ``[`` square brackets ``]`` you can ask for a glyph by its (PostScript) name. In Python speak::

    value = dictionary[key]

If you want to look at all glyphs in a font, one at a time, you can loop or iterate through the font. It's written like this::

    >>> # robothon06
    >>> # iteration through glyphs in a font
    >>> from robofab.world import CurrentFont
    >>> font = CurrentFont()
    >>> print "font has %d glyphs" % len(font)
    >>> for glyph in font:
    >>>     print glyph
    font has 201 glyphs
    <RGlyph for MyFamily-Roman.aring>
    <RGlyph for MyFamily-Roman.ordfeminine>
    <RGlyph for MyFamily-Roman.less>
    <RGlyph for MyFamily-Roman.ograve>
    <RGlyph for MyFamily-Roman.V>
    <RGlyph for MyFamily-Roman.dollar>
    <RGlyph for MyFamily-Roman.circumflex>
    ..etc..

A couple of things to look for in the example above:

- ``len(font)`` shows Python's built-in ``len()`` function, which will try to count the thing its given and it will return the number. Fonts like to be counted and they respond with the number of glyphs. In this case the font has 201 glyphs.

- All the glyphs are mixed up! there is no particular order! chaos! In Python dictionaries there is no standard order in which the keys appear. It will iterate through all the glyphs though.

- Notice the indentation at the beginning of the line under ``for glyph in font``: This is Python's way of showing that all of the code that's indented belongs to the same loop. When the code is *dedented* again that's where Python will continue when it is done with the loop.

When you want to be sure about the order in which the glyphs are looked at, you need to sort them first. Example::

    >>> # iteration through alphabetically sorted glyphnames
    >>> from robofab.world import CurrentFont
    >>> font = CurrentFont()
    >>> print "font has %d glyphs" % len(font)
    >>> # names is now a list of strings, the names of the glyphs
    >>> # not the glyphs themselves!
    >>> names = font.keys()
    >>> # the list of names is sorted
    >>> names.sort()
    >>> # now we iterate through the list of names
    >>> for glyphName in names:
    >>>     # now we ask for the glyph with glyphName
    >>>     print font[glyphName]
    >>> font has 201 glyphs
    <RGlyph for MyFamily-Roman.A>
    <RGlyph for MyFamily-Roman.AE>
    <RGlyph for MyFamily-Roman.Aacute>
    <RGlyph for MyFamily-Roman.Acircumflex>
    <RGlyph for MyFamily-Roman.Adieresis>
    <RGlyph for MyFamily-Roman.Agrave>
    <RGlyph for MyFamily-Roman.Aring>
    <RGlyph for MyFamily-Roman.Atilde>
    <RGlyph for MyFamily-Roman.B>
    ..etc..
