#!/usr/bin/env python

import os;
from pyphylogenomics import BLAST


"""
Do a BLASTn of the sequences against the Bombyx mori genome. The input arguments
are your file containing the sequences for single-copy genes (pulled_seqs.fa) 
and your file with the genome of Bombyx mori which is in FASTA format (silkgenome.fa).
"""
BLAST.blastn('data/pulled_seqs.fasta', 'data/silkgenome.fa')


