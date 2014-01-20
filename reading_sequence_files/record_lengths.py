from Bio import SeqIO
filename = "NC_000913.faa"
for record in SeqIO.parse(filename, "fasta"):
    print("Record %s, length %i" % (record.id, len(record)))
