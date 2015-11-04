==============
FontLab Remote
==============

A neat feature in RoboFab for FontLab on MacOS. RoboFab can install an AppleEvent handler in FontLab to make FontLab respond to calls from other applications. There is code to communicate with FontLab using this AppleEvent and to make it execute code and exchange data such as glyphs. How useful this remote stuff is depends on what you want to do with it. We thought it was cool. The 'remote' relates to one application controlling another. Both applications need to run on the same machine, it does not mean that FontLab is accepting commands over a network for instance. For that we need another tool.

----
How?
----

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Step 1: Start the remote stuff in FontLab
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The first thing you need to do is start the AppleEvent support in FontLab. That's done by importing the remote module:

.. showcode:: ../../Examples/howtos/fontlabRemote_00.py

.. code::

    FontLabRemote is on.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Step 2: Start the Python IDE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can now send commands, bits of code and entire glyphs to FontLab from the Python IDE:

.. showcode:: ../../Examples/howtos/fontlabRemote_01.py

.. code::

    2

The function ``runFontLabRemote()`` sends a piece of Python code to FontLab's python interpreter and has it executed. In this example the code is ``print 1+1``. The result, the output of FontLab running this piece of code is then returned to the Python IDE. Note that the output is always a string. Depending on the code you throw at FontLab it could even contain tracebacks or other output.

When FontLab receives and executes a remote command, it will print a note to the FontLab Output window::

    < executing remote command >
    < executing remote command >
    < executing remote command >

That means that FontLab is doing remote stuff.

^^^^^^^^^^^^^^^^^^^^^^^^^^^
Step 3: Teleporting a Glyph
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The remote module has support to send and receive Glyphs. For the next example open a new font in FontLab first (command N), then run the following code in the Python IDE. Make sure you have a UFO font handy somewhere:

.. showcode:: ../../Examples/howtos/fontlabRemote_02.py

If all went well, you now have the ``n`` from your UFO copied to the right slot in your FontLab font. As noted earlier, if all you want to do is import some glyphs from a UFO into FontLab there is absolutely no need to use all this remote stuff.

----
Why?
----

The remote module only takes care of the communication with FontLab. Possible applications which could be built on top of this are:

- Use FontLab to perform outline operations such as remove overlap.
- Use FontLab to batch process font generation.
- Build an external editor to augment the functionality of FontLab.

As noted before, the remote stuff only works on MacOS.

^^^^^^^
Example
^^^^^^^

Example in which a glyph from a UFO opened in plain Python is copied to FontLab. After removing overlap the glyph is returned and inserted in the UFO:

.. showcode:: ../../Examples/howtos/fontlabRemote_03.py

Possible results::

    Number of contours before: 6
    Number of contours after:  4

.. note::

    While experimenting with ``robofab.tools.remote`` we found that after some time it's possible that FontLab grows weary of the remote fussing and the scripts stop working. Restarting FontLab usually solves that situation.
