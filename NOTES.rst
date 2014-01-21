As this material is aimed at Python beginners, we're avoiding a lot of
useful but not fundamental things, including:

* String formating with the % operator
* The ``with`` statement for context management (e.g. closing file handles)
* The increment/decrement operators, use ``count = count + 1`` not ``count += 1``

Also note that the examples should try to run under both Python 2 and 3
without changes. To this end, only simple print statements are used as
``print(some_string)`` which will work on both Python 2 and 3, with or
without using ``from __future__ import print_function``.
