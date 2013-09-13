#!/usr/bin/env python

from pyphylogenomics import NGS

ionfile = "data/Carlos_feb_2013_ionrun.fastq"
index_length = 8

NGS.prepare_data(ionfile, index_length)
