from __future__ import division
# (needed under Python 2 for sensible division)

from Bio import SeqIO
record = SeqIO.read("NC_000913.gbk", "genbank")
print("Total length of genome is " + str(len(record)))
totals = dict()
counts = dict()
for feature in record.features:
    if feature.type in totals:
        totals[feature.type] = totals[feature.type] + len(feature)
        counts[feature.type] = counts[feature.type] + 1
    else:
        #First time to see this feature type
        totals[feature.type] = 1
        counts[feature.type] = 1
for f_type in totals:
    print(f_type)
    print(" - total number: " + str(counts[f_type]))
    print(" - total length: " + str(totals[f_type]))
    ave_len = totals[f_type] / counts[f_type]
    print(" - average length: " + str(ave_len))
