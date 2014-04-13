=================================
Python, RoboFab, FontLab, Editors
=================================

----------
Scripting?
----------

These talks are about scripting. The term **scripting** is loosely defined as "writing small programs" without making it sound as difficult or complicated as "programming". Scripting is programming of course, but you don't have to tell anyone. You're using a programming language, **Python**, to write a script (or whatever you want to call it), which is then acted out by the **Python interpreter**. This is a program which will try to follow your instructions, giving feedback when it runs into problems or finishing the job when it doesn't. Running into problems is not something to be afraid of, Python does it very politely with a **traceback**, Python's way of reporting what went wrong and roughly where it the code it happened. We'll see a lot of these and we'll learn how to read these reports and understand what went wrong.

----
Why?
----

Scripting is not type design. Or perhaps better: scripting is everything but typedesign. Scripts won't help you find ideas or draw a better curve. But it might help you make simple tools for things you need to do often. Just like anything, it will get better with some experience, but even a badly written, simple script can save you lots of time. You don't have to be (or become) a professional programmer to make it a useful skill.

-----
Where
-----

Python is a modern, open source, programming language which is relatively easy to work with. There are Pythons for all operating systems and it has many developers building many different tools for it. It is not just for fonts and glyphs, there are networking and scientific tools, games, web applications. Years ago **RoboFog** introduced Python to make tools for typedesign and the idea stuck. Now there is a range of type applications that use Python: FontLab, the Adobe FDK, MetricsMachine, RoboFab. Learning Python means you can use your skills in more than one application.

There are several places where you can write your code. Each with their own purpose and use. We'll look at some of them:

- **FontLab's Macro panel**: a simple code editor in FontLab where you can edit and run scripts. The advantage is that you're in FontLab and can start work immediately, manipulating fonts and glyphs which are open. But the panel is lacking features which are useful when writing a lot of code, which is why FontLab includes the:

- **FontLab with "external editor"**: in the FontLab preferences panel you can select another application as your python editor of choice. So when you hit the Macros button, this editor will pop up. This requires that your script is saved in a file somewhere on disk. You can use the editor to write the code, but FontLab will still run the program. FontLab doesn't actually execute the Python code, but uses a system installed interpreter.

- **Python IDE, Win, Mac OSX**: There are several IDE ("Integrated Development Environment") programs for Python on Mac and Windows. This means basically a Python code editor which can also run your code. Some of them offer debugging tools, module browsers or even complete interface toolkits. These IDE's are general programming tools and don't know much about type specific things. More and more code editors offer Python execution, for instance in **BBEdit** and **Textmate** on OSX you can edit your code, hit a cmd key and have the code run in the OSX Python interpreter. This is similar to the FontLab-with-external-editor option.

- **Command-line Python interpreter**: a form of Python where you write a line of code at a prompt and it is immediately executed. Useful to test simple problems, but not for anything over a couple of lines of code.

- **Command-line python**: use the installed command-line Python interpreter to execute files. The interpreter is called with the filename as an argument.

  >>> python myCode.py
  ..does stuff..

-------
Objects
-------

Perhaps the most useful invention in programming since the paper-punch card is called **object oriented programming**. The term is used to describe a way of programming in which the data you're working on, and the code which belongs to that data are kept together, much like a person holding a handful of balloons on strings, in a single **object**, the cluster of balloons. This may sound a bit abstract. But it's a way to keep all the code and data sorted in a useful way. Otherwise there will be too much stuff very quickly. More terminology:

- **attributes**: the things an object knows about, its data or value. An object's data is stored in its attributes.

- **methods**: the things an object can do. The code to manipulate an object, its functions.

Risking an example: an object of the class **car** has an attribute **color** (blue) and a method **drive** (slow). Big objects are usually split up into smaller, more specific objects. For instance, a **Font** object offers access to **Glyph** objects. The way the various objects relate, wich object contains what etc. — the way something is abstracted — is called an **object model**. A map of the object model used in RoboFab is in :doc:`the Fab docs <../docs_objects/model>`. An object model is also called **API** for Application Programming Interface.

FontLab objects? RoboFab objects? Are there different flavors of objects? Doesn't that confuse things? FontLab has its own object model. There are FontLab Font objects and FontLab Glyph objects. But these objects are relatively low-level, that means that while using these objects, you have to keep track of a lot of things yourself and understand some FontLab peculiarities. This makes it difficult to write code efficiently. RoboFab is a layer of objects built on top of the FontLab objects, making it a lot easier to work with the data, fewer things to memorise and that means faster development. FontLab now comes bundled with RoboFab. In this conference we focus mainly on the RoboFab objects, but for some things the FontLab objects are needed.

Back to Python. Objects, attributes and methods follow the **dot separated syntax** which is a handy way to clearly state what method or attribute you want to talk to. Other programming languages use dot syntax as well, for instance JavaScript or PHP.

.. code::

    # attribute
    someObject.someAttribute
    someObject.anotherAttribute
    font.path
    glyph.width
    
    # method
    someObject.someMethod(aParameter)
    someObject.anotherMethod()
    font.generate()
    glyph.clear()

See how the dot connects the names? But this can go deeper than one level as well. Sometimes objects contain other objects, which in turn can have.. etc. Dont' worry about getting lost, this is why there is documentation.

.. code::

    # attribute
    someObject.someOtherObject.theOtherObjectsAttribute
    font.info.fullName
    font.info.familyName
     
    # method
    someObject.someOtherObject.theOtherObjectsMethod(aParameter)
    font.kerning.update()

Did you notice some lines has parentheses after them, and others don't? Writing `()` means you want to use the method and execute it. In Python terms: the **method** is **called**.

.. code::

    # a method but not called, you're looking at
    # the python object which contains the method.
    font.update
     
    # but calling a method is more useful,
    # it means: take this code and run it.
    font.update()

------------------------------
Names of variables and methods
------------------------------

In Robofab we have a couple of conventions for naming classes, attributes, methods and functions. These make it easier to predict what something is called and that means fewer trips to the documentation. This is what we're talking about:

- **camelCase**: this means that when a name is made up from several words, eachAdditionalWordStartsWithACap. Examples: ``glyphName``, ``kernTable``, ``groupList``, ``fontTools``.
- **class names** always start with an uppercase, then camelCase. Examples: ``RFont``, ``RGlyph``, ``RKerning``.
- **attribute and method names** always start with a lowercase, then camelCase. Examples: ``kerning.importAFM()``, ``glyph.drawPoints()``

.. note::

    These are our conventions, we do it this way because we prefer it. But that does not mean that Python requires it, as long as your names are legal Python you can write whatever you want. It's just useful to stick to a predictable method one way or the other. Please look at the standard `Python documentation`_ for a full description of the language. Some rules about legal Python names:

    .. _Python documentation: http://python.org/doc/

    - Names can be arbitrarily long.
    - Names can contain letters and numbers.
    - The first character has to be a letter.
    - Names can contain upper and lower case letters.
    - Upper and lower case letters are different.
    - ``bruce`` and ``Bruce`` are different variable names
    - The underscore character ``_`` is legal. ex: ``my_name``

------------------
Installing RoboFab
------------------

Installing RoboFab is usually straightforward. There are quite a few combinations of operating system, FontLab version and Python version possible, some with their own pecularities. There's not much we can do about that, you just have to get it sorted.

More :doc:`installation notes <../docs_intro/install>` in the RoboFab documentation.

-------------
Documentation
-------------

There is a lot of documentation available on the internet. When writing code, `Google`_ is your best friend -- there is almost always someone else who has dealt with or written about the same problem. Reading the documentation is always a good idea. Looking at code snippets is useful too because it will explain how other people have solved problems. Even if a particular bit of code doesn't do what you're looking for, it can give you ideas.

.. _Google: http://google.com

- :doc:`RoboFab objects <../docs_objects/objects>`: the RoboFab API and reference.
- `FontLab objects`_: the FontLab documentation. API and reference for the FontLab objects.
- :doc:`RoboFab introduction to Scripting <../docs_howtos/scripting>`: RoboFab scripting intro.
- `How to think like a computer scientist`_: an introduction into learning Python. Not specifically about typedesign, but general Python programming, lists, dicts, variables, stuff like that.
- :doc:`Emergency Python Basics <python_basics>`: elsewhere on this site an short overview of some of Python's basic stuff.

.. _FontLab objects: http://dev.fontlab.net/flpydoc/
.. _How to think like a computer scientist: http://www.greenteapress.com/thinkpython/
