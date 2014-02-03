from Bio import SeqIO
record = SeqIO.read("NC_000913.gbk", "genbank")
print("Total length of genome is " + str(len(record)))
totals = dict()
for feature in record.features:
    if feature.type in totals:
        totals[feature.type] = totals[feature.type] + len(feature)
    else:
        #First time to see this feature type
        totals[feature.type] = 1
for f_type in totals:
    print("Total length of " + f_type + " is " + str(totals[f_type]))
