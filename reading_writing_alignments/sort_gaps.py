from Bio import AlignIO

def count_gaps(record):
    """Counts number of gaps in record's sequence."""
    return record.seq.count("-")

filename = "PF08792_seed.sth"
alignment = AlignIO.read(filename, "stockholm")
alignment.sort(key=count_gaps)
print(alignment)
