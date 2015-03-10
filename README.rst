=========================
Introduction to Biopython
=========================

This is a basic introduction to Biopython, intended for a classroom based workshop.
It assumes you have been introduced to both working at the command line, and basic
Python - for example as covered in Martin Jones' free eBook
`Python for Biologists <http://pythonforbiologists.com/index.php/introduction-to-python-for-biologists/>`_.

The Biopython website http://www.biopython.org has more information including the 
`Biopython Tutorial & Cookbook <http://biopython.org/DIST/docs/tutorial/Tutorial.html>`_
(html, `PDF available <http://biopython.org/DIST/docs/tutorial/Tutorial.pdf>`_),
which is worth going through once you have mastered the basics of Python.

=================
Workshop Sections
=================

The examples use a number of `sample data files <SAMPLE_DATA.rst>`_.

* `Reading sequence files <reading_sequence_files/README.rst>`_.
* `Writing sequence files <writing_sequence_files/README.rst>`_.
* `Working with sequence features <using_seqfeatures/README.rst>`_.
* `Reading and writing alignment files <reading_writing_alignments/README.rst>`_.

This material focuses on Biopython's `SeqIO <http://biopython.org/wiki/SeqIO>`_
and `AlignIO <http://biopython.org/wiki/AlignIO>`_ modules (these links
include an overview and tables of supported file formats), each of which
also has a whole chapter in the `Biopython Tutorial & Cookbook
<http://biopython.org/DIST/docs/tutorial/Tutorial.html>`_
(`PDF <http://biopython.org/DIST/docs/tutorial/Tutorial.pdf>`_)
which would be worth reading after this workshop to learn more.

========
Notation
========

Text blocks starting with ``$`` show something you would type and run at the
command line prompt, where the ``$`` itself represents the prompt. For example:

.. sourcecode:: console

    $ python -V
    Python 2.7.5

Depending how your system is configured, rather than just ``$`` you may see you
user name and the current working directory. Here you would only type ``python -V``
(python space minus capital V) to find out the default version of Python installed.

Lines starting ``>>>`` represent the interactive Python prompt, and something
you would type inside Python. For example:

.. sourcecode:: pycon

    $ python
    Python 2.7.3 (default, Nov  7 2012, 23:34:47) 
    [GCC 4.4.6 20120305 (Red Hat 4.4.6-4)] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 7 * 6
    42
    >>> quit()

Here you would only need to type ``7 * 6`` (and enter) into Python, the ``>>>``
is already there. To quit the interactive Python prompt use ``quit()`` (and enter).
This example would usually be shortened to just:

.. sourcecode:: pycon

    >>> 7 * 6
    42

These text blocks are also used for entire short Python scripts, which you can
copy and save as a plain text file with the extension ``.py`` to run them.

=============
Prerequisites
=============

We assume you have Python and Biopython 1.63 or later installed and working.
Biopython 1.63 supports Python 2.6, 2.7 and 3.3 (and should work on more recent
versions). The examples here assume you are using Python 2.6 or 2.7, but in
general should work with Python 3 with minimal changes. Check this works:

.. sourcecode:: console

    $ python -c "import Bio; print(Bio.__version__)"
    1.63

Most of the examples use real biological data files. You could download them
all at the start, or gradually as needed - see `sample data <SAMPLE_DATA.rst>`_
for instructions.

================
Sample Solutions
================

Each workshop section was written in a separate directory, and in addition
to the main text (named ``README.rst`` which is plain text file with markup
to make it look pretty on GitHub), the folders contain sample solution
Python scripts (named as in the text).

If you are reading this on GitHub, you can view, copy/paste or download
individual examples from your web browser. Or, you can use the ``git``
command line tool to make a local copy of the entire workshop:

.. sourcecode:: console

    $ git clone https://github.com/peterjc/biopython_workshop.git

Or,

.. sourcecode:: console

    $ git clone git@github.com:peterjc/biopython_workshop.git

The best option may depend on your firewall settings. To learn more about
``git`` and software version control, I recommend a course like one of the
`Software Carpentry Bootcamps <http://software-carpentry.org/bootcamps/index.html>`_.

=======
History
=======

This material was first used as part of a two-day course "Introduction to Python for
Biologists" (Kathryn Crouch, Peter Cock and Tim Booth), part of a two-week course
`Keystone Skills in Bioinformatics <http://environmentalomics.org/foundations/>`_,
held in February 2014 at Centre for Ecology & Hydrology (CEH), Wallingford, UK.
In a morning session lasting about 2.5 hours (plus coffee break), we covered all
of `reading sequence files <reading_sequence_files/README.rst>`_ and
`writing sequence files <writing_sequence_files/README.rst>`_ - and I quickly
talked through `alignment files <reading_writing_alignments/README.rst>`_.

I presented much of it again later in February 2014 at the University of Dundee
as part of the third year undergraduate course *BS32010 Applied Bioinformatics*
run by Dr David Martin and Dr David Booth. In the two hour slot we covered all
of `reading sequence files <reading_sequence_files/README.rst>`_ and most of
`writing sequence files <writing_sequence_files/README.rst>`_.

I repeated this in March 2015 for the same third year undergraduate course,
*BS32010 Applied Bioinformatics* at the University of Dundee.

=====================
Copyright and Licence
=====================

Copyright 2014-2015 by Peter Cock, The James Hutton Institute, Dundee, UK.
All rights reserved.

This work is licensed under a `Creative Commons Attribution-ShareAlike 4.0 International
License <http://creativecommons.org/licenses/by-sa/4.0/>`_ (CC-BY-SA 4.0).

.. image:: http://i.creativecommons.org/l/by-sa/4.0/88x31.png

Note this documentation links to and uses external and separately licenced
`sample data <SAMPLE_DATA.rst>`_ files.
