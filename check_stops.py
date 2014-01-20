from Bio import SeqIO
filename = "NC_000913.faa"
#filename = "PGSC_DM_v3.4_pep_representative.fasta"
contains_star = 0
ends_with_star = 0
print("Checking %s for terminal stop codons" % filename)
for record in SeqIO.parse(filename, "fasta"):
    if record.seq.count("*"):
        contains_star += 1
    if record.seq.endswith("*"):
        ends_with_star += 1
print("%i records with * in them" % contains_star)
print("%i with * at the end" % ends_with_star)


