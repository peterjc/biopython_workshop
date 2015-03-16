#!/usr/bin/env bash
# Set bash strict mode (fail on errors, undefined variables, and via pipes)
set -euo pipefail

echo "=============================================="
echo "Fetching Escherichia coli K-12 files from NCBI"
echo "=============================================="

wget ftp://ftp.ncbi.nlm.nih.gov/genomes/Bacteria/Escherichia_coli_K_12_substr__MG1655_uid57779/NC_000913.gbk
wget ftp://ftp.ncbi.nlm.nih.gov/genomes/Bacteria/Escherichia_coli_K_12_substr__MG1655_uid57779/NC_000913.fna
wget ftp://ftp.ncbi.nlm.nih.gov/genomes/Bacteria/Escherichia_coli_K_12_substr__MG1655_uid57779/NC_000913.ffn
wget ftp://ftp.ncbi.nlm.nih.gov/genomes/Bacteria/Escherichia_coli_K_12_substr__MG1655_uid57779/NC_000913.faa

echo "=========================================================="
echo "Fetching proteins from Potato Genome Sequencing Consortium"
echo "=========================================================="

wget http://potato.plantbiology.msu.edu/data/PGSC_DM_v3.4_pep_representative.fasta.zip
unzip PGSC_DM_v3.4_pep_representative.fasta.zip

echo "===================================="
echo "Fetching PF08792 alignment from PFAM"
echo "===================================="

wget -O "PF08792_seed.sth" http://pfam.sanger.ac.uk/family/PF08792/alignment/seed/format?format=stockholm
# Note: Mac OS alternative needs -L due to link redirect:
# curl -o "PF08792_seed.sth" -L http://pfam.sanger.ac.uk/family/PF08792/alignment/seed/format?format=stockholm
