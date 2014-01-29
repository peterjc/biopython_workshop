from Bio import SeqIO
wanted_ids = ["PGSC0003DMP400019313", "PGSC0003DMP400020381", "PGSC0003DMP400020972"]
input_filename = "PGSC_DM_v3.4_pep_representative.fasta"
output_filename = "wanted_potato_proteins_in_order.fasta"
fasta_index = SeqIO.index(input_filename, "fasta")
count = 0
total = len(fasta_index)
output_handle = open(output_filename, "w")
for identifier in wanted_ids:
    record = fasta_index[identifier]
    SeqIO.write(record, output_handle, "fasta")
    count = count + 1
output_handle.close()
print(str(count) + " records selected out of " + str(total))
