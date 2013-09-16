#!/usr/bin/env python

import subprocess
import sys
from pyphylogenomics import NGS
import glob


""" This will try to assembly all from a list of files.
will log results to be parsed later. Try to find Bmori
sequences"""

kmers = [31, 29, 27, 25]


log = open("log", "a")
for file in glob.glob("output/index*"):
    file = file.strip()

    # do assembly using NGS
    fastq_file = file
    outfile = file + "_assembled.fasta"
    index_length = 8
    min_quality = 20
    percentage = 70
    min_length = 50


    log.write(str(file) + "\n")

    cmd = "python code/do_quality_control.py " + file;
    subprocess.check_call(cmd, shell=True)

    for i in kmers:
        cmd = "bash code/assembly_velvet2.sh filter3.fastq " + str(i)
        subprocess.check_call(cmd, shell=True)

        cmd = "python code/do_me_blast.py test/contigs.fa"
        subprocess.check_call(cmd, shell=True)

        cmd = "cat test/contigs.fa >> " + outfile
        subprocess.check_call(cmd, shell=True)

        table = open("test/contigs.fa_out.csv", "r")
        for line in table:
            line = line.strip()
            line = line.split(",")
            output = line[0][:28] + "\t" + line[1] + "\t" + "mistmatc=" + line[4] + "\t"
            output += "gaps=" + line[5]
            log.write(output + "\n")

subprocess.check_call(cmd, shell=True)
log.close()
