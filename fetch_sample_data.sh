#!/usr/bin/env bash
# Set bash strict mode (fail on errors, undefined variables, and via pipes)
set -euo pipefail

if [ -x "$(command -v wget)" ]; then
  # e.g. Linux
  echo "Downloading files using wget"
  FETCH="wget"
elif [ -x "$(command -v curl)" ]; then
  # e.g. Max OS X
  echo "Downloading files using curl"
  FETCH="curl -O"
else
  echo "ERROR: Failed to find wget or curl"
  exit 1
fi

echo "=============================================="
echo "Fetching Escherichia coli K-12 files from NCBI"
echo "=============================================="

# Note: These files are no longer being updated...
$FETCH ftp://ftp.ncbi.nlm.nih.gov/genomes/archive/old_refseq/Bacteria/Escherichia_coli_K_12_substr__MG1655_uid57779/NC_000913.gbk
$FETCH ftp://ftp.ncbi.nlm.nih.gov/genomes/archive/old_refseq/Bacteria/Escherichia_coli_K_12_substr__MG1655_uid57779/NC_000913.fna
$FETCH ftp://ftp.ncbi.nlm.nih.gov/genomes/archive/old_refseq/Bacteria/Escherichia_coli_K_12_substr__MG1655_uid57779/NC_000913.ffn
$FETCH ftp://ftp.ncbi.nlm.nih.gov/genomes/archive/old_refseq/Bacteria/Escherichia_coli_K_12_substr__MG1655_uid57779/NC_000913.faa

echo "=========================================================="
echo "Fetching proteins from Potato Genome Sequencing Consortium"
echo "=========================================================="

$FETCH http://potato.plantbiology.msu.edu/data/PGSC_DM_v3.4_pep_representative.fasta.zip
unzip -o PGSC_DM_v3.4_pep_representative.fasta.zip

echo "===================================="
echo "Fetching PF08792 alignment from PFAM"
echo "===================================="

if [ -x "$(command -v wget)" ]; then
  # Note: Using -O to set the filename explicitly as default is format?format=stockholm
  wget -O "PF08792_seed.sth" http://pfam.sanger.ac.uk/family/PF08792/alignment/seed/format?format=stockholm
elif [ -x "$(command -v curl)" ]; then
  # Note: Mac OS alternative needs -L due to link redirect:
  curl -o "PF08792_seed.sth" -L http://pfam.sanger.ac.uk/family/PF08792/alignment/seed/format?format=stockholm
else
  echo "ERROR: Failed to find wget or curl"
  exit 1
fi
