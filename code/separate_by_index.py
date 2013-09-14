#!/usr/bin/env python

import glob;
import os;
from pyphylogenomics import NGS;
from Bio import SeqIO;
import pp;
import sys;

os.system("t set active prim1atutu");
os.system("t update '@carlosp420 starting separation by indexes of run'");

# find reads matching our indexes and do separation
# we will take a list of indexes corresponding to individuals 
# and use it to separate the gene bins 
index_list = "data/indexes.fasta";
folder = "output";
levenshtein_distance = 0;

# progressbar
progressbar_width = 20;
sys.stdout.write("Progress: [%s]" % (" " * progressbar_width))
sys.stdout.flush();
sys.stdout.write("\b" * (progressbar_width + 1))

ppservers = ("*",)
job_server = pp.Server(ppservers=ppservers, secret="123")
jobs = []

for gene_file in glob.glob(os.path.join("output", "gene*fastq")):
    jobs.append(job_server.submit(NGS.separate_by_index, (gene_file, index_list, folder, levenshtein_distance),(),("re","pyphylogenomics","NGS",)));

for job in jobs:
    sys.stdout.write("#")
    sys.stdout.flush();
    job()

sys.stdout.write("\n")
job_server.print_stats();


os.system("t set active prim1atutu");
os.system("t update '@carlosp420 finished separation by indexes of run'");
