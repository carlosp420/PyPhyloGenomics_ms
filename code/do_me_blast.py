#!/usr/bin/env python

import sys
import subprocess

# does a quick blast

if len(sys.argv) < 2:
    print "Error, this will blast a query seq aginst our expected NGS genes"
    sys.exit()

query = sys.argv[1].strip()
genome = "data/genes_Bmori.fasta"

cmd = 'blastn -query ' + query + ' -db ' + genome + ' -task blastn '
cmd += '-evalue 0.0001 -out ' + query + "_out.csv" + ' -num_threads 1 -outfmt 10'
p = subprocess.check_output(cmd, shell=True)
print cmd
print p

table = open(query + "_out.csv", "r")
for line in table:
    line = line.strip()
    line = line.split(",")
    output = line[0][:28] + "\t" + line[1] + "\t" + "mistmatc=" + line[4] + "\t"
    output += "gaps=" + line[5]
    print output
