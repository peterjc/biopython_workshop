from Bio import SeqIO
record = SeqIO.read("NC_000913.gbk", "genbank")
output_handle = open("NC_000913_cds.fasta", "w")
count = 0
for feature in record.features:
    if feature.type == "CDS":
        count = count + 1
        feature_name = feature.qualifiers["locus_tag"][0]
        feature_seq = feature.extract(record.seq)
        # Simple FASTA output without line wrapping:
        output_handle.write(">" + feature_name + "\n" + str(feature_seq) + "\n")
output_handle.close()
print(str(count) + " CDS sequences extracted")
