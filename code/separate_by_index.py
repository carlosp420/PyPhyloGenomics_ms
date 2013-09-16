#!/usr/bin/env python

import glob;
import os;
from pyphylogenomics import NGS;
from Bio import SeqIO;
import pp;
import sys;


# find reads matching our indexes and do separation
# we will take a list of indexes corresponding to individuals 
# and use it to separate the gene bins 
index_list = "data/indexes.fasta";
folder = "output";
levenshtein_distance = 0;

ppservers = ("*",)
job_server = pp.Server(ppservers=ppservers, secret="123")
jobs = []

for gene_file in glob.glob(os.path.join("output", "gene*fastq")):
    jobs.append(job_server.submit(NGS.separate_by_index, (gene_file, index_list, folder, levenshtein_distance),(),("re",)));

for job in jobs:
    job()
    print "\n"

job_server.print_stats();

