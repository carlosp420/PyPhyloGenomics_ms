pdf: MS.pdf

MS.pdf: MS.md refs.bib
	pandoc --latex-engine=xelatex -s -S --template header.latex -f markdown -V geometry:margin=1in MS.md --bibliography=refs.bib --csl=style/molbiolevol.csl -o MS.pdf


analysis: prepare_data separate_by_gene separate_by_gene_filter_out_table separate_by_index assembly

## Prepare raw NGS data (FASTQ file)
# - creates a FASTQ file with the quality format changed from Phred to Solexa
# - read IDs changed to numbers
# - FASTA file created from the FASTQ file
prepare_data: data/modified/wrk_ionfile.fasta data/modified/wrk_ionfile.fastq

data/modified/wrk_ionfile.fasta data/modified/wrk_ionfile.fastq: data/Bmori_run.fastq code/prepare_NGS_data.py
	python code/prepare_NGS_data.py data/Bmori_run.fastq


## Separate reads by gene using BLAST
separate_by_gene: data/modified/wrk_ionfile_blastn_out.csv

data/modified/wrk_ionfile_blastn_out.csv: code/separate_by_gene.py data/modified/wrk_ionfile.fasta data/genes.fasta data/genes_Bmori.fasta data/genes_Bmori.fasta
	python code/separate_by_gene.py


## filter out reads by gene
separate_by_gene_filter_out_table: output/gene_NSG-034_Bmori.fastq

output/gene_NSG-034_Bmori.fastq:	code/separate_by_gene_filter_out_table.py data/modified/wrk_ionfile_blastn_out.csv data/modified/wrk_ionfile.fastq
	python code/separate_by_gene_filter_out_table.py


## filter out reads by index
separate_by_index: output/index_IonADA_464_gene_NSG-034_Bmori.fastq

output/index_IonADA_464_gene_NSG-034_Bmori.fastq: output/gene_NSG-034_Bmori.fastq data/indexes.fasta
	python code/separate_by_index.py


# assembly
assembly: output/index_IonADA_464_gene_NSG-034_Bmori.fastq_assembled.fasta

output/index_IonADA_464_gene_NSG-034_Bmori.fastq_assembled.fasta: code/assembly_all.py output/index_IonADA_464_gene_NSG-034_Bmori.fastq code/do_quality_control.py code/assembly_velvet2.sh code/do_me_blast.py 
	python code/assembly_all.py




clean: 
	rm -rf data/modified
	rm -rf output

