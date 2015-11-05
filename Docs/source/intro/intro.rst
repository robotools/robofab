RoboFab Intro
=============

RoboFab is a **library** of Python code for manipulation and storage of font and glyph related data. RoboFab implements a new font file format, the :doc:`Unified Font Objects <ufo>` or .ufo for short. UFO is a format for **font sources** (similar to something like .fog or .vfb) except that UFO is XML based (see :ref:`Glyph Interchange Format <glif>`), readable, well documented and easily extended to contain different kinds of data.

Long term sources
-----------------

Traditionally, font editors have their own file formats to store the work in progress. Generated fonts are optimised for size and speed and they have no extra room to store all the additional information one needs during the design of a font (for instance background layers, notes, information for other font formats). When a company stops working on their application (it happens), the binary source files become a burden. Not immediately, but soon enough as system updates make the last version of the program impossible to run. When that happens, all the binary source files are impossible to read. The formats are not or badly documented. They've locked themselves and your work is gone. Type design is a long term endeavour and it makes sense to store font source material in a long term format. UFO is our idea of how such a format should look like: XML based, object oriented and flexible. Text is just so much easier to handle.

Unified Font Objects
^^^^^^^^^^^^^^^^^^^^

RoboFab reads and writes UFO, but it also provides a range of Python objects to work with these Unified Font Objects. We have implemented the UFO objects for use in FontLab (based on top of FontLab's own objects) and another one which implements the UFO objects for use in a plain-Python environment, NoneLab. That means you can access and manipulate font and glyph data in Python without running a font editor (but it has some other drawbacks). It's possible to write scripts with RoboFab that work the same in FontLab as they do in a plain Python environment. Unified Font Objects can store quadratic and bezier splines.

RoboFab environments
--------------------

Parts of RoboFab can be used in FontLab, other parts work outside FontLab, in normal Python interpreters. Some parts work in both. This is a powerful feature of RoboFab, but it can sometimes be a bit confusing. Have a look at :doc:`the world module <../howtos/world>` for some help in making scripts that work everywhere.

RoboFab in plain Python
^^^^^^^^^^^^^^^^^^^^^^^

After RoboFab is installed you can write plain non-FontLab Python scripts that open, manipulate and save .ufo files. Through the RoboFab :doc:`objects <../objects/objects>` you have access to all data in the font: names, glyphs, contours, widths, kerning, the lot. Use the :doc:`objects overview <../objects/objects>` or the :doc:`objects map <../objects/model>` to get an idea of what these things can do. Plain Python can be a Python IDE, or a python command line interpreter. RoboFab runs on any Python 2.2.1+ installation, Linux, Unix, Mac OSX, MacOS9, Windows. `Python ports to lots of platforms`_ and so does RoboFab.

.. _Python ports to lots of platforms: http://python.org/download/

RoboFab in FontLab's Python
^^^^^^^^^^^^^^^^^^^^^^^^^^^

RoboFab can also run in FontLab and transparently implements the RoboFab object structure on top of the FontLab objects. That means that with RoboFab installed you can talk to FontLab fonts using the same methods and attributes as you use to write scripts for UFO fonts. The RoboFab objects in FontLab can manipulate the font data you see in the FontLab windows. Some RoboFab objects in FontLab have extra attributes and methods to deal with FontLab specific functionality. For example font generation, guides and access to the underlying FontLab objects.

RoboFab and UFO
^^^^^^^^^^^^^^^

RoboFab Font objects can export and import the UFO format. So you can write scripts in FontLab that export data to UFO, and other scripts that edit these UFO's, and then later import the UFO back into FontLab.

What RoboFab is not..
---------------------

Not entirely RoboFog MkII
^^^^^^^^^^^^^^^^^^^^^^^^^

RoboFab is not a port of **RoboFog** to OSX, nor is it a complete font editor with interfaces, font and glyph windows etc. It is a toolkit that you can use to build your tools with. You can start by using RoboFab to make scripting in FontLab easier. But you can also use RoboFab to build elaborate tools (for instance **MetricsMachine**) that read and write UFO fonts and work on the data. Other RoboFab based tools are under construction.

Not entirely RoboFog Compatible
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We've poured all our experience from writing RoboFog into the RoboFab objects. You will recognise a lot. But the font world has grown a lot more complex since Fontographer 3.5 so RoboFab objects need to deal with a lot more than their RoboFog ancestors. Your RoboFog scripts won't work with RoboFab, sorry. But they're structured quite similarly and you won't have much trouble adapting. We thought about building objects with the RoboFab API for RoboFog, but their functionality depends too much on features that were introduced after Python 1.5.2. It would be too complex. But we've provided an alternative: export scripts for RoboFog to UFO format, so that you can write UFOs for all your RoboFog sources and use them in the new UFO tools.

Where next?
-----------

First you could :doc:`download` the library and install it. Then you could browse through this documentation and see what the various :doc:`objects <../objects/index>` are, what they can do etc. You could have a look at :doc:`a discussion on scripting <../howtos/scripting>`.
