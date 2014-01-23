from Bio import SeqIO
input_filename = "PGSC_DM_v3.4_pep_representative.fasta"
output_filename = "PGSC_DM_v3.4_pep_rep_no_stars.fasta"
output_handle = open(output_filename, "w")
for record in SeqIO.parse(input_filename, "fasta"):
    if record.seq.endswith("*"):
        record = record[:-1] # remove last letter (the star)
    SeqIO.write(record,output_handle, "fasta")
output_handle.close()
