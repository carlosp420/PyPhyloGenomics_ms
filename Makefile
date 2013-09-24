SRC = $(wildcard *.md)
PDFS = $(SRC:.md=.pdf)
DOCS = $(SRC:.md=.docx)


pdf: $(PDFS)

%.pdf: %.md refs.bib header.latex style/molbiolevol.csl
	pandoc --latex-engine=xelatex -s -S --template header.latex -f markdown -V geometry:margin=1in $< --bibliography=refs.bib --csl=style/molbiolevol.csl -o $@


docx: $(DOCS)

%.docx: %.md refs.bib style/molbiolevol.csl
	pandoc -f markdown -V geometry:margin=1in -t docx $< --bibliography=refs.bib --csl=style/molbiolevol.csl -o $@


####
# Do gene search
#
gene_search: data/pulled_seqs.fasta data/pulled_seqs_blastn_out.csv data/Bombyx_exons.fas blast_danaus blast_heliconius blast_manduca alignments/*.fasta

data/pulled_seqs.fasta: data/OrthoDB6_Arthropoda_tabtext.csv data/silkcds.fa code/start_gene_search.py
	python code/start_gene_search.py

data/pulled_seqs_blastn_out.csv: code/gene_search_blast1.py data/pulled_seqs.fasta data/silkgenome.fa
	python code/gene_search_blast1.py

data/Bombyx_exons.fas: code/gene_search_blast_filtering_exons.py data/pulled_seqs_blastn_out.csv data/pulled_seqs.fasta
	python code/gene_search_blast_filtering_exons.py

# validate against Danaus plexippus
blast_danaus: data/Danaus_exons.fasta

data/Bombyx_exons_blastn_out.csv: data/Bombyx_exons.fas data/Dp_genome_v2.fasta code/blast_against_models.py
	python code/blast_against_models.py data/Bombyx_exons.fas data/Dp_genome_v2.fasta

data/Danaus_exons.fasta: data/Bombyx_exons_blastn_out.csv data/Dp_genome_v2.fasta code/parse_blast_against_models.py
	python code/parse_blast_against_models.py data/Bombyx_exons_blastn_out.csv data/Dp_genome_v2.fasta data/Danaus_exons.fasta Danaus

# validate against Heliconius melpomene
blast_heliconius: data/Heliconius_exons.fasta
	
data/Heliconius_exons.fasta: code/blast.py code/parse_blast.py data/Bombyx_exons.fas data/Heliconius_genome.fa 
	rm -rf data/Bombyx_exons_blastn_out.csv
	python code/blast.py data/Bombyx_exons.fas data/Heliconius_genome.fa
	python code/parse_blast.py data/Bombyx_exons_blastn_out.csv data/Heliconius_genome.fa data/Heliconius_exons.fasta Heliconius

# validate against Manduca sexta
blast_manduca: data/Manduca_exons.fasta

data/Manduca_exons.fasta: code/blast.py code/parse_blast.py data/Bombyx_exons.fas data/Msex05162011.genome.fa
	rm -rf data/Bombyx_exons_blastn_out.csv
	python code/blast.py data/Bombyx_exons.fas data/Msex05162011.genome.fa
	python code/parse_blast.py data/Bombyx_exons_blastn_out.csv data/Msex05162011.genome.fa data/Manduca_exons.fasta Manduca
	rm -rf data/Bombyx_exons_blastn_out.csv


##
# align taxa exons using MUSCLE
alignments: alignments/*.fasta
	
alignments/*.fasta: code/do_alignment.py data/Bombyx_exons.fas data/Danaus_exons.fasta data/Heliconius_exons.fasta data/Manduca_exons.fasta
	python code/do_alignment.py


####
# Analysis NGS data
#
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

data/modified/wrk_ionfile_blastn_out.csv: code/separate_by_gene.py data/modified/wrk_ionfile.fasta data/genes_Bmori.fasta
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
	rm -rf alignments
	rm -rf data/*asnb
	rm -rf data/*.n*
	rm -rf data/*exons*
	rm -rf data/pulled_seqs.fasta

