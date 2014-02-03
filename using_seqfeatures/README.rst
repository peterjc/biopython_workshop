==============================
Working with Sequence Features
==============================

This picks up from the end of the section on `reading sequence files
<../reading_sequence_files/README.rst>`_, but looks at the feature
annotation included in some file formats like EMBL or GenBank.

Most of the time GenBank files contain a single record for a single
chromosome or plasmid, so we'll generally use the ``SeqIO.read(...)``
function. Remember the second argument is the file format, so if we
start from the code to read in a FASTA file:

.. sourcecode:: pycon

    >>> from Bio import SeqIO
    >>> record = SeqIO.read("NC_000913.fna", "fasta")
    >>> print(record.id)
    gi|556503834|ref|NC_000913.3|
    >>> print(len(record))
    4641652
    >>> print(len(record.features))
    0

Now switch the filename and the format:

.. sourcecode::	pycon

    >>> from Bio import SeqIO
    >>> record = SeqIO.read("NC_000913.gbk", "genbank")
    >>> print(record.id)
    NC_000913.3
    >>> print(len(record))
    4641652
    >>> print(len(record.features))
    23086

So what is this new ``.features`` thing? It is a Python list, containing
a Biopython ``SeqFeature`` object for each feature in the GenBank file.
For instance,

.. sourcecode:: pycon

    >>> print(record.features[3])
    type: gene
    location: [336:2799](+)
    qualifiers: 
        Key: db_xref, Value: ['EcoGene:EG10998', 'GeneID:945803']
        Key: gene, Value: ['thrA']
        Key: gene_synonym, Value: ['ECK0002; Hs; JW0001; thrA1; thrA2; thrD']
        Key: locus_tag, Value: ['b0002']

Doing a print like this tries to give a human readable display. There
are three key properties, ``.type`` which is a string like ``gene``
or ``CDS``, ``.location`` which describes where on the genome this
feature is, and ``.qualifiers`` which is a Python dictionary full of
all the annotation for the feature (things like gene identifiers).

This is what this gene looks like in the raw GenBank file::

     gene            337..2799
                     /gene="thrA"
                     /locus_tag="b0002"
                     /gene_synonym="ECK0002; Hs; JW0001; thrA1; thrA2; thrD"
                     /db_xref="EcoGene:EG10998"
                     /db_xref="GeneID:945803"

Hopefully it is fairly clear how this maps to the ``SeqFeature`` structure.
