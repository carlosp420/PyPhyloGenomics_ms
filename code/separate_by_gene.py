#!/usr/bin/env python

# find reads matching target genes using BLAST
from pyphylogenomics import BLAST;

query_seqs = "data/modified/wrk_ionfile.fasta";
genome = "data/genes.fasta";
BLAST.blastn(query_seqs, genome); 

# output is a csv file in data/mofidied/wrk_ionfile_blastn_out.csv
