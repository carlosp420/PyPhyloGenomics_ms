#!/usr/bin/env python

from pyphylogenomics import NGS;

blast_table = "data/modified/wrk_ionfile_blastn_out.csv"
ion_file = "data/modified/wrk_ionfile.fastq";

NGS.parse_blast_results(blast_table, ion_file);



