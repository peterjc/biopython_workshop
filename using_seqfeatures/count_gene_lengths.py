from Bio import SeqIO
record = SeqIO.read("NC_000913.gbk", "genbank")
print("Total length of genome is " + str(len(record)))
total = 0
for feature in record.features:
    if feature.type == "gene":
        total = total + len(feature)
print("Total length of all genes is " + str(total))
