================
Building accents
================

Making accented glyphs is a job where scripting can help save some time. When you have prepared all the parts, the base glyphs and the accents, a script can help to assemble the combinations. There are various ways of doing it, let's start with a simple one.::

    # robofab manual
    # Buildingaccents howto
    # usage examples
    from robofab.world import CurrentFont 
    f = CurrentFont()
    f.newGlyph("aacute")
    f["aacute"].appendComponent("a")
    f["aacute"].appendComponent("acute", (200, 0))
    f["aacute"].width = f["a"].width
    f.update()

In this example the script creates a new glyph, ``aacute``, then proceeds to add components, references to other glyphs rather than the glyphs themselves. The glyph method ``appendComponent`` is used to do this. See how the acute component has an extra argument, ``(200, 0)`` - this the offset for the accent. Finally the new glyph is given the width of the base ``a``.

This example illustrates the use of the very basic ``appendComponent`` method. But it's not a very useful way to make glyphs. For instance, the string ``aacute`` could easily be made into a variable taken from a list. And dealing with the offsets when placing the accent isn't going to be efficient either when you want to make a large list of accented glyphs. How to go about it that?

------------------------------
Building accents automagically
------------------------------

RoboFab has its own database which connects glyphnames to components. In the RoboFab distribution folder, go to ``Data/GlyphConstruction.txt``. This text file contains a list of glyphnames and from which components they should be built. The RoboFab Glyph Construction database was based on FontLab's glyph list. This list contains information about where components should be connected.::

    Acircumflexdotaccent: A circumflex.top dotaccent.bottom

This entry shows that ``Acircumflexdotaccent`` is constructed with components from ``A``, a ``circumflex`` using the ``top`` anchor, and ``dotaccent`` using the ``bottom`` anchor.

----------------
Generate a glyph
----------------

RoboFab's Font object has several ways of starting component glyphs and adding stuff to them. There are different strategies possible for different kinds of problems.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
font.generateGlyph(glyphName, replace, preflight, printErrors)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The easiest method to add an assembled glyph to a font is using the font's generateGlyph method. This will look for the glyphname in the glyph construction database and attempt to get all the components and place them at the anchors listed in the database. Let's have a look at its parameters.

**glyphName**
    the name of the glyph, has to correspond to a name in the glyph construction database.

**replace**
    default set to ``True``, the new glyph will replace the old one if it exists.

**preflight**
    default set to ``False``, preflight gives you the opportunity to run the glyph creation process without actually adding it to the font. This is useful if you're building the characterset and you don't have all the parts yet. Preflight will return a list of missing anchor points, missing accents, components, etc. Note that it can take several iterations of fixing problems and discovering new ones. If for instance a glyph for a component can't be found, it also means that some problems with that glyph are hidden. i.e. when a glyph ``A`` can't be found, preflight can't tell you that this glyph is missing a required anchor point either.

**printErrors**
    default set to ``True``, print any errors and problems to the standard output window.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
font.compileGlyph(glyphName, baseName, accentNames, adjustWidth=False, preflight=False, printErrors=True)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Compile a glyph with specified components. If you want to assemble accents that are not the glyph construction database, using compileGlyph.

**glyphName**
    the name of the glyph where it all needs to go.

**baseName**
    the name of the base glyph. ``accentNames``: a list of ``accentName``, ``anchorName`` tuples: ``[('acute', 'top'), etc]``

**preflight**
    default set to ``False``, preflight gives you the opportunity to run the glyph creation process without actually adding it to the font. This is useful if you're building the characterset and you don't have all the parts yet. Preflight will return a list of missing anchor points, missing accents, components, etc.

**printErrors**
    default set to ``True``, print any errors and problems to the standard output window.

-------------
AccentBuilder
-------------

RoboFab comes with a versatile accent building tool, ``AccentBuilder``. Have a look at :py:mod:`robofab.tools.accentbuilder`. ``AccentBuilder`` deals with components, anchorpoints.::

    # robofab manual
    # Buildingaccents howto
    # AccentBuilder examples
     
    from robofab.world import CurrentFont
    from robofab.accentBuilder import AccentTools, buildRelatedAccentList
     
    font = CurrentFont()
     
    # a list of accented glyphs that you want to build
    myList = ['Aacute', 'aacute']
     
    # search for glyphs related to glyphs in myList and add them to myList
    myList = buildRelatedAccentList(font, myList)+myList
     
    # start the class
    at = AccentTools(font, myList)
     
    # clear away any anchors that exist (this is optional)
    at.clearAnchors()
     
    # add necessary anchors if you want to
    at.buildAnchors(ucXOffset=20, ucYOffset=40, lcXOffset=15, lcYOffset=30)
     
    # print a report of any errors that occured
    at.printAnchorErrors()
     
    # build the accented glyphs if you want to
    at.buildAccents()
     
    # print a report of any errors that occured
    at.printAccentErrors()

--------------------------------
Building your own accentbuilders
--------------------------------

For typeface production it is a good idea to build a set of standardised tools with which you finalise the font data. Here's an example of a script which adds a standardised list of accents to a font. It does not do automatic anchor placement because the scripter wanted to do this manually. But the rest is done automatically. The script also deals correctly with smallcap glyphnames with ``.sc``.::

    # robofab manual
    # Buildingaccents howto
    # attribute examples
    
    # a script to generate all necessary accented characters.
    # this assumes all anchor points are set correctly.
    # including doublelayer accents. so, add anchorpoints 
    # on the accents too!
    # (c) evb
     
    from robofab.world import CurrentFont
    from robofab.tools.toolsAll import readGlyphConstructions
     
    f = CurrentFont()
     
    import string
     
    theList = [
        # caps
        'AEacute',
        'AEmacron',
        'Aacute',
        'Abreve',
        # add all the accents you want in this list
    ]
    
    con = readGlyphConstructions()
    theList.sort()
     
    def accentify(f, preflight=False):
        print 'start accentification', f.info.fullName
        slots = con.keys()
        slots.sort()
        for k in theList:
            if k[-3:] in [".sc"]:
                isSpecial = True
                tag = k[-3:]
                name = k[:-3]
            else:
                isSpecial = False
                tag = ""
                name = k
            parts = con.get(name, None)
            if parts is None:
                print k, "not defined?"
                continue
            base = parts[0]
            accents = parts[1:]
            f.generateGlyph(k, preflight=preflight)
            f[k].mark = 100 + randint(-20, 20)
            f[k].autoUnicodes()
            f[k].update()
        f.update()
     
    accentify(f)
    print 'done'
