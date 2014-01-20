Sequence Files in Biopython
===========================

Dealing with assorted sequence file formats is one of the strengths of Biopython.
The primary module we'll be using is `Bio.SeqIO <http://biopython.org/wiki/SeqIO>`_,
which is short for sequence input/output (following the naming convention set by
`BioPerl's SeqIO module <http://bioperl.org/wiki/HOWTO:SeqIO>`_).

Built-in Help
-------------

Python code should be documented. You can (and should) write special comment strings
called ``docstrings`` at the start of your own modules, classes and functions which
are used by Python as the built-in help text. Let's look at some of the built-in
Biopython documentation.

We'll run the interactive Python prompt (or you can use a Python GUI if you prefer,
depending what you are used to working with), load the ``SeqIO`` module with the
``import`` command, and have a look at the built in help::

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
``head`` to look at the start of the file::

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

    $ grep -c "^>" NC_000913.faa 
    4141

Now let's count the records with Biopython using the ``SeqIO.parse`` function::

    $ python
    Python 2.7.3 (default, Nov  7 2012, 23:34:47) 
    [GCC 4.4.6 20120305 (Red Hat 4.4.6-4)] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from Bio import SeqIO
    >>> filename = "NC_000913.faa"
    >>> count = 0
    >>> for record in SeqIO.parse(filename, "fasta"):
    ...     count += 1
    >>> print("There were %i records in file %s" % (count, filename))
    There were 4141 records in file NC_000913.faa

Running more than few commands like this at the Python prompt gets complicated
(especially if you make a mistake and need to edit bits to rerun them). It is also
fiddly to copy and paste without the ``>>>`` prompt and ``...`` line continuation
characters.

Instead, using your favourite editor (e.g. ``nano`` or ``gedit``) create a plain
text file (in the same directory as the *E. coli* files) named ``count_proteins.py``
which contains the following::

    from Bio import SeqIO
    filename = "NC_000913.faa"
    count = 0
    for record in SeqIO.parse(filename, "fasta"):
        count += 1
    print("There were %i records in file %s" % (count, filename))

This time it should be easy to copy & paste in one go. We can now run this:

    $ python count_proteins.py
    There were 4141 records in file NC_000913.faa

**Exercise**: Modify this to count the number of records in the other FASTA files,
both from *E. coli* K12 and the potato genome (``PGSC_DM_v3.4_pep_representative.fasta``).

**Advanced exercise**: Using ``sys.argv`` get the filename as a command line argument,
so that you can run it like this::

    $ python count_proteins_adv.py NC_000913.ffn
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

    from Bio import SeqIO
    filename = "NC_000913.faa"
    for record in SeqIO.parse(filename, "fasta"):
        print("Record %s, length %i" % (record.id, len(record)))

If you save that as ``record_lengths.py`` and run it you'll get over four thousand
lines of output:

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
identifier, the first 10 letters of each sequences, the last 10 letters. e.g.

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
and count how many records fail this. Let's create a script called ``check_start_met.py``::

    from Bio import SeqIO
    filename = "NC_000913.faa"
    bad = 0
    for record in SeqIO.parse(filename, "fasta"):
        if not record.seq.startswith("M"):
            bad += 1
            print("%s starts %s" % (record.id, record.seq[0]))
    print("Found %i records in %s which did not start with M" % (bad, filename))

If you run that, you should find this *E. coli* protein set all had leading methionines:

    $ python check_start_met.py
    Found %i records in NC_000913.faa which did not start with M

Good - no strange proteins. This genome has been completely sequenced and a lot of
work has been done on the annotation, so it is a 'Gold Standard'. Now try this on
the potato protein file ``PGSC_DM_v3.4_pep_representative.fasta``

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

What did you notice about these record descriptions?


----------------
Parsing Potatoes
----------------

For this example we'll first download and unzip a FASTA file of potato proteins. You
can download this at the command line using the ``wget`` command, and decompress the
ZIP file using the ``unzip`` command as follows. Note ``$`` indicates the command line
prompt, copy and paste (or type) the text starting ```wget``` etc::

    $ wget http://potato.plantbiology.msu.edu/data/PGSC_DM_v3.4_pep_representative.fasta.zip
    $ unzip PGSC_DM_v3.4_pep_representative.fasta.zip

Mac OS X users, instead of ``wget http://...`` you can use ``curl -O http://...`` here.

Once unzipped, you should have a plain text FASTA file ``PGSC_DM_v3.4_pep_representative.fasta``
which we'll just look at quickly using a few more command line tools before starting Python.
You can print the entire file to the terminal using ``cat``, but since it is quite large
we'll use ``head`` to look at the start only::

    $ head PGSC_DM_v3.4_pep_representative.fasta
    >PGSC0003DMP400067339 PGSC0003DMT400095664 Protein
    MGVWKDSNYGKGVIIGVIDTGILPDHPSFSDVGMPPPPAKWKGVCESNFINKCNNKLIGA
    RSYQLGNGSPIDGNGHGTHTASTAAGAFVKGANVFGNANGTAVGVAPLAHIAVYKVCSSD
    GGCSDSDILAAMDSAIDDGVDVLSISLGGSPNSFYDDPIALGAYSATARGILVSCSAGNR
    GPLLASVGNAAPWILTVGASTLDRKIKATVKLGNGEEFEGESAYRPQISNSTFFTLFDAA
    KHAKDQSETPYCKPGSLNDPVIRGKIVLCLAGGGVGGGVANVDKGQVVKDAGGVGMIVIK
    TSQYGVTKSADAHVLPALDVSDADGLRIRAYTNSTINSVATITFQGTIIGDKNAPIVAAF
    SSRGPSRASPGILKPDIIGPGVNILASWTTSVDDNKNTKSTFNIISGTSMSCPHLSGVAA
    LLKSSHPDWSPAVIKSAIMTTADTLNLANSPILDERLIPAYIFAVGAGHVNPSRANDPGL
    VYDTPFEDYVPYFCGLNYTNREVGKMLQRQVNCLKVKSIPEAQLNYPSFSIFRLGSTPQT

We can count the number of records using the ``grep`` command and the regular expression
pattern ``^>`` which means look for a greater-than-sign at the start of a line:

    $ grep -c "^>" PGSC_DM_v3.4_pep_representative.fasta
    39031

That says this FASTA file contains nearly forty thousand sequences, quite a lot bigger!
