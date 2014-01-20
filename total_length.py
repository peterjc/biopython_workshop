from Bio import SeqIO
filename = "NC_000913.faa"
count = 0
total = 0
for record in SeqIO.parse(filename, "fasta"):
    count += 1
    total += len(record)
print("%i records, total length %i" % (count, total))
