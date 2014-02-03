from Bio import SeqIO
record = SeqIO.read("NC_000913.gbk", "genbank")
bases = set() # Python's built in set datatype
for feature in record.features:
    if feature.type == "gene":
        # This adds all the possible base coordinates
        # within the feature location to the set. Try
        # print(list(feature.location)) on a gene...
        bases.update(feature.location)
# The Python set doesn't store duplicates, so len(bases)
# is the number of unique bases in at least one gene.
print(len(bases) * 100.0 / len(record))
