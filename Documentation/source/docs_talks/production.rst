========================
Scripting for production
========================

----------
Production
----------

In the production phase of a font it all comes together: moving stuff around, naming, interpolations, quality control, generating, database work, it pays to invest some time (or money) in some really good scripts. Each foundry and designer has their own preferred ways of doing things. It's impossible to describe one production process and please everyone. So instead we're going to look at some of the things you probably have to do anyway. You will have to match and adapt for your own methods.

Production scripts can save a lot of time. But be careful: it is costly to make mistakes with your production sources. Make sure to test production scripts first on duplicate data, preferably in a different folder. Doing something "quickly" to a massive kerning table only to discover it was your only copy, and the action was wrong — will not save you any time. Like carpentry: measure twice, cut once.

----------------
Batch processing
----------------

Here are some examples of applying changes to several fonts at once using :py:func:`AllFonts()`. Keep in mind that this applies to all fonts you have open in FontLab. So make sure to close any fonts that you don't want treated this way before running the script.::

    # robothon06
    # set font info in all fonts
    from robofab.world import AllFonts
    for font in AllFonts():
        font.info.familyName = "MyFamily"
        font.info.ascender = 700
        font.info.descender = -300
        font.update()

Obviously you can extend these to do lots more.::

    # robothon 2006
    # get info attributes for all fonts
    # and dump them to a text file
     
    from robofab.world import AllFonts
    from robofab.interface.all.dialogs import PutFile
     
    text = []
     
    for font in AllFonts():
        text.append(str(font.path))
        text.append(str(font.info.familyName))
        text.append(str(font.info.styleName))
        text.append(str(font.info.fullName))
        text.append(str(font.info.unitsPerEm))
        text.append(str(font.info.ascender))
        text.append(str(font.info.descender))
        text.append('')
     
    text = '\n'.join(text)
    path = PutFile('Save file as:')
    if path:
        file = open(path, 'w')
        file.write(text)
        file.close()

This is a more complex script. It iterates through all open fonts, collects some data in each and finally asks for a place to save all the data in a text file.::

    # robothon 2006
    # batch save as
     
    import os
    from robofab.world import AllFonts
    from robofab.interface.all.dialogs import GetFolder
     
    path = GetFolder()
    if path:
        for font in AllFonts():
            fileName = os.path.basename(font.path)
            newPath = os.path.join(path, fileName)
            font.save(newPath)

This asks for a folder, then proceeds to save all open fonts in this folder.::

    # robothon 2006
    # batch interpolate
     
    import os
    from robofab.world import SelectFont, NewFont
     
    # ask for two masters to interpolate:
    font1 = SelectFont("Select font 1")
    font2 = SelectFont("Select font 2")
    # these are the interpolation factors:
    values = [.3, .6]
     
    for value in values:
        # make a new font
        destination = NewFont()
        # do the interpolation
        destination.interpolate(value, font1, font2, doProgress=True)
        destination.update()
        # make a new path + filename for the new font to be saved at:
        dir = os.path.dirname(font1.path)
        fileName = "Demo_%d.vfb" % (1000 * value)
        # save at this path and close the font 
        destination.save(os.path.join(dir, fileName))
        destination.close()

Here you can pick two fonts from the open fonts. The script will create a new, third font, and make interpolations with the interpolation factors in the ``values = [.3, .6]`` list. The interpolated font is then saved in the same folder as the first master.

This touches on a slippery problem which can cause a lot of confusion. Robofab can only tell FontLab fonts apart from their path attribute, the place where each font is saved. A newly created font has not been saved yet, so it has no path. The effect is that when you have more than one new, unsaved font open, Robofab can't tell them apart (for a couple of reasons) and will continue to work with the first one. It will look like nothing is happening when you run a script. The way around this is to make sure you save each font you created with a script before creating another one. This is safer anyway.

Here are some useful bits for batch processing fonts which are not open, but in a file. This script is a way to make python collect all files of a particular kind in a folder or folders within that folder. You can use the :py:func:`walker` function outside of this script too, it's a useful thing to know.

>>> # robothon06
>>> # ask for a folder
>>> # find (nested) fontlab files in the folder
>>> # open the fonts
>>> # Demonstrates: recursive function,, dialog, os module
>>>  
>>> import os.path
>>> from robofab.interface.all.dialogs import GetFolder
>>> from robofab.world import OpenFont
>>>  
>>> # this function looks for fontlab files in a folder 
>>> def walk(someFolder, extension):
>>>     extension = extension.lower()
>>>     files = []
>>>     # the os module has tools to deal with
>>>     # the operating system. This returns a list of names
>>>     # of stuff in the folder you feed it:
>>>     names = os.listdir(someFolder)
>>>     for n in names:
>>>             p = os.path.join(someFolder, n)
>>>             # if this new thing is a folder itself,
>>>             # call this function again, but now with the
>>>             # new path to check that as well. This is
>>>             # called recursion.
>>>             if os.path.isdir(p):
>>>                 # add the results of the other folder
>>>                 # to the list
>>>                 files += walk(p, extension)
>>>                 continue
>>>             # is it a file with the extension we want?
>>>             # add it then!
>>>             if n.lower().find(extension) <> -1:
>>>                 files.append(p)
>>>     return files
>>> 
>>> yourFolder = GetFolder("Search a folder:")
>>> if yourFolder is not None:
>>>     fontPaths = walk(yourFolder, ".vfb")
>>>     for path in fontPaths:
>>>         OpenFont(path)
>>> 
['/Applications/FontLab/Samples/FREESANS.VFB', '/Applications/FontLab/Samples/FREESERF.VFB']

-------------------
Moving stuff around
-------------------

The moving, merging and splitting of fonts. The first example moves selected glyphs in the same font and renames them. Note that if you remove the line :py:func:`f.removeGlyph(g.name)` the same script effectively copies the glyphs. Also new in this script: it iterates through the whole font and checks for each glyph if the ``g.selected`` attribute is ``1`` or ``0``. If it is ``0``, the glyph is not selected in the font window. If it is ``1``, is is selected. It then proceeds to create a new glyph name, and calls ``f.insertGlyph()`` method which takes a glyph as parameter. The optional parameter as is to be able to insert the glyph under a different name. If you don't pass a parameter for as, the font will insert the glyph under its own name. The glyph can come from the same font, or a different font, or be an orphan glyph.

>>> # rename the selected glyphs
>>> # in the current font to <glyphname>.sc
>>>  
>>> from robofab.world import CurrentFont
>>> f = CurrentFont()
>>>  
>>> for g in f:
>>>     if g.selected == 0:
>>>         continue
>>>     newName = g.name+".sc"
>>>     print "moving", g.name, "to", newName
>>>     # note: as of robofab svn version 200, the "as" argument in insertGlyph has changed to "name"
>>>     f.insertGlyph(g, name=newName)
>>>     f.removeGlyph(g.name)
>>>     f.update()
moving A to A.sc
moving C to C.sc
moving B to B.sc

------------------------
Generating font binaries
------------------------

::
    # robothon 2006
    # batch generate
    from robofab.world import AllFonts
    for font in AllFonts():
        font.generate('otfcff')

This will generate CFF flavored OpenType fonts for all open files.::

    # robothon 2006
    # a more robust batch generator that only has one font open at the time.
    
    from robofab.interface.all.dialogs import GetFolder
    from robofab.world import RFont, OpenFont
    import os
     
    def collectSources(root):
        files = []
        ext = ['.vfb']
        names = os.listdir(root)
        for n in names:
            if os.path.splitext(n)[1] in ext:
                files.append(os.path.join(root, n))
        return files
     
    # A little function for making folders. we'll need it later.
    def makeFolder(path):
        # if the path doesn't exist, make it!
        if not os.path.exists(path):
            os.makedirs(path)
     
    def makeDestination(root):
        macPath = os.path.join(root, 'FabFonts', 'ForMac')
        makeFolder(macPath)
        return macPath
     
    def generateOne(f, dstDir):
        print "generating %s"%f.info.fullName
        f.generate('otfcff',  dstDir)
    
    f = GetFolder()
    
    if f is not None:
        paths = collectSources(f)
        dstDir = makeDestination(f)
        for f in paths:
            font = None
            print f
            try:
                font = OpenFont(f)
                generateOne(font, dstDir)
            finally:
                if font is not None:
                    font.close(False)
        print 'done'

The script above generates fonts too, but is a bit more robust. FontLab sometimes crashes when it has to generate a long list of fonts and they're all open at the same time. This script asks you for a folder of ``.vfb`` sources (which in itself can be a useful ingredient for your own scripts). Then it will open them one by one and generate the fonts in the flavor indicated in the line ``f.generate('mactype1', dstDir)``. A list of types and their names can be found in the robofab documentation how-to page on generating fonts. This script also creates a new folder to store the generated fonts in, sorted by type.

-------
Merging
-------

Here's an script, quite complex, for combining two fonts into one. Maybe not for the newbie, but if you're into it try to figure out how it works. It uses a couple of new concepts, like ``Sets`` and ``DigestPens``. If it is too complicated: don't worry.

>>> # robothon 2006
>>> # merge two fonts
>>>  
>>> from robofab.world import SelectFont, NewFont
>>> from robofab.pens.digestPen import DigestPointPen
>>> from sets import Set
>>>  
>>> font1 = SelectFont("Select base font")
>>> font2 = SelectFont("Select alternate font")
>>>  
>>> font1Names = Set(font1.keys())
>>> font2Names = Set(font2.keys())
>>>  
>>> commonNames = font1Names & font2Names
>>> uncommonNames = font2Names - font1Names
>>>  
>>> for glyphName in commonNames:
>>>     glyph1 = font1[glyphName]
>>>     pointPen = DigestPointPen()
>>>     glyph1.drawPoints(pointPen)
>>>     digest1 = pointPen.getDigest()
>>>     
>>>     glyph2 = font2[glyphName]
>>>     pointPen = DigestPointPen()
>>>     glyph2.drawPoints(pointPen)
>>>     digest2 = pointPen.getDigest()
>>>     
>>>     if digest1 != digest2:
>>>         print '> alt >', glyphName
>>>         # note: as of robofab svn version 200, the "as" argument in insertGlyph has changed to "name"
>>>         glyph3 = font1.insertGlyph(glyph2, name=glyphName+'.alt')
>>>         glyph3.mark = 1
>>>         glyph3.update()
>>>  
>>> for glyphName in uncommonNames:
>>>     print '>', glyphName
>>>     glyph = font1.insertGlyph(font2[glyphName])
>>>     glyph.mark = 60
>>>     glyph.update()
>>>     
>>> font1.update()

--------------------------------
Dealing with Robofab limitations
--------------------------------

A handful of FontLab's own glyph and font methods are not supported in RoboFab. The reasons for this vary, some of them are very FontLab specific (for instance ``fl.productnumber`` or ``fl.username``), but most of the missing stuff was just not needed very often — the following examples show how to get access to all functionality and attributes in the FontLab layer.

-------------
FontLab layer
-------------

To get to the FontLab layer, Robofab's Font and Glyph objects have a ``naked()`` method which returns the FontLab object. Note that you can still use the Robofab functionality like :py:func:`CurrentFont`, :py:func:`CurrentGlyph`, pens etc. The FontLab layer is documented here_. Maybe you remember the ``naked()`` method from the cookie cutter example.

>>> # show the objects from the fontlab layer
>>> from robofab.world import CurrentFont
>>> f = CurrentFont()
>>> print f.naked()
>>> g =  f["A"]
>>> print g.naked()
<Font: 'MyFont'>
<Glyph: 'A', 0 nodes, parent: 'MyFont'>

Other things you need to dig deeper for. Note that some of these objects appear to be broken.

^^^^^^^^^^^^^^^^
PostScript hints
^^^^^^^^^^^^^^^^

The vertical and horizontal hint zones as well as blue values can be read and set.

>>> # show vhints for current glyph
>>> g = CurrentGlyph()
>>> g.naked().vhints
[<VHint: p=25, w=163, parent: "a">,<VHint: p=42, w=146, parent: "a">]

^^^^^^^^^^^^^^^
All name fields
^^^^^^^^^^^^^^^

The FontLab table of OpenType names, the naming record, is available. See also the the FontLab reference for ``NameRecord``.

>>> # robothon06
>>> # show OpenType naming records
>>> # in the fontlab API
>>> from robofab.world import CurrentFont
>>> f = CurrentFont()
>>> fn = f.naked()
>>> for r in fn.fontnames:
>>>     print r.nid, r.pid, r.eid, r.lid, r.name
256 1 0 0 Bold
256 3 1 1033 Bold

^^^^^^^^^
Encodings
^^^^^^^^^

The FontLab Encoding object. See also the the FontLab reference for ``Encoding``.

>>> # robothon06
>>> # show encoding 
>>> from robofab.world import CurrentFont
>>> f = CurrentFont()
>>> fn = f.naked()
>>> # object containing encoding records
>>> # you can iterate through it by using
>>> # an index.
>>> print fn.encoding
>>> for i in range(len(fn.encoding)):
>>>     er = fn.encoding[i]
>>>     print er, er.name, er.unicode
<Encoding: parent: "MyDemoRegular">
...
<EncodingRecord: "eacute", unicode: 233> eacute 233
<EncodingRecord: "ecircumflex", unicode: 234> ecircumflex 234
<EncodingRecord: "edieresis", unicode: 235> edieresis 235
<EncodingRecord: "igrave", unicode: 236> igrave 236
<EncodingRecord: "iacute", unicode: 237> iacute 237
<EncodingRecord: "icircumflex", unicode: 238> icircumflex 238
..etc..
