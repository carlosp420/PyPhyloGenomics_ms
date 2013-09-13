pdf: MS.pdf

MS.pdf: MS.md refs.bib
	pandoc --latex-engine=xelatex -s -S --template header.latex -f markdown -V geometry:margin=1in MS.md --bibliography=refs.bib --csl=style/molbiolevol.csl -o MS.pdf


## Prepare raw NGS data (FASTQ file)
# - creates a FASTQ file with the quality format changed from Phred to Solexa
# - read IDs changed to numbers
# - FASTA file created from the FASTQ file
prepare_data: data/modified/wrk_ionfile.fasta data/modified/wrk_ionfile.fastq

data/modified/wrk_ionfile.fasta data/modified/wrk_ionfile.fastq: data/Carlos_feb_2013_ionrun.fastq code/prepare_NGS_data.py
	python code/prepare_NGS_data.py


## Separate reads by gene using BLAST
separate_by_gene: data/modified/wrk_ionfile_blastn_out.csv

data/modified/wrk_ionfile_blastn_out.csv: code/separate_by_gene.py data/modified/wrk_ionfile.fasta data/genes.fasta
	python code/separate_by_gene.py

separate_by_gene_filter_out_table: code/separate_by_gene_filter_out_table.py data/modified/wrk_ionfile_blastn_out.csv data/modified/wrk_ionfile.fastq
