from Bio import SeqIO
input_filename = "PGSC_DM_v3.4_pep_representative.fasta"
output_filename = "PGSC_DM_v3.4_pep_rep_no_stars.fasta"
output_handle = open(output_filename, "w")
for record in SeqIO.parse(input_filename, "fasta"):
    cut_record = record[:-1] # remove last letter
    SeqIO.write(cut_record, output_handle, "fasta")
output_handle.close()
