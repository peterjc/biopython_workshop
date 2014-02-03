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

    >>> my_gene = record.features[3]
    >>> print(my_gene)
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
The `Biopython Tutorial & Cookbook <http://biopython.org/DIST/docs/tutorial/Tutorial.html>`_
(`PDF <http://biopython.org/DIST/docs/tutorial/Tutorial.pdf>`_) goes into
more detail about this - we're going to focus on extracting the sequnce
associated with a location:

    >>> print(my_gene.location)
    [336:2799](+)
    >>> print(my_gene.location.start)
    336
    >>> print(my_gene.location.end)
    2799
    >>> print(my_gene.location.strand)
    1

Recall in the GenBank file this simple location was ``337..2799``, yet
in Biopython this has become a start value of ``336`` and ``2799`` as the
end. The reason for this is to match how Python counting work, in particular
string slicing:

.. sourcecode:: pycon

    >>> gene_seq = record.seq[336:2799]
    >>> len(gene_seq)
    2463
    >>> print(gene_seq)
    ...

This was a very simple location on the forward strand, if it had been on
the reverse strand you'd need to take the reverse-complement. Also if the
location had been a more complicated compound location like a *join* (used
for eukaryotic genes where the CDS is made up of several exons), then the
location would have-sub parts to consider.

All these complications are taken care of for you via the ``.extract(...)``
method which takes the full length parent record's sequence as an argument:

.. sourcecode:: pycon

    >>> gene_seq = my_gene.extract(record.seq)
    >>> len(gene_seq)
    2463
    >>> print(gene_seq)
    ...

Note you can also take the length of the feature directly (or the feature's
``.location``) and get the same answer:

.. sourcecode:: pycon

    >>> len(my_gene)
    2463

This example loops over all the features looking for gene records, and
calculates their total length:

.. sourcecode:: python

    from Bio import SeqIO
    record = SeqIO.read("NC_000913.gbk", "genbank")
    total = 0
    for feature in record.features:
        if feature.type == "gene":
            total = total + len(feature)
    print("Total length of all genes is " + str(total))

.. sourcecode:: console

    $ python total_gene_lengths.py
    Total length of genome is 4641652
    Total length of all genes is 4137243

**Exercise**: Give a separate count for each feature type. Use a dictionary
where the keys are the feature type (e.g. "gene" and "CDS") and the values
are the count for that type.

**Discussion**: What proportion of the genome is annotated as gene coding?
What assumptions does this estimate 89% make:

.. sourcecode:: pycon

    >>> 4137243 * 100.0 / 4641652
    89.13298541122859

**Exercise**: Extend the previous script to also count the number of
features of each type, and report this and the average length of that
feature type. e.g.

.. sourcecode:: console

    $ python total_feature_lengths.py
    Total length of genome is 4641652
    misc_feature
     - total number: 13686
     - total length: 6136082
     - average length: 448.347362268
    mobile_element
     - total number: 49
     - total length: 50131
     - average length: 1023.08163265
    ...

**Discussion**: What proportion of the genome is annotated with *misc_feature*?
Does this simple calculation give a meaningful answer?

.. sourcecode:: pycon

    >>> 6136082 * 100.0 / 4641652
    132.19608018869144

This is an alternative approach, using some more advanced bits of Python like
the set datatype, and the concept of iterating over the bases within a feature:

.. sourcecode:: pycon

    >>> from Bio import SeqIO
    >>> record = SeqIO.read("NC_000913.gbk", "genbank")
    >>> bases = set()
    >>> for feature in record.features:
    ...     if feature.type == "misc_feature":
    ...         bases.update(feature.location)
    ... 
    >>> print(len(bases) * 100.0 / len(record))
    80.69355479471533

**Exercise**: Without worrying to much about how it works, modify this example
to count the number of bases in the *gene* features.

.. sourcecode:: console

    $ python bases_in_genes.py 
    88.9494085295

**Discussion**: Compare this calculation (88.95%) to one earlier (89.13%).
Which is a better estimate of the proportion of the genome which encodes genes?
When might these methods give very different answers? Any virologists in the group?
How should this be defined given that any single base may be in more than one gene?
