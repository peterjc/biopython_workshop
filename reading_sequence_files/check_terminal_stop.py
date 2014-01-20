from Bio import SeqIO
#filename = "NC_000913.faa"
filename = "PGSC_DM_v3.4_pep_representative.fasta"
no_star = 0
with_star = 0
print("Checking %s for terminal stop codons" % filename)
for record in SeqIO.parse(filename, "fasta"):
    if record.seq.endswith("*"):
        with_star += 1
    else:
        no_star += 1
print("%i with terminal stop, %i without terminal stop" % (with_star, no_star))

