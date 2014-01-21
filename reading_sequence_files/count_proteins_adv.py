#!/usr/bin/env python
import sys
from Bio import SeqIO

#Remember sys.argv[0] is the script itself
for filename in sys.argv[1:]:
    count = 0
    for record in SeqIO.parse(filename, "fasta"):
        count += 1
    print("There were " + str(count) + " records in file " + filename)
