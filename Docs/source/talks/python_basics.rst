Basic Python
============

In these and following examples we'll be using a couple of programming things which are simple enough that, should you not be familiar with them, you might be able to figure out from the contect. While the experienced programmers will tap their feet impatiently for this to finish, and the newbies are struggling to pick their dicts from their strings: a very short overview of the stuff you're missing.

Conditional statements
----------------------

If some condition is met: execute a separate block of your script::

    >>> if 1+1 == 2:
    ...     print "still true"
    >>> else:
    ...     print "oops"
    still true

Compound statements
-------------------

For each item in this list: execute a seperate block of your script::

    >>> for item in [1, 2, 3, "a"]:
    ...     print item
    1
    2
    3
    "a"

Assignment
----------

This is basically setting something to a new value, or attaching a name to something::

    >>> a = 10
    >>> print a
    10

The information that you want to work with in programming comes in different forms and colors: text, numbers, sequences of things. Python offers a nice range of tupperware boxes to stick them in. More things to keep track of, but: useful and these will be your friends.

Strings
-------

Text, letters, words, are called strings and they live between quotes. In order to allow quotes in strings you have several quote alternatives::

    # examples of strings
    a = "a string"
    b = 'a string too'
    c = 'a "string" too'
    d = """a triple quoted string - but still just a string."""
    e = '''a triple quoted string - but still just a string.'''

Numbers
-------

Whole numbers, decimal numbers. You don't need to do anything special to make them, just write them::

    # examples of numbers
    a = 1900
    b = -239345
    c = 1.349683
    d = 0

Lists
-----

Sequences can be written between brackets. You've seen one earlier. Lists are powerful things to keep stuff in order. Some objects can behave like lists. List objects have useful methods to manipulate them::

    >>> # examples of lists
    >>> aList = [4, "a", 2, 1] 
    >>> aListInAList = [ [1, 2], [3, 4] ]
    >>> print len(aList)
    >>> sort(aList)
    >>> print aList
    4
    [1, 2, 4, 'a']

Dictionaries
------------

These are similar to lists, but rather than just store a sequence, a dictionary stores a ``key: value`` pair. In order to get the value, you need to provide the key. Dictionaries are written between {braces}. Some objects can behave like dictionaries. Dictionary objects have useful methods to manipulate them. While lists have their sequencential order, dictionaries don't, something to remember when you're iterating::

    >>> # examples of dicts
    >>> aDict = {"key": "value", 100: 200}
    >>> print aDict.keys()
    >>> print aDict.values()
    >>> print aDict.items()
    >>> print len(aDict)
    [100, 'key']
    [200, 'value']
    [(100, 200), ('key', 'value')]
    2

Tuples
------

Sequences between parentheses, rather than square brackets. Tuples are very much like lists, except that you can't really change them. For instance a tuple can't sort like a list can::

    # examples of tuples
    aTuple = (1, 2, 3)
    aTuple = ("a", "b", "c")

And that's really all we're going to say about this. Figure out the rest yourself.
