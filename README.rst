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

========
Notation
========

Text blocks starting with ``$`` show something you would type and run at the
command line prompt, where the ``$`` itself represents the prompt. For example::

    $ python -V
    Python 2.7.5

Depending how your system is configured, rather than just ``$`` you may see you
user name and the current working directory.

Lines starting ``>>>``` represent the interactive Python prompt, and something
you would type inside Python. For example:

    $ python
    Python 2.7.3 (default, Nov  7 2012, 23:34:47) 
    [GCC 4.4.6 20120305 (Red Hat 4.4.6-4)] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 7 * 6
    42
    >>> quit()

Here you would only need to type ``7 * 6`` (and enter) into Python, the ``>>>```
is already there. To quit the interactive Python prompt use ``quit()`` (and enter).
This example would usually be shortened to just:

    >>> 7 * 6
    42

These text blocks are also used for entire short Python scripts, which you can
copy and save as a plain text file with the extension `.py` to run them.

=============
Prerequisites
=============

We assume you have Python and Biopython 1.63 or later installed and working.
Biopython 1.63 supports Python 2.6, 2.7 and 3.3 (and should work on more recent
versions). The examples here assume you are using Python 2.6 or 2.7, but in
general should work with Python 3 with minimal changes. Check this works::

    $ python -c "import Bio; print(Bio.__version__)"
    1.63


=================
Workshop Sessions
=================

TODO - Links to separate documents.

===========
Sample Data
===========

Many of the examples will use real biological data files. You could download them all
at the start, or gradually as needed.

Under Linux this is easily done at the command line with the ``wget`` tool. For Mac
OS X users, ``wget`` is not installed by default so instead of ``wget ftp://...`` or
``wget http://..`` please use ``curl -O ftp://...`` or ``curl -O http://..`` instead.

In the following command line examples ``$`` indicates the command line prompt, copy
and paste (or type) the text starting after this (e.g. ``wget ftp://...``).

---------------------
*Esherichia coli* K12
---------------------

We'll use the complete genome of this model bacteria in GenBank format, FASTA format,
plus FASTA files of the annotated genes and their protein sequences::

    $ wget ftp://ftp.ncbi.nlm.nih.gov/genomes/Bacteria/Escherichia_coli_K_12_substr__MG1655_uid57779/NC_000913.gbk
    $ wget ftp://ftp.ncbi.nlm.nih.gov/genomes/Bacteria/Escherichia_coli_K_12_substr__MG1655_uid57779/NC_000913.fna
    $ wget ftp://ftp.ncbi.nlm.nih.gov/genomes/Bacteria/Escherichia_coli_K_12_substr__MG1655_uid57779/NC_000913.ffn
    $ wget ftp://ftp.ncbi.nlm.nih.gov/genomes/Bacteria/Escherichia_coli_K_12_substr__MG1655_uid57779/NC_000913.faa

The NCBI use a confusing range of file extensions, but ``*.fna``, ``*.ffn`` and ``*.faa``
are all plain text FASTA files - but specificially they are a whole chromosome (``*.fna``),
gene sequences (``*.ffn``), and protein/amino acid sequences (``*.faa``).

------
Potato
------

We'll use this amino acid/protein set from the Potato Genome Sequencing Consortium (PGSC)
(see http://solanaceae.plantbiology.msu.edu/pgsc_download.shtml for more downloads) for
the doubled monoploid *Solanum tuberosum* group Phureja clone DM1-3::

    $ wget http://potato.plantbiology.msu.edu/data/PGSC_DM_v3.4_pep_representative.fasta.zip

For anyone working on Mac OS X, the ``wget`` command is not installed by default. You can
use this slightly more complicated ``curl`` command instead::

    $ curl -O http://potato.plantbiology.msu.edu/data/PGSC_DM_v3.4_pep_representative.fasta.zip

Once download, decompress the ZIP file using the ``unzip`` command::

    $ unzip PGSC_DM_v3.4_pep_representative.fasta.zip

=====================
Copyright and Licence
=====================

Copyright 2014 by Peter Cock, The James Hutton Institute, Dundee, UK. All rights reserved.

This work is licensed under a `Creative Commons Attribution-ShareAlike 4.0 International
License <http://creativecommons.org/licenses/by-sa/4.0/>`_ (CC-BY-SA 4.0).

.. image:: http://i.creativecommons.org/l/by-sa/4.0/88x31.png

Note this documentation links to and uses external and separately licenced sample data.
