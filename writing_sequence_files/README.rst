====================================
Writing Sequences Files in Biopython
====================================

The `previous section <../reading_sequence_files/README.rst>`_ talked
about reading sequence files in Biopython using the ``SeqIO.parse(...)``
function. Now we'll talk about writing sequence files using the sister
function ``SeqIO.write(...)``.

The more gently paced `Biopython Tutorial and Cookbook
<http://biopython.org/DIST/docs/tutorial/Tutorial.html>`_
(`PDF <http://biopython.org/DIST/docs/tutorial/Tutorial.pdf>`_)
first covers creating your own records (``SeqRecord`` objects) and
then how to write them out. We're going to skip that and work with
read-made ``SeqRecord`` objects from existing sequence files loaded
with ``SeqIO.parse(...)``. Let's start with something really simple...

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

Also have a look at the output file:

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

**Warning**: The output will overright any pre-existing file of the same name.

**Advanced Exercise**: Modify this to add command line parsing to take
the input and output filenames as arguments.

The ``SeqIO.convert(...)`` function is effectively a shortcut for calling
``SeqIO.parse(...)`` on the input, and giving this to ``SeqIO.write(...)``
for the output. Here's how you'd do this explictly:

.. sourcecode::	python

    from Bio import SeqIO
    input_filename = "NC_000913.gbk"
    output_filename = "NC_000913_converted.fasta"
    records_iterator = SeqIO.parse(input_filename, "gb")
    count = SeqIO.write(records_iterator, output_filename, "fasta")    
    print(str(count) + " records converted")

Previously we'd always used the results from ``SeqIO.parse(...)`` in a for
loop - but here the for loop happens inside the ``SeqIO.write(...)`` function.

-----------------------
Writing with a for-loop
-----------------------

TODO

-------------------------
Filtering a sequence file
-------------------------

TODO

