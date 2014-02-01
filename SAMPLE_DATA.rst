=================
Sample Data Files
=================

Most of the examples use real biological data files. You could download them all
at the start, or gradually as needed.

Under Linux this is easily done at the command line with the ``wget`` tool. For Mac
OS X users, ``wget`` is not installed by default so in place of ``wget ftp://...`` or
``wget http://..`` please use ``curl -O ftp://...`` or ``curl -O http://..`` instead.

In the following command line examples ``$`` indicates the command line prompt, copy
and paste (or type) the text starting after this (e.g. ``wget ftp://...``).

---------------------
*Esherichia coli* K12
---------------------

We'll use the complete genome of this model bacteria in GenBank format, FASTA format,
plus FASTA files of the annotated genes and their protein sequences:

.. sourcecode:: console

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
the doubled monoploid *Solanum tuberosum* group Phureja clone DM1-3:

.. sourcecode::	console

    $ wget http://potato.plantbiology.msu.edu/data/PGSC_DM_v3.4_pep_representative.fasta.zip

For anyone working on Mac OS X, the ``wget`` command is not installed by default. As noted
above you can use ``curl -O http://...`` instead.

Once downloaded, decompress the ZIP file using the ``unzip`` command:

.. sourcecode:: console

    $ unzip PGSC_DM_v3.4_pep_representative.fasta.zip

--------------
Pfam Alignment
--------------

This example is a little different as by default wget and curl will name
the saved file something annoying like ```format?format=stockholm`` based
on the last part of the URL. We therefore set the desired output filename
explicitly.

On Linux at the command line using wget:

.. sourcecode:: console

    $ wget -O "PF08792_seed.sth" http://pfam.sanger.ac.uk/family/PF08792/alignment/seed/format?format=stockholm

On Mac OS X using curl you can set the saved filename as follows:

.. sourcecode:: console

    $ curl -o "PF08792_seed.sth" http://pfam.sanger.ac.uk/family/PF08792/alignment/seed/format?format=stockholm

Note the the output filename option is in upper case for wget, but
confusingly is lower case for curl.
