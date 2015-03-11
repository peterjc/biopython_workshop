from __future__ import division
from Bio import AlignIO

filename = "PF08792_seed.sth"
alignment = AlignIO.read(filename, "stockholm")
gaps = 0
for record in alignment:
    gaps = gaps + record.seq.count("-")
count = len(alignment)  # number of records
print(filename + " had " + str(count) + " records,")
print("Total gaps " + str(gaps) + ", average per record " + str(gaps / count))
