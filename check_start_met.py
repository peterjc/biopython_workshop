from Bio import SeqIO
#filename = "NC_000913.faa"
filename = "PGSC_DM_v3.4_pep_representative.fasta"
bad = 0
for record in SeqIO.parse(filename, "fasta"):
    if not record.seq.startswith("M"):
        bad += 1
        print("%s starts %s" % (record.id, record.seq[0]))
print("Found %i records in %s which did not start with M" % (bad, filename))

