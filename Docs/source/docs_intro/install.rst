==================
Installation notes
==================

- March 1, 2009. Implements full support of the UFO2 specification.
- November 18, 2007. License changed to `The BSD License`_.
- May 30, 2007, updated some points.
- v1.1.1 release September 9 2005
- v1.1 release February 7 2005
- v1.0b1 release October 6 2003
- September 14, 2003
- September 1, 2003
- July 27, 2003

.. _The BSD License: http://www.opensource.org/licenses/bsd-license.php

.. note:: from November 2007 on, the 1.1.1 version is now distributed with `The BSD License`_. The license information in the current 1.1.1 package still needs to be updated.

-------------
Which Python?
-------------

RoboFab works with any Python 2.2.1 and up.

^^^^^^^^^^^^^^^^^^^^^^^^^
Which Python for FontLab?
^^^^^^^^^^^^^^^^^^^^^^^^^

If you're using RoboFab in conjunction with FontLab, there are some restrictions imposed by FontLab's taste in Python. If you are using FontLab Studio in Mac OS X, you already have the necessary Python. If you are using anything previous to FontLab Studio on a Mac, you will need to install MacPython-OS9 2.3. FontLab on Windows requires at least Python 2.2.1.

------------------------------------
Installing on Mac OSX for FontLab, 1
------------------------------------

If you're on OSX Tiger (10.4) or Leopard (10.5), and you want to install RoboFab and its dependencies (FontTools, Numeric), for use in FontLab 5.0x, then you can use the :doc:`RoboFab Installer for OSX, FontLab 5.0x <download>`. This should work for most current users on OSX.

------------------------------------
Installing on Mac OSX for FontLab, 2
------------------------------------

If the all-in-one installer doesn't do it for you (for instance, you want to use RoboFab outside the context of FontLab) the following instructions show you the individual steps to install RoboFab. Currently Python,org already offers version 2.5. However, on MacOSX FontLab **will only work with the OS installed Python 2.3**. So there's not really much point in installing a newer Python if you don't know what you're doing.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
How do I install Robofab for use with FS5 on mac?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The easiest way is to do the following:

1. Download RoboFab and put it wherever you want it to live on your hard drive. Many people make a RoboFab folder in ``/Applications``.

2. Go to your ``Applications/Utilities`` folder.

3. Open Terminal.

4. Once the terminal is open, type ``python`` with a space after it.

5. Drag the ``install.py`` script from the RoboFab folder into the line that you just typed in the terminal. It should now look something like this (with your name, rather than ``Tinkywinky``)::

    python /Users/Tinkywinky/RoboFab_1/install.py

.. note::

    If you have installed newer (2.3+) versions of Python, you need to explicitly tell with which version of Python you want to install. The command would look like this::

        python2.3 /Users/Tinkywinky/RoboFab_1/install.py

6. Hit the return key and the following should be printed in the terminal::

    Installing RoboFab: about to write a path to '/Users/Tinkywinky/RoboFab_1/
    Lib' in '/System/Library/Frameworks/Python.framework/Versions/2.3/lib/
    python2.3/site-packages/robofab.pth'...
    Robofab is now installed.
    (Note that you have to run the install script again if you move your RoboFab folder)

7. Restart FontLab if you had it open during this process.

This will install RoboFab for the system Python, which is what FontLab Studio uses.

----------------
About install.py
----------------

In the package, on the same level as this read me there's a ``install.py`` script. Running this script creates a file named ``robofab.pth`` in site-packages. This ``robofab.pth`` file contains the path to the current location of the RoboFab package. It does not copy the RoboFab package to ``site-packages`` itself, you need to keep the RoboFab package. Also: if you *move* the RoboFab folder to some other location (or rename any of the directories the RoboFab folder is nested in), you have to run the ``install.py`` script again to update the path.

- `Download Python <http://python.org/download>`_
- `MacOS Python download page <http://homepages.cwi.nl/~jack/macpython/download.html>`_

------------
Dependencies
------------

Some parts of RoboFab depend on other Python modules and packages. These need to be installed as well.

**FontTools.**
    Robofab requires Just van Rossum's FontTools package (not to be confused with Apple Inc's set of tools for fonts with the same name). It is recommended that you use the RoboFab installer with FontTools built in, available at :doc:`the download section <download>`. If you must pick up FontTools separately, download the latest snapshot at `fonttools.sf.net`_.

**The Numeric Python module.**
    The version of Numeric for FontTools is available here: `Numeric 24.2`_.

.. _fonttools.sf.net: http://fonttools.sf.net/
.. _Numeric 24.2: http://www.robofab.org/download/Numeric-24.2.zip

-------------------------------------
RoboFab bundled with FontLab Studio 5
-------------------------------------

FontLab Inc. has been granted permission to bundle RoboFab with FontLab-the-application. They have not done so. The reason is not clear.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Installing on Mac OSX MacPython "OS9" 2.3, for FontLab
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

FontLab 4.6 on Mac OSX has to work with MacPython "OS9" 2.3 (available from `MacPython`_). FontLab **4.6** does not work with the Framework version of Python. In Application/MacPython-OS9 2.3 find the **PythonInterpreter**. Then go to the directory where you downloaded RoboFab. Drag install.py on top of PythonInterpreter to run it. If it says 'RoboFab is installed' you're done. Since FontLab uses this version of Python, this procedure also installs RoboFab for use inside FontLab.

.. _MacPython: http://homepages.cwi.nl/~jack/macpython/macpython-older.html

RoboFab has two folders of demo scripts and utilities which can be used in FontLab. Copy the contents of the **Scripts** folder to the ``FontLab/Macros`` folder to make them available to FontLab.

^^^^^^^^^^^
Permissions
^^^^^^^^^^^

Make sure you have admin permissions on the machine when you install the various packages. When installing as a normal priviliged user, it can sometimes happen that certain files can't be written, and the installation remains incomplete. The most common problem is that one or two preference files need to be written, but the current user does not have enough permissions to delete them. Read the traceback, locate the file, delete, install again.

---------------------
Installing on Windows
---------------------

Installing RoboFab on windows should be pretty straightforward. RoboFab is backwards compatible to Python 2.2.1, but not 2.2. RoboFab now includes a Python 2.2 compatible version of ``sets.py``.

.. note::

    FontLab 4.54 (and higher) offer some basic file dialogs which RoboFab 1.1.1 uses. If you want to use file dialogs on Windows in an older (pre- 4.54) version of FontLab, or you want to use file dialogs on Windows, outside of FontLab (NoneLab), then you need to install the free ``win32`` module, which might have dependencies of its own.

    The ``win32`` module is available for download `here`_. This module is needed for some simple dialogs and messages. We might actually move to another module for these services in the future.

    Tested in Windows XP Home Edition. If there are special requests or procedures we've forgotten to mention, please let us know.

.. _here : http://starship.python.net/crew/mhammond/win32/Downloads.html

-----------------------------
Installing on other platforms
-----------------------------

Place the robofab directory in a place where you can leave it for a while. Not on the desktop or a temporary download folder. Run ``install.py`` in a Python interpreter.

---------------
Initial testing
---------------

Open a Python interactive interpreter window.::

    import robofab
    # notice, all lowercase!

If you don't get an traceback, you're good to go.

In ``Scripts/RoboFabIntro/`` there are some test scripts, simple examples and some utilities. Read the source to learn more about what the examples do and where they want to run.

--------------------
Detailed unittesting
--------------------

Robofab has unittesting to make sure all parts function properly. If you don't know what unittesting is, don't sweat it. If you're interested, go to ``robofab/test/runAll.py``.
