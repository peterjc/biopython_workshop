from Bio import SeqIO
filename = "NC_000913.faa"
for record in SeqIO.parse(filename, "fasta"):
    start_seq = record.seq[:10] # first 10 letters
    end_seq = record.seq[-10:] # last 10 letters
    print(record.id + " " + start_seq + "..." + end_seq)
