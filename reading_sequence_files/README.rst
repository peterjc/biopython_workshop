===================================
Reading Sequence Files in Biopython
===================================

Dealing with assorted sequence file formats is one of the strengths of Biopython.
The primary module we'll be using is `Bio.SeqIO <http://biopython.org/wiki/SeqIO>`_,
which is short for sequence input/output (following the naming convention set by
`BioPerl's SeqIO module <http://bioperl.org/wiki/HOWTO:SeqIO>`_).

These examples use a number of real example sequence files, how to obtain these
is described in the `sample data <../SAMPLE_DATA.rst>`_ instructions.

-------------
Built-in Help
-------------

Python code should be documented. You can (and should) write special comment strings
called ``docstrings`` at the start of your own modules, classes and functions which
are used by Python as the built-in help text. Let's look at some of the built-in
Biopython documentation.

We'll run the interactive Python prompt (or you can use a Python GUI if you prefer,
depending what you are used to working with), load the ``SeqIO`` module with the
``import`` command, and have a look at the built in help:

.. sourcecode:: pycon

    $ python2.7
    Python 2.7.3 (default, Nov  7 2012, 23:34:47) 
    [GCC 4.4.6 20120305 (Red Hat 4.4.6-4)] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from Bio import SeqIO
    >>> help(SeqIO)

You'll see the `SeqIO help text <http://biopython.org/DIST/docs/api/Bio.SeqIO-module.html>`_
built into Biopython -- the latest version of which should also be online. Pressing
space will show the next page of help text, the up and down cursor arrows scroll,
and ``q`` will quit the help and return to the Python prompt.

Rather than showing the help for the entire ``SeqIO`` module, you can ask for the help
on a particular object or function. Let's start with ``SeqIO.parse`` - and from now on
the triple greater-than-sign prompt (``>>>``) will be used to indicate something you
would type into Python:

.. sourcecode::	pycon

    >>> help(SeqIO.parse)

This gives some examples, and we'll start with something very similar.

-----------
Sample Data
-----------

For these examples we're going to use files for the famous bacteria *Esherichia coli*
K12 (from the NCBI FTP server), and some potato genes from the PGSC:

- ``NC_000913.faa``
- ``NC_000913.fna``
- ``NC_000913.ffn``
- ``PGSC_DM_v3.4_pep_representative.fasta``

See the main README file for instructions for downloading these files.

----------------
Counting Records
----------------

We'll start by looking at the protein sequence in the FASTA amino acid file,
``NC_000913.faa``. First take a quick peek using some command line tools like
``head`` to look at the start of the file:

.. sourcecode:: console

    $ head NC_000913.faa 
    >gi|16127995|ref|NP_414542.1| thr operon leader peptide [Escherichia coli str. K-12 substr. MG1655]
    MKRISTTITTTITITTGNGAG
    >gi|16127996|ref|NP_414543.1| fused aspartokinase I and homoserine dehydrogenase I [Escherichia coli str. K-12 substr. MG1655]
    MRVLKFGGTSVANAERFLRVADILESNARQGQVATVLSAPAKITNHLVAMIEKTISGQDALPNISDAERI
    FAELLTGLAAAQPGFPLAQLKTFVDQEFAQIKHVLHGISLLGQCPDSINAALICRGEKMSIAIMAGVLEA
    RGHNVTVIDPVEKLLAVGHYLESTVDIAESTRRIAASRIPADHMVLMAGFTAGNEKGELVVLGRNGSDYS
    AAVLAACLRADCCEIWTDVDGVYTCDPRQVPDARLLKSMSYQEAMELSYFGAKVLHPRTITPIAQFQIPC
    LIKNTGNPQAPGTLIGASRDEDELPVKGISNLNNMAMFSVSGPGMKGMVGMAARVFAAMSRARISVVLIT
    QSSSEYSISFCVPQSDCVRAERAMQEEFYLELKEGLLEPLAVTERLAIISVVGDGMRTLRGISAKFFAAL
    ARANINIVAIAQGSSERSISVVVNNDDATTGVRVTHQMLFNTDQVIEVFVIGVGGVGGALLEQLKRQQSW

We can use ``grep`` to count the number of proteins by using the regular
expression pattern ``^>`` (the caret is a special symbol meaning look at
the start of a line):

.. sourcecode::	console

    $ grep -c "^>" NC_000913.faa 
    4141

Now let's count the records with Biopython using the ``SeqIO.parse`` function:

.. sourcecode::	pycon

    $ python
    Python 2.7.3 (default, Nov  7 2012, 23:34:47) 
    [GCC 4.4.6 20120305 (Red Hat 4.4.6-4)] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from Bio import SeqIO
    >>> filename = "NC_000913.faa"
    >>> count = 0
    >>> for record in SeqIO.parse(filename, "fasta"):
    ...     count = count + 1
    >>> print("There were " + str(count) + " records in file " + filename)
    There were 4141 records in file NC_000913.faa

Running more than few commands like this at the Python prompt gets complicated
(especially if you make a mistake and need to edit bits to rerun them). It is also
fiddly to copy and paste without the ``>>>`` prompt and ``...`` line continuation
characters.

Instead, using your favourite editor (e.g. ``nano`` or ``gedit``) create a plain
text file (in the same directory as the *E. coli* files) named ``count_fasta.py``
which contains the following:

.. sourcecode:: python

    from Bio import SeqIO
    filename = "NC_000913.faa"
    count = 0
    for record in SeqIO.parse(filename, "fasta"):
        count = count + 1
    print("There were " + str(count) + " records in file " + filename)

This time it should be easy to copy & paste in one go. We can now run this:

.. sourcecode::	    console

    $ python count_fasta.py
    There were 4141 records in file NC_000913.faa

**Exercise**: Modify this to count the number of records in the other FASTA files,
both from *E. coli* K12 and the potato genome (``PGSC_DM_v3.4_pep_representative.fasta``).

**Advanced Exercise**: Using ``sys.argv`` get the filename as a command line argument,
so that you can run it like this:

.. sourcecode::	console

    $ python count_fasta_adv.py NC_000913.ffn
    There were 4321 records in file NC_000913.ffn

----------------------
Looking at the records
----------------------

In the above example, we used a for loop to count the records in a FASTA file,
but didn't actually look at the information in the records. The ``SeqIO.parse``
function was creating `SeqRecord objects <http://biopython.org/wiki/SeqRecord>`_.
Biopython's ``SeqRecord`` objects are a container holding the sequence, and any
annotation about it - most importantly the identifier.

For FASTA files, the record identifier is taken to be the first word on the ``>``
line -- anything after a space is *not* part of the identifier.

This simple example prints out the record identifers and their lengths:

.. sourcecode:: python

    from Bio import SeqIO
    filename = "NC_000913.faa"
    for record in SeqIO.parse(filename, "fasta"):
        print("Record " + record.id + ", length " + str(len(record)))

If you save that as ``record_lengths.py`` and run it you'll get over four thousand
lines of output:

.. sourcecode::	console

    $ python record_lengths.py
    Record gi|16127995|ref|NP_414542.1|, length 21
    Record gi|16127996|ref|NP_414543.1|, length 820
    Record gi|16127997|ref|NP_414544.1|, length 310
    Record gi|16127998|ref|NP_414545.1|, length 428
    ...
    Record gi|16132219|ref|NP_418819.1|, length 46
    Record gi|16132220|ref|NP_418820.1|, length 228
    
The output shown here is truncated!

**Excercise**: Count how many sequences are less than 100 amino acids long.

**Exercise**: Create a modified script ``total_length.py`` based on the above examples
which counts the number of records and calculates the total length of all the
sequences (i.e. ``21 + 820 + 310 + 428 + ... + 46 + 228``), giving:

.. sourcecode::	console

    $ python total_length.py
    4141 records, total length 1311442

**Advanced Exercise**: Plot a histogram of the sequence length distribution (tip - see the
`Biopython Tutorial & Cookbook <http://biopython.org/DIST/docs/tutorial/Tutorial.html>`_).

-----------------------
Looking at the sequence
-----------------------

The record identifiers are very important, but more important still is the sequence
itself. In the ``SeqRecord`` objects the identifiers are stored as standard Python
strings. For the sequence, Biopython uses a string-like ``Seq`` object.

In many ways the ``Seq`` objects act like Python strings, you can print them, take
their length using the ``len(...)`` function, and slice them with square brackets
to get a sub-sequence or a single letter.

**Exercise**: Using ``SeqIO.parse(...)`` in a for loop, for each record print out the
identifier, the first 10 letters of each sequences, the last 10 letters. e.g.:

.. sourcecode::	console

   $ python print_seq.py
   gi|16127995|ref|NP_414542.1| MKRISTTITT...ITITTGNGAG
   gi|16127996|ref|NP_414543.1| MRVLKFGGTS...LRTLSWKLGV
   gi|16127997|ref|NP_414544.1| MVKVYAPASS...DTAGARVLEN
   ...
   gi|16132219|ref|NP_418819.1| MTKVRNCVLD...AVILTILTAT
   gi|16132220|ref|NP_418820.1| MRITIILVAP...LHDIEKNITK

---------------------------------------
Checking proteins start with methionine
---------------------------------------

In the next example we'll check all the protein sequences start with a methionine
(represented as the letter "M" in the standard IUPAC single letter amino acid code),
and count how many records fail this. Let's create a script called ``check_start_met.py``:

.. sourcecode:: python

    from Bio import SeqIO
    filename = "NC_000913.faa"
    bad = 0
    for record in SeqIO.parse(filename, "fasta"):
        if not record.seq.startswith("M"):
            bad = bad + 1
            print(record.id + " starts " + record.seq[0])
    print("Found " + str(bad) + " records in " + filename + " which did not start with M")

If you run that, you should find this *E. coli* protein set all had leading methionines:

.. sourcecode::	console

    $ python check_start_met.py
    Found 0 records in NC_000913.faa which did not start with M

Good - no strange proteins. This genome has been completely sequenced and a lot of
work has been done on the annotation, so it is a 'Gold Standard'. Now try this on
the potato protein file ``PGSC_DM_v3.4_pep_representative.fasta``:

.. sourcecode::	console

    $ python check_start_met.py
    PGSC0003DMP400032467 starts T
    PGSC0003DMP400011427 starts Q
    PGSC0003DMP400068739 starts E
    ...
    PGSC0003DMP400011481 starts Y
    Found 208 records in PGSC_DM_v3.4_pep_representative.fasta which did not start with M

**Excercise**: Modify this script to print out the description of the problem records,
not just the identifier. *Tip*: Try reading the documentation, e.g. Biopython's wiki page
on the `SeqRecord <http://biopython.org/wiki/SeqRecord>`_.

**Discussion**: What did you notice about these record descriptions? Can you think of any
reasons why there could be so many genes/proteins with a problem at the start?

------------------------
Checking stop characters
------------------------

In the standard one letter IUPAC amino acid codes for proteins, "*" is used for a
stop codon. For many analyses tools having a "*" in the protein sequence can cause
an error. There are two main reasons why you might see a "*" in a protein sequence.

First, it might be there from translation up to and including the closing stop codon
for the gene. In this case, you might want to remove it.

Second, it could be there from a problematic/broken annotation where there is an
in-frame stop codon. In this case, you might want to fix the annotation, remove
the whole sequence, or perhaps cheat and replace the "*" with an "X" for an unknown
amino acid.

We'll talk about writing out sequence files soon, but first let's check the example
protein FASTA files for any "*" symbols in the sequence. For this you can use several
of the standard Python string operations which also apply to ``Seq`` objects, e.g.:

.. sourcecode:: python

    >>> my_string = "MLNTCRVPLTDRKVKEKRAMKQHKAMIVALIVICITAVVAALVTRKDLCEVHIRTGQTEVAVFTAYESE*"
    >>> my_string.startswith("M")
    True
    >>> my_string.endswith("*")
    True
    >>> len(my_string)
    70
    >>> my_string.count("M")
    3
    >>> my_string.count("*")
    1

**Exercise**: Write a python script to check ``NC_000913.faa`` to count the number of
sequences with a "*" in them (anywhere), and the number where the sequence ends with
a "*". Then try it on ``PGSC_DM_v3.4_pep_representative.fasta`` as well. e.g.:

.. sourcecode::	console

    $ python check_stops.py
    Checking NC_000913.faa for terminal stop codons
    0 records with * in them
    0 with * at the end

**Discussion**: What did you notice about the "*" stop characters in these FASTA files?
What should we do to 'fix' the problems?

--------------
Single Records
--------------

One of the example FASTA files for *E. coli* K12 is the a single long sequence
for the entire (circular) genome, file ``NC_000913.fna``. We can still use a
for loop and ``SeqIO.parse(...)`` but it can feel awkward. Instead, for the
special case where the sequence file contains one and only one record, you
can use ``SeqIO.read(...)``.

.. sourcecode:: pycon

    >>> from Bio import SeqIO
    >>> record = SeqIO.read("NC_000913.fna", "fasta")
    >>> print(record.id + " length " + str(len(record)))
    gi|556503834|ref|NC_000913.3| length 4641652

*Exercise*: Try using ``SeqIO.read(...)`` on one of the protein files.
What happens?

----------------------
Different File Formats
----------------------

So far we've only been using FASTA format files, which is why when we've called
``SeqIO.parse(...)`` or ``SeqIO.read(...)`` the second argument has been ``"fasta"``.
The Biopython ``SeqIO`` module supports quite a few other important sequence file
formats (see the table on the `SeqIO wiki page <http://biopython.org/wiki/SeqIO>`_).

If you work with finished genomes, you'll often see nicely annotated files in
the EMBL or GenBank format. Let's try this with the *E. coli* K12 GenBank file,
``NC_000913.gbk``, based on the previous example:

.. sourcecode::	pycon

    >>> from Bio import SeqIO
    >>> fasta_record = SeqIO.read("NC_000913.fna", "fasta")
    >>>	print(fasta_record.id + " length " + str(len(fasta_record)))
    gi|556503834|ref|NC_000913.3| length 4641652
    >>> genbank_record = SeqIO.read("NC_000913.gbk", "genbank")
    >>>	print(genbank_record.id + " length " + str(len(genbank_record)))
    NC_000913.3 length 4641652

All we needed to change was the file format argument to the ``SeqIO.read(...)``
function - and we could load a GenBank file instead. You'll notice the GenBank
version was given a shorter identifier, and took longer to load. The reason is
that there is a lot more information present - most importantly lots of features
(where each gene is and so on). We'll return to this in a later section,
`working with sequence features <../using_seqfeatures/README.rst>`_.

===================================
Writing Sequence Files in Biopython
===================================

We move on to `writing sequence files <../writing_sequence_files/README.rst>`_
in the next section.
