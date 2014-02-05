from Bio import SeqIO
filename = "NC_000913.faa"
count = 0
total = 0
for record in SeqIO.parse(filename, "fasta"):
    count = count + 1
    # Can use len(record) as shortcut for len(record.seq)
    total = total + len(record)
print(str(count) + " records, total length " +str(total) + " in file " + filename)
