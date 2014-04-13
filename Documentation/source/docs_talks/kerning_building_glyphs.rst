===========================
Kerning and building Glyphs
===========================

-------
Kerning
-------

All kerning data of a font is represented by the ``Kerning`` object. This object behaves like a Python dictionary: the key is a tuple of two glyph or groupnames, the dictionary value is the kern distance.

In FontLab, ``font.kerning`` should not be called repeatedly like a normal attribute. Nothing will go wrong if you do, it will just be slow. The reason for this is that ``font.kerning`` is an attribute which (under the hood) has to do a lot of work to collect the data from the underlying FontLab file. Kerning in FontLab is stored at the glyph level, so to pull it up to the RoboFab level a massive iteration must occur when the kerning object is created. This happens each time you ask for the ``font.kerning`` attribute. But there's a simple way to work with that efficiently: cache the kerning object. Like so::

    >>> # robothon06
    >>> # work with kerning 1 
    >>> from robofab.world import CurrentFont
    >>> font = CurrentFont()
    >>> # now the kerning object is generated once
    >>> kerning = font.kerning
    >>> # and ready for your instructions.
    >>> print kerning
    >>> print len(kerning)
    >>> print kerning.keys()
    >>> # proceed to work with the myKerning object
    >>> # this happens in the following examples too.
    <RKerning for MyFont Normal>
    3141
    [('F', 'L'), ('D', 'G'), ('N', 'Eacute'), ..etc.. ]

The Kerning object has some useful methods to transform and analyse the data::

    >>> # robothon06
    >>> # work with kerning 2
    >>> from robofab.world import CurrentFont
    >>> font = CurrentFont()
    >>> kerning = font.kerning
    >>> 
    >>> # calculate the average offset
    >>> print kerning.getAverage()
    >>> 
    >>> # count pairs with these glyphs
    >>> print kerning.occurrenceCount(["a", "b"])
    >>> 
    >>> # get the maximum values
    >>> print kerning.getExtremes()
    >>> 
    >>> # count the pars
    >>> print "font has %d kerning pairs" % len(kerning)
    >>> 
    >>> # this prints all the pairs
    >>> for (left, right), value in kerning.items():
    >>>     print (left, right), value
    <RKerning for MyFont Normal>
    -20.5953517988
    {'a': 82, 'b': 52}
    (-191, 184)
    font has 3141 kerning pairs
    ('F', 'L') -7
    ('D', 'G') 31
    ('N', 'Eacute') -34
    ('agrave.sc', 'z') -7
    ('K', 'v') -111
    ('Z', 'N') -15
    ..etc..

In the example above you see the ``Kerning`` object as attribute of a font object, then it is cached by storing it in a new variable. ``len(kerning)`` gives you the length of the kerning dictionary, the number of kern pairs. Have a look at the attributes and methods of the :doc:`Kerning object here <../docs_objects/RKerning>`. It has some very useful methods for interpolating, sorting, combining and splitting kern tables. Back to the example, did you note that the kern pairs appear in random order? It's that Python dictionary thing again: keys of a dictionary have no particular order. Just like the example of the glyph names in a font object::

    >>> # robothon06
    >>> # work with kerning 3
    >>> # print a specific set of pairs
    >>> from robofab.world import CurrentFont
    >>> font = CurrentFont()
    >>> kerning = font.kerning
    >>> for left, right in kerning.keys():
    >>>     if kerning[(left, right)] < -100:
    >>>         print left, right, kerning[(left, right)]
    K v -111
    N Atilde -114
    W o -118
    W odieresis -118
    Acircumflex Y -103
    T e -153
    T adieresis -126
    T odieresis -133
    T aacute -126
    W eacute -141
    ..etc..

Another example of iterating through the kerning dictionary. This time each kern is tested if the value is less than ``-100``, and only when this is the case the pair is printed. This shows you how you can write code which responds to particular kinds of kerns::

    >>> # robothon06
    >>> # work with kerning 4
    >>> from robofab.world import CurrentFont
    >>> font = CurrentFont()
    >>> kerning = font.kerning
    >>> for left, right in kerning.keys():
    >>>     if left == "acircumflex":
    >>>         print left, right, kerning[(left, right)]
    acircumflex k -7
    acircumflex v -38
    acircumflex r -4
    acircumflex u -4
    acircumflex y -31
    acircumflex j -26
    ..etc..

This script prints all kerns with ``acircumflex`` as first glyph.

---------------
Building glyphs
---------------

A particularly interesting topic of scripting is building glyphs out of component parts. If a font already has all the parts, a script can, in many cases, assemble the accented versions. An overview of :doc:`glyph building options is in the how-to section of the Robofab docs <../docs_howtos/building_accents>`. The first example takes a look at all necessary ingredients: making a new glyph, adding parts and finishing it. Then we'll look at more efficient ways::

    # robothon06
    # building a glyph from parts
    # the hard way
    from robofab.world import CurrentFont
    f = CurrentFont()
    # make a new glyph
    f.newGlyph("aacute")
    # add the component for the base glyph, a
    f["aacute"].appendComponent("a")
    # add the component for the accent, acute
    # note it has an offset
    f["aacute"].appendComponent("acute", (200, 0))
    # set the width too
    f["aacute"].width = f["a"].width
    f.update()

Let's have a look at that line by line. ``f.newGlyph("aacute")``. The ``newGlyph()`` of the ``RFont`` object creates a new glyph and names it ``aacute``. Then we can get to the new glyph by asking the font. The ``Glyph`` object has a ``appendComponent()`` method, which takes a ``glyphName`` of the glyph you want to add as a component and optionally an offset coordinate. This you can see in the line where the ``acute`` glyph is added. Then the width of the new glyph is set to the width of the original glyph. Finally FontLab is told to update.

Well, that's going to be an awful lot of code if you have to write 4 lines of code for each new letter. There are other ways of going about this, using FontLab's ``Anchor`` points.

---------------------
glyph.generateGlyph()
---------------------

RoboFab has a database of glyph constructions based on the Adobe Glyph List. Have a look in your RoboFab code folder, ``robofab/Data/GlyphConstruction.txt``. The RoboFab list contains information about where components should be connected and what the anchor points are called::

    Acircumflexdotaccent: A circumflex.top dotaccent.bottom

This entry shows that ``Acircumflexdotaccent`` is constructed with components from ``A``, a ``circumflex`` using the ``top`` anchor, and ``dotaccent`` using the ``bottom`` anchor. In order to make this work, you need to add anchor points to your glyphs and accents. Check the FontLab manual for instructions. For instance the ``a`` has an anchor point named ``top``, the ``acute`` glyph has one named ``_top``::

    # building a glyph from parts
    from robofab.world import CurrentFont
    f = CurrentFont()
    font.generateGlyph("aacute")

This creates a new glyph at ``aacute``, it puts all the components in the right place and sets the width.

--------------------
glyph.compileGlyph()
--------------------

Suppose you want to create glyphs using anchor points, but the glyphs don't have entries in Robofab's ``GlyphConstruction.txt`` list. What to do? Editing ``GlyphConstruction.txt`` is not recommended because you will loose your changes when you install a new version of RoboFab. ``Glyph`` has another method: ``compileGlyph()``. This method, like ``generateGlyph``, builds a new glyph with components, but you get to provide the list and tell which anchor points you want to use. ``compileGlyph`` takes a list of accents and anchors. It will follow the list and allow "stacking" of accents::

    # robothon06
    # Compile a new glyph from a list of accents and required anchors
    # Demo of multiple accents chaining together, or "stacking".
    # For this example you need to set  up a couple of things
    # in your test font:
    # - base glyph "a", with anchor "top" and anchor "bottom"
    # - glyph "dieresis" with anchor "_top" and anchor "top"
    # - glyph "acture" with anchor "_top"
    # - glyph "cedilla" with anchor "_bottom"
    
    from robofab.world import CurrentFont
    font = CurrentFont()
    
    # this is a list of tuples
    # each tuple has the name of the accent as first element
    # and the name of the anchor which to use as the second element
    
    accentList = [("dieresis", "top"),
        ("acute", "top"),
        ("cedilla", "bottom")]
    
    # The accents are compiled in this order, so first
    #    "dieresis" connects to "a" using "top" anchor
    #    "acute" connects to dieresis, using the next "top" anchor
    
    font.compileGlyph("myCompiledGlyph", "a", accentList)
    font.update()
