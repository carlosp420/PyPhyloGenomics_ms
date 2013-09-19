#!/usr/bin/env python



from pyphylogenomics import MUSCLE

files = ['data/Bombyx_exons.fas', 'data/Danaus_exons.fasta','data/Heliconius_exons.fasta','data/Manduca_exons.fasta']
MUSCLE.batchAlignment(files)
