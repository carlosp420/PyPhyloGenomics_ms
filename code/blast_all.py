#!/usr/bin/env python

import subprocess
import sys
from pyphylogenomics import NGS
import glob


""" This will try to assembly all from a list of files.
will log results to be parsed later. Try to find Bmori
sequences"""


log = open("log", "a")
for file in glob.glob("output/index*assembled*"):
    file = file.strip()

    log.write(str(file) + "\n")

    cmd = "python code/do_me_blast.py " + file 
    subprocess.check_call(cmd, shell=True)

    blast_out = file + "_out.csv"
    print blast_out
    table = open(blast_out, "r")
    for line in table:
        line = line.strip()
        line = line.split(",")
        output = line[0][:28] + "\t" + line[1] + "\t" + "mistmatc=" + line[4] + "\t"
        output += "gaps=" + line[5]
        log.write(output + "\n")

log.close()
