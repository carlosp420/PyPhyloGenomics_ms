#!/usr/bin/env python

import glob;
import os;
from pyphylogenomics import NGS;


# find reads matching our indexes and do separation
# we will take a list of indexes corresponding to individuals 
# and use it to separate the gene bins 
index_list = "data/indexes.fasta";
folder = "output";
levenshtein_distance = 0;
for gene_file in glob.glob(os.path.join("output", "gene*fastq")):
    NGS.separate_by_index(gene_file, index_list, folder, levenshtein_distance);
