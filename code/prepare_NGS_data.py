#!/usr/bin/env python

from pyphylogenomics import NGS
import sys

if len(sys.argv) < 2:
    print "Error, need to enter ionfile to process"
    print "cmd ionfile.fastq"
    sys.exit()

ionfile = sys.argv[1].strip()
index_length = 8

NGS.prepare_data(ionfile, index_length)
