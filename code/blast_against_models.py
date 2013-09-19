#!/usr/bin/env python


from pyphylogenomics import BLAST
import sys


exons = sys.argv[1].strip()
genome = sys.argv[2].strip()

BLAST.blastn(exons, genome)
