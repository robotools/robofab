Installation notes
==================

Installing RoboFab on Mac OSX
-----------------------------

1. Download RoboFab and put it wherever you want it to live on your hard drive. Many people make a RoboFab folder in ``/Applications``.

2. Go to your ``Applications/Utilities`` folder.

3. Open Terminal.

4. Once the terminal is open, type ``python`` with a space after it.

5. Drag the ``install.py`` script from the RoboFab folder into the line that you just typed in the terminal. It should now look something like this (with your name, rather than ``Tinkywinky``)::

    python /Users/Tinkywinky/RoboFab/install.py

.. note::

    If you have different versions of Python in your system, you need to explicitly tell with which version of Python you want to install. The command would look like this::

        python2.6 /Users/Tinkywinky/RoboFab/install.py

6. Hit the return key and the following should be printed in the terminal::

    Installing RoboFab: about to write a path to '/Users/Tinkywinky/RoboFab/
    Lib' in '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/
    python2.7/site-packages/robofab.pth'...
    Robofab is now installed.
    (Note that you have to run the install script again if you move your RoboFab folder)

7. Restart FontLab if you had it open during this process.

This will install RoboFab for the system Python, which is what FontLab Studio uses.

Permissions
-----------

Make sure you have admin permissions on the machine when you install the various packages. When installing as a normal priviliged user, it can sometimes happen that certain files can't be written, and the installation remains incomplete. The most common problem is that one or two preference files need to be written, but the current user does not have enough permissions to delete them. Read the traceback, locate the file, delete, install again.

About install.py
----------------

In the package, on the same level as this read me there's a ``install.py`` script. Running this script creates a file named ``robofab.pth`` in site-packages. This ``robofab.pth`` file contains the path to the current location of the RoboFab package. It does not copy the RoboFab package to ``site-packages`` itself, you need to keep the RoboFab package. Also: if you *move* the RoboFab folder to some other location (or rename any of the directories the RoboFab folder is nested in), you have to run the ``install.py`` script again to update the path.

Dependencies
------------

Some parts of RoboFab depend on other Python modules and packages. These need to be installed as well.

**FontTools**
    Robofab requires Just van Rossum's FontTools package (not to be confused with Apple Inc's set of tools for fonts with the same name). Download the latest snapshot of FontTools at `fonttools.sf.net`_.

**dialogKit**
    Some FontLab scripts in RoboFab require Tal Leming's dialogKit UI package. Download the latest version of dialogKit at `github.com/typesupply/dialogKit`_.

.. _fonttools.sf.net: http://fonttools.sf.net/
.. _github.com/typesupply/dialogKit: http://github.com/typesupply/dialogKit

RoboFab bundled with FontLab Studio 5
-------------------------------------

FontLab Inc. has been granted permission to bundle RoboFab with FontLab-the-application. They have not done so. The reason is not clear.

Installing FontLab scripts
--------------------------

RoboFab has two folders of demo scripts and utilities which can be used in FontLab. Copy the contents of the **Scripts** folder to the ``FontLab/Macros`` folder to make them available to FontLab.

Installing on Windows
---------------------

Installing RoboFab on windows should be pretty straightforward. RoboFab is backwards compatible to Python 2.2.1, but not 2.2. RoboFab now includes a Python 2.2 compatible version of ``sets.py``.

Installing on other platforms
-----------------------------

Place the robofab directory in a place where you can leave it for a while. Not on the desktop or a temporary download folder. Run ``install.py`` in a Python interpreter.

Initial testing
---------------

Open a Python interactive interpreter window.::

    import robofab
    # notice, all lowercase!

If you don't get an traceback, you're good to go.

In ``Scripts/RoboFabIntro/`` there are some test scripts, simple examples and some utilities. Read the source to learn more about what the examples do and where they want to run.

Detailed unittesting
--------------------

Robofab has unittesting to make sure all parts function properly. If you don't know what unittesting is, don't sweat it. If you're interested, go to ``robofab/test/runAll.py``.
