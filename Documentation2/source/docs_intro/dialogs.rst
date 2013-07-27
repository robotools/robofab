-------
Dialogs
-------

Sometimes you need simple dialogs to get scripts to talk to the user. As RoboFab can run in many different environments, this dialog module tries to offer consistent functionality in all worlds. Most of the dialogs work in FontLab Mac/Win and Python IDE Mac. Some dialogs also work in Windows. This module offers the right kind of dialog for the environment you call them in. A bit like ``robofab.world`` helps you out by finding the right objects.

Availability:

- FontLab means that the dialogs are available in FontLab on either platform.
- Mac means that the dialogs are available in plain Python for OS9 as well as OSX.
- Windows means the dialogs are available in plain Python in Windows.

.. py:function:: Message(message, title='RoboFab')

A simple message dialog with just one OK button. It does not return any values.::

    from robofab.interface.all.dialogs import Message
    Message("A Message From RoboFab")

Available on FontLab, Macintosh.

.. py:function:: AskString(prompt, value='', title='RoboFab')

Asks for a string and return it. Returns ``None`` if the user cancelled.

>>> from robofab.interface.all.dialogs import AskString
>>> print AskString("Text for preview?")
"hello"

Available on FontLab, Macintosh.

.. py:function:: AskYesNoCancel(prompt, title='RoboFab', default=0)

Returns ``1`` for 'Yes', ``0`` for 'No' and ``-1`` for 'Cancel'. ``default`` argument only available on Macintosh.)

>>> from robofab.interface.all.dialogs import AskYesNoCancel
>>> print AskYesNoCancel("Do you really want to continue?", 
>>>       title='RoboFab', default=0)
-1

Available on FontLab, Macintosh

.. py:function:: GetFile(message=None)

A standard select file dialog. Returns path if one is selected. Otherwise it returns None.

>>> from robofab.interface.all.dialogs import GetFile
>>> print GetFile("Open Master")
path/folder/something

Available on FontLab, Macintosh, PC.

.. py:function:: GetFolder(message=None)

A standard select folder dialog. Returns path if one is selected. Otherwise it returns None.

>>> from robofab.interface.all.dialogs import GetFolder
>>> print GetFolder("Pick a directory...")
path/folder/something

Available on FontLab, Macintosh, PC.

.. py:function:: PutFile(message=None, defaultName=None)

Save file dialog. Returns path if one is entered. Otherwise it returns ``None``.

>>> from robofab.interface.all.dialogs import PutFile
>>> print PutFile("Save this file as..")
path/folder/something

Available on FontLab, Macintosh, PC.

.. py:function:: SelectFont(message="Select a font:", title='RoboFab')

Returns font instance if there is one, otherwise it returns ``None``.

>>> from robofab.interface.all.dialogs import SelectFont
>>> print SelectFont("Select a font:")
< the font you selected >

Available on FontLab.

.. py:function:: SelectGlyph(font, message="Select a glyph:", title='RoboFab')

Returns glyph instance from font if a glyph is selected. Otherwise it returns ``None``.

>>> from robofab.world import CurrentFont
>>> from robofab.interface.all.dialogs import SelectGlyph
>>> f = CurrentFont()
>>> if f is not None:
>>>     print SelectGlyph(f, "select a glyph")
< the glyph you selected >

Available on FontLab.

.. py:function:: FindGlyph(aFont, message="Search for a glyph:", title='RoboFab')

The ``FindGlyph`` dialog offers a list of the glyphs present in a font. A name or partial name can be types to navigate to the wanted glyph quickly.

>>> from robofab.world import CurrentFont
>>> from robofab.interface.all.dialogs import FindGlyph
>>> f = CurrentFont()
>>> if f is not None:
>>>     print FindGlyph(f, "select a glyph")
< the glyph you selected >

Available on FontLab.

.. py:function:: GetFolder(message=None)

Select folder dialog. Returns the selected path if one is picked. Otherwise it returns ``None``.

Available on FontLab, Macintosh, PC.
