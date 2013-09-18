#!/usr/bin/env python

import os;
from pyphylogenomics import OrthoDB
from pyphylogenomics import BLAST
from pyphylogenomics import MUSCLE


"""
As stated before, we prefer long exons for each of the candidate genes ( > 300
nucleotides):
"""
exons = BLAST.getLargestExon("data/pulled_seqs_blastn_out.csv", E_value=0.001, ident=98, exon_len=300)


"""
Some small segments of sequences might be similar to non-homologous regions of
the genome. We will use the function eraseFalsePosi to keep those matches of
longest length:
"""
exons = BLAST.eraseFalsePosi(exons) # Drop presumable false positives.


"""
Ideally we want exons that are not too close to each other in the genome to
avoid gene linkage. So we will keep only those exons that are apart by 810
kilobases:
"""
exons = BLAST.wellSeparatedExons(exons) # Keep exons separated by > 810KB


"""
Finally we can use a function to save the obtained exons while making sure they
are in frame. We need to use as additional arguments the genome file and output
filename:
"""
BLAST.storeExonsInFrame(exons, "data/pulled_seqs.fasta", "data/Bombyx_exons.fas")


