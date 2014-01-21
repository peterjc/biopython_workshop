from Bio import SeqIO
#filename = "NC_000913.faa"
filename = "PGSC_DM_v3.4_pep_representative.fasta"
bad = 0
for record in SeqIO.parse(filename, "fasta"):
    if not record.seq.startswith("M"):
        bad = bad + 1
        print(record.id + " starts " + record.seq[0])
print("Found " + str(bad) + " records in " + filename + " which did not start with M")

