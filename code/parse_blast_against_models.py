#!/usr/bin/env python


from pyphylogenomics import BLAST
import sys


blast_output = sys.argv[1].strip()
model_genome = sys.argv[2].strip()
output_file = sys.argv[3].strip()
species_name = sys.argv[4].strip()

BLAST.blastParser(blast_output, model_genome, output_file, species_name)
