====================================
Writing Sequences Files in Biopython
====================================

The `previous section <../reading_sequence_files/README.rst>`_ talked
about reading sequence files in Biopython using the ``SeqIO.parse(...)``
function. Now we'll focus on writing sequence files using the sister
function ``SeqIO.write(...)``.

The more gently paced `Biopython Tutorial and Cookbook
<http://biopython.org/DIST/docs/tutorial/Tutorial.html>`_
(`PDF <http://biopython.org/DIST/docs/tutorial/Tutorial.pdf>`_)
first covers creating your own records (``SeqRecord`` objects) and
then how to write them out. We're going to skip that here, and work
with ready-made ``SeqRecord`` objects loaded with ``SeqIO.parse(...)``.

Let's start with something really simple...

--------------------------
Converting a sequence file
--------------------------

Recall we looked at the *E. coli* K12 chromosome as a FASTA file
``NC_000913.fna`` and as a GenBank file ``NC_000913.gbk``. Suppose
we only had the GenBank file, and wanted to turn it into a FASTA file?

Biopython's ``SeqIO`` module can read and write lots of sequence file
formats, and has a handy helper function to convert a file:

.. sourcecode:: pycon

    >>> from Bio import SeqIO
    >>> help(SeqIO.convert)

Here's a very simple script which uses this function:

.. sourcecode:: python

    from Bio import SeqIO
    input_filename = "NC_000913.gbk"
    output_filename = "NC_000913_converted.fasta"
    count = SeqIO.convert(input_filename, "gb", output_filename, "fasta")
    print(str(count) + " records converted")

Save this as ``convert_gb_to_fasta.py`` and run it:

.. sourcecode:: console

    $ python convert_gb_to_fasta.py
    1 records converted

Notice that the ``SeqIO.convert(...)`` function returns the number of
sequences it converted -- here only one. Also have a look at the output file:

.. sourcecode:: console

    $ head NC_000913_converted.fasta 
    >NC_000913.3 Escherichia coli str. K-12 substr. MG1655, complete genome.
    AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTC
    TGATAGCAGCTTCTGAACTGGTTACCTGCCGTGAGTAAATTAAAATTTTATTGACTTAGG
    TCACTAAATACTTTAACCAATATAGGCATAGCGCACAGACAGATAAAAATTACAGAGTAC
    ACAACATCCATGAAACGCATTAGCACCACCATTACCACCACCATCACCATTACCACAGGT
    AACGGTGCGGGCTGACGCGTACAGGAAACACAGAAAAAAGCCCGCACCTGACAGTGCGGG
    CTTTTTTTTTCGACCAAAGGTAACGAGGTAACAACCATGCGAGTGTTGAAGTTCGGCGGT
    ACATCAGTGGCAAATGCAGAACGTTTTCTGCGTGTTGCCGATATTCTGGAAAGCAATGCC
    AGGCAGGGGCAGGTGGCCACCGTCCTCTCTGCCCCCGCCAAAATCACCAACCACCTGGTG
    GCGATGATTGAAAAAACCATTAGCGGCCAGGATGCTTTACCCAATATCAGCGATGCCGAA

**Warning**: The output will over-write any pre-existing file of the same name.

**Advanced Exercise**: Modify this to add command line parsing to take
the input and output filenames as arguments.

The ``SeqIO.convert(...)`` function is effectively a shortcut combining
``SeqIO.parse(...)`` for input ``SeqIO.write(...)`` for output. Here's how
you'd do this explictly:

.. sourcecode::	python

    from Bio import SeqIO
    input_filename = "NC_000913.gbk"
    output_filename = "NC_000913_converted.fasta"
    records_iterator = SeqIO.parse(input_filename, "gb")
    count = SeqIO.write(records_iterator, output_filename, "fasta")    
    print(str(count) + " records converted")

Previously we'd always used the results from ``SeqIO.parse(...)`` in a for
loop - but here the for loop happens inside the ``SeqIO.write(...)`` function.

**Exercise**: Check this does the same as the ``SeqIO.convert(...)`` version above.

The ``SeqIO.write(...)`` function is happy to be given multiple records
like this, or simply as a list of ``SeqRecord`` objects. You can also give
it just one record:

.. sourcecode:: python

    from Bio import SeqIO
    input_filename = "NC_000913.gbk"
    output_filename = "NC_000913_converted.fasta"
    record = SeqIO.read(input_filename, "gb")
    SeqIO.write(record, output_filename, "fasta")

We'll be doing this in the next example, where we call ``SeqIO.write(..)``
several times in order to build up a mult-record output file.

-------------------------
Filtering a sequence file
-------------------------

Suppose we wanted to filter a FASTA file by length, for example
exclude protein sequences less than 100 amino acids long.

The `Biopython Tutorial and Cookbook
<http://biopython.org/DIST/docs/tutorial/Tutorial.html>`_
(`PDF <http://biopython.org/DIST/docs/tutorial/Tutorial.pdf>`_)
has filtering  examples combining ``SeqIO.write(...)`` with more
advanced Python features like generator expressions and so on.
These are all worth learning about later, but in this workshop
we will stick with the simpler for-loop.

You might try something like this:

.. sourcecode:: python

    from Bio import SeqIO
    input_filename = "NC_000913.faa"
    output_filename = "NC_000913_long_only.faa"
    count = 0
    total = 0
    for record in SeqIO.parse(input_filename, "fasta"):
        total = total + 1
        if 100 <= len(record):
            count = count + 1
	    SeqIO.write(record, output_filename, "fasta")
    print(str(count) + " records selected out of " + str(total))

Save this as ``length_filter_naive.py``, and run it, and check it worked.

.. sourcecode:: console

    $ python length_filter_naive.py
    3719 records selected out of 4141

*Discussion:* What goes wrong and why? Have a look at the output file...

.. sourcecode:: console

    $ grep -c "^>" NC_000913_long_only.faa
    1
    $ cat NC_000913_long_only.faa 
    >gi|16132220|ref|NP_418820.1| predicted methyltransferase [Escherichia coli str. K-12 substr. MG1655]
    MRITIILVAPARAENIGAAARAMKTMGFSDLRIVDSQAHLEPATRWVAHGSGDIIDNIKV
    FPTLAESLHDVDFTVATTARSRAKYHYYATPVELVPLLEEKSSWMSHAALVFGREDSGLT
    NEELALADVLTGVPMVADYPSLNLGQAVMVYCYQLATLIQQPAKSDATADQHQLQALRER
    AMTLLTTLAVADDIKLVDWLQQRLGLLEQRDTAMLHRLLHDIEKNITK

The problem is that our output file only contains *one* sequence, actually
the last long sequence in the FASTA file. Why? What happened is each time
round the loop when we called ``SeqIO.write(...)`` to save one record, it
overwrote the existing data.

The solution is to open and close the file explicitly, using a *file handle*.
The ``SeqIO`` functions are happy to work with either filenames (strings) or
file handles, and this is a case where the more low-level handle is useful.

Here's a working version of the script, save this as ``length_filter.py``:

.. sourcecode:: python

    from Bio import SeqIO
    input_filename = "NC_000913.faa"
    output_filename = "NC_000913_long_only.faa"
    count = 0
    total = 0
    output_handle = open(output_filename, "w")
    for record in SeqIO.parse(input_filename, "fasta"):
        total = total + 1
        if 100 <= len(record):
            count = count + 1
	    SeqIO.write(record, output_handle, "fasta")
    output_handle.close()
    print(str(count) + " records selected out of " + str(total))

This time we get the expected output - and it is much faster (needlessly
creating and replacing several thousand small files is slow):

.. sourcecode:: console

    $ python length_filter.py
    3719 records selected out of 4141
    $ grep -c "^>" NC_000913_long_only.faa 
    3719

Yay!


-----------------
Editing sequences
-----------------

One of the examples in the `previous section <../reading_sequence_files/README.rst>`_
looked at the potato protein sequences, and that they all had a terminal "*"
character (stop codon). Python strings, Biopython ``Seq`` and ``SeqRecord`` objects
can all be *sliced* to extract a sub-sequence or partial record. In this case,
we want to take everything up to but excluding the final letter:

.. sourceode: pycon

    >>> my_seq = "MTAIVIGAKILGIIYSSPQLRKCNSATQNDHSDLQISFWKDHLRQCTTNS*"
    >>> cut_seq = my_seq[:-1] # remove last letter
    >>> print(cut_seq)
    MTAIVIGAKILGIIYSSPQLRKCNSATQNDHSDLQISFWKDHLRQCTTNS

Consider the following example (which I'm calling ``cut_star_dangerous.py``):

.. sourcecode:: python

    from Bio import SeqIO
    input_filename = "PGSC_DM_v3.4_pep_representative.fasta"
    output_filename = "PGSC_DM_v3.4_pep_rep_no_stars.fasta"
    output_handle = open(output_filename, "w")
    for record in SeqIO.parse(input_filename, "fasta"):
        cut_record = record[:-1] # remove last letter
        SeqIO.write(cut_record, output_handle, "fasta")
    output_handle.close()

This should work fine on this potato file... but what might go wrong if you
used it on another protein file? What happens if (some of) the input records
don't end with a "*"?

**Exercise**: Modify this example to only remove the last letter if it is a "*"
(and save the original record unchanged if it does not end with "*"). The sample
solution is called ``cut_final_star.py`` instead.


------------------------
Filtering by record name
------------------------

A very common task is pulling out particular sequences from a large sequence
file. Membership testing with Python lists (or sets) is one neat way to do
this. Recap:

.. sourcecode:: pycon

    >>> wanted_ids = ["PGSC0003DMP400019313", "PGSC0003DMP400020381", "PGSC0003DMP400020972"]
    >>> "PGSC0003DMP400067339" in wanted_ids
    False
    >>> "PGSC0003DMP400020972" in wanted_ids
    True

*Exercise*: Guided by the ``filter_length.py`` script, write a new script
starting as follows which writes out the potato proteins on this list:

.. sourcecode:: python

    from Bio import SeqIO
    wanted_ids = ["PGSC0003DMP400019313", "PGSC0003DMP400020381", "PGSC0003DMP400020972"]
    input_filename = "PGSC_DM_v3.4_pep_representative.fasta"
    output_filename = "wanted_potato_proteins.fasta"
    count = 0
    total = 0
    output_handle = open(output_filename, "w")
    # ...
    # Your code here
    # ...
    output_handle.close()
    print(str(count) + " records selected out of " + str(total))

The sample solution is called ``filter_wanted_ids.py``, and the output should be:

.. sourcecode:: console

    $ python filter_wanted_id.py
    3 records selected out of 39031

*Advanced Excerise*: Modify this to read the list of wanted identifiers from
a plain text input file (one identifier per line).

*Discussion*: What happens if a wanted identifier is not in the input file?
What happens if an identifer appears twice? What order is the output file?

------------------------
Selecting by record name
------------------------

In the previous example, we used ``SeqIO.parse(...)`` to loop over the input
FASTA file. This means the output order will be dictated by the input sequence
file's order. What if you want the records in the specified order (regardless
of the order in the FASTA file)?

In this situation, you can't make a single for loop over the FASTA file. For
a tiny file you could load everything into memory (e.g. as a Python dictionary),
but that won't work on larger files. Instead, we can use Biopython's
``SeqIO.index(...)`` function which lets us treat a sequence file like a
Python dictionary:

.. sourcecode:: pycon

    >>> from Bio import SeqIO
    >>> filename = "PGSC_DM_v3.4_pep_representative.fasta"
    >>> fasta_index = SeqIO.index(filename, "fasta")
    >>> print(str(len(fasta_index)) + " records in " + filename)
    >>> "PGSC0003DMP400019313" in fasta_index
    True
    >>> record = fasta_index["PGSC0003DMP400019313"]
    >>> print(record)
    ID: PGSC0003DMP400019313
    Name: PGSC0003DMP400019313
    Description: PGSC0003DMP400019313 PGSC0003DMT400028369 Protein
    Number of features: 0
    Seq('MSKSLYLSLFFLSFVVALFGILPNVKGNILDDICPGSFFPPLCFQMLRNDPSVS...LK*', SingleLetterAlphabet())

*Excercise*: Write a new version of your ``count_fasta.py`` script using
``SeqIO.index(...)`` instead of ``SeqIO.parse(...)`` and a for loop.
Which is faster?

*Excercise*: Complete the following script (which I've called to use ``SeqIO.index(...)``
to make a FASTA file with records of interest *in the given order*:

.. sourcecode:: python

    from Bio import SeqIO
    wanted_ids = ["PGSC0003DMP400019313", "PGSC0003DMP400020381", "PGSC0003DMP400020972"]
    input_filename = "PGSC_DM_v3.4_pep_representative.fasta"
    output_filename = "wanted_potato_proteins_in_order.fasta"
    fasta_index = SeqIO.index(input_filename, "fasta")
    count = 0
    total = # Your code here, get total from fasta_index
    output_handle = open(output_filename, "w")
    for identifier in wanted_ids:
        # ...
        # Your code here, get the record for the identifier, and write it out
        # ...
    output_handle.close()
    print(str(count) + " records selected out of " + str(total))

I called this script ``filter_wanted_id_in_order.py`` and the output should be:

.. sourcecode:: console

    $ python filter_wanted_id_in_order.py
    3 records selected out of 39031


Now compare the outfile files from the two approaches:

.. sourcecode:: console

    $ grep "^>" wanted_potato_proteins.fasta
    >PGSC0003DMP400020381 PGSC0003DMT400029984 Protein
    >PGSC0003DMP400020972 PGSC0003DMT400030871 Protein
    >PGSC0003DMP400019313 PGSC0003DMT400028369 Protein
    $ grep "^>" wanted_potato_proteins_in_order.fasta 
    >PGSC0003DMP400019313 PGSC0003DMT400028369 Protein
    >PGSC0003DMP400020381 PGSC0003DMT400029984 Protein
    >PGSC0003DMP400020972 PGSC0003DMT400030871 Protein

The second file has the order specified in the Python list.
