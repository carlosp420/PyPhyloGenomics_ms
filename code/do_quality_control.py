import sys;
import subprocess;
import shlex;



if len(sys.argv) < 2:
	print "Error. Enter FASTQ file to process";
	sys.exit(0);

fastqFile = sys.argv[1].strip();

#
#print "\nConverting quality data from phred to solexa";
#cmd = ["convert_phred_2_solexa.py", fastqFile, "tmp"];
cmd = ["cp", fastqFile, "tmp"]
try:
    subprocess.check_call(cmd);
    print subprocess.check_output("grep -c '^@' tmp", shell=True).strip() + "\t: Original number of reads.\n" 
except:
    print ""

# 
print "Removing indexes: fastx_trimmer -f 9"
cmd = "fastx_trimmer -f 9 -i tmp -o filter1.fastq";
try: 
    subprocess.check_call(cmd, shell=True)
except:
    print ""

#
print "fastq_quality_filter -q 20 -p 70";
cmd = "fastq_quality_filter -q 20 -p 70 -i filter1.fastq -o filter2.fastq";
try:
    subprocess.check_call(cmd, shell=True);
    print subprocess.check_output("grep -c '^@' filter2.fastq", shell=True).strip() + "\t: filter2 number of reads.\n" 
except:
    print ""


#
print "fastq_quality_trimmer -t 20 -l 20";
cmd = "fastq_quality_trimmer -t 20 -l 20 -i filter2.fastq -o filter3.fastq";
try:
    subprocess.check_call(cmd, shell=True);
    print subprocess.check_output("grep -c '^@' filter3.fastq", shell=True).strip() + "\t: filter3 number of reads.\n" 
except:
    print ""



print "\nFile to process: filter3.fastq\nend;";
