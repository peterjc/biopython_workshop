from Bio import SeqIO
filename = "NC_000913.faa"
#filename = "PGSC_DM_v3.4_pep_representative.fasta"
contains_star = 0
ends_with_star = 0
print("Checking " + filename + " for terminal stop codons")
for record in SeqIO.parse(filename, "fasta"):
    if record.seq.count("*"):
        contains_star += 1
    if record.seq.endswith("*"):
        ends_with_star += 1
print(str(contains_star) + " records with * in them")
print(str(ends_with_star) + " with * at the end")


