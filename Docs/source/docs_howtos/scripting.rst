=========
Scripting
=========

Scripting with RoboFab is programming in Python. Everything is possible, it's just that some things are easier than others.

------------------
For Python Newbies
------------------

If you don't have much programming experience, or you're not familiar with Python, have a look at Just van Rossum's Drawbot_ (if you're on OSX that is). Drawbot is a low threshold app to play with python code and get awarded with nice eye candy. Learn the princples of programming, loops, variables, by building with graphic shapes, paths, colors.

.. _Drawbot : http://drawbot.com/

RoboFab uses objects to address the various things you find in a font. Objects are a useful way to think about code. A font is an **object**. It has some **attributes**, values that belong to that object. A font object is also capable of doing stuff by calling its **methods**. None of this is specific to RoboFab, a lot of programming languages use objects, and Python does as well. Objects can contain other objects. Have a look at the :doc:`RoboFab object model <../docs_objects/model>` to see how they are structured and what other objects there are besides Font.

^^^^^^^^^^^^^^^
Other resources
^^^^^^^^^^^^^^^

This is an interesting introduction into programming with Python as well: `How to think like a computer scientist`_. A full introduction into programming goes beyond the scope of this manual. Then there are tons of books, websites, stuff. Do some googling.

.. _How to think like a computer scientist : http://openbookproject.net/thinkcs/python/english2e/

--------------------
For RoboFog Converts
--------------------

For those of you joining us from the cohorts of RoboFog users, here some some of the main points of difference. Maybe others will find this part interesting too.

^^^^^^^^^^^^^^^^^^^^
Packages and modules
^^^^^^^^^^^^^^^^^^^^

Robofab is set up with packages. This is to organise the large volume of code into smaller, easier to manage modules. RoboFab does not have any builtins anymore, so you have to import the stuff you want to work with. Look at :doc:`the use of the world module <world>` which is where a lot of stuff is made available for you.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
CurrentFont(), CurrentGlyph()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We've kept the ``CurrentFont`` function to provide a font object for the front most font. And we've renamed ``CurrentChar`` into ``CurrentGlyph`` as RoboFab is fully unicode aware and we're dealing with glyphs, not characters. ``CurrentGlyph()`` returns a glyph object for the front most glyph.

^^^^^^^^^^^^^^^^^
Segments, bPoints
^^^^^^^^^^^^^^^^^

Fonts store :doc:`glyphs <../docs_objects/RGlyph>`, glyphs store :doc:`contours <../docs_objects/RContour>`, just like RoboFog. Contours however have a few more tricks than their RoboFog counterparts. Contours have :doc:`segments <../docs_objects/RSegment>`, a kind of cluster of a series of offcurve points and one on curve point (see :doc:`Understanding contours <understanding_contours>`). Contours also have lists of :doc:`points <../docs_objects/RPoint>` and :doc:`bpoints <../docs_objects/bPoint>`. Depending on what you need to do you can iterate through the segments or points or bpoints.

^^^^^^^^^^^^^^^^^^^
Conversion, drawing
^^^^^^^^^^^^^^^^^^^

For scripts which convert or transform outline data in some way, consider writing a :doc:`Pen <usepen>` object for that conversion. These are also handy for drawing in glyphs.

--------------
Where to start
--------------

You've seen that a lot of the examples in this manual start by importing some objects or functions from ``robofab.world``. This is an easy way to get to a font, and through the font you can get access to the glyphs and all other values that are associated with them.

^^^^^^^^^^^^^^^^^^^^^^^^^
Open a font from any file
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code::

    >>> from robofab.world import OpenFont
    >>> f = OpenFont()
    >>> # hey look! an open font dialog!
    >>> print f
    None # or a font object, depending on what you select

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Open a font from a specific file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code::

    >>> from robofab.world import OpenFont
    >>> path = "MyDrive/Folder1/Work/somefile"
    >>> f = OpenFont(path)
    >>> # hey look! it opens the file without asking..
    >>> print f
    # a font object

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Do something with the font that's open
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code::

    >>> # in Fontlab:
    >>> from robofab.world import CurrentFont
    >>> f = CurrentFont()
    >>> print f
    # a font object for the font that's on top.

---------------
How to proceed?
---------------

Programming is for a large part the art of picking one seemingly single problem apart and make a lot of smaller, solveable problems from it. Some random thoughts on the subject:

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
First think about where to start:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Does your problem have something to do with the entire font?
- Or the metrics? The widths? Sidebearings? Kerning?
- Or one single glyph? Or perhaps a group of glyph while excluding others?
- Do you need to move stuff around?
- Do you need to create new glyphs?

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Can you describe each step of the process
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- RoboFab can't be instructed to make judgements on aesthetics.
- You have to formulate small steps, first do this, then compare that.
- Use approaches and tricks you learned before to get ahead.
- Start with the simplest possible loop and test.
- Play around -- pick and object and try to make it do tricks. Use this documentation to see what methods and attributes each one has.

^^^^^^^^^^
Be patient
^^^^^^^^^^

- Programming and scripting is a skill just like any other.
- Eventhough some folks pick it up faster, anyone clever enough to understand typedesign can learn scripting.
- Read the documentation, try the examples, try the demos. Are there scripts that do something like what you want to do? Pick them apart, see how they work. Learn from the source.
- If you think that scripting is nothing like design consider this: it's certainly a nicer intellectual challenge to try to write some code, then it is to manually do repetitive, stupid production things for hours or days on end. Make the computers work for you, instead of the other way round. Scripting is control.
