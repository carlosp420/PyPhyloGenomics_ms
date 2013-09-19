### Article

## PyPhyloGenomics: toolkit and protocol for developing phylogenetic markers in novel species for Next Generation Sequence data
Carlos Peña^*,1^; Victor Solis^2^; Pável F. Matos-Maraví^3^; Chris Wheat^4^

^1^Laboratory of Genetics, Department of Biology, University of Turku, Turku, Finland

^2^

^3^School of Biological Sciences, University of South Bohemia and Institute of Entomology, Biology Centre AS CR, Ceske Budejovice, Czech Republic

^4^Population Genetics, Department of Zoology, Stockholm University, Stockholm, Sweden

***Corresponding author:** Carlos Peña, E-mail: <mycalesis@gmail.com>

# Abstract


# Introduction
Next Generation Sequencing (NGS) is considered a quantum leap in DNA sequencing
techniques [@loman2012].
The sequencing output of NGS technologies is around 30 gigabases of DNA in one single
run [@reis2009] whereas the traditional Sanger method [@sanger1977] can only generate
\~1,000 bp per specimen using the old capillary-based technology.
The higher yield of NGS is achieved by using massively parallel sequencing of PCR
products based on DNA synthesis of clonal clusters on surfaces such as micron-scale
beads or planar flowcell slides [@shendure2008].
As a result, millions of copies of sequences (reads) are produced from the DNA
templates.

Research in phylogenomics can be accelerated by using NGS due to the ease to obtain
DNA data at massive scale. Moreover, targeted sequencing of numerous loci of interest
[@ekblom2010] is quicker and cheaper using NGS than the Sanger method. Thus, it is
possible to dramatically increase the throughput of most common phylogenomic studies
[@wahlberg2008; @regier2013], which use datasets of only 12 to 19 loci.

Some studies have used NGS techniques to sequence miRNAs in phylogenomic analyses 
of the high level relationships in Panarthropoda [@campbell2011].
miRNAs are nonprotein coding RNAs of small length involved in DNA transcription and
gene regulation. Nonetheless, these molecules are not easy to sequence from genomic
DNA as miRNAs are processed in the cell and shortened to \~22 base pair sequences
[@wienholds2005].

Suitable molecular markers or candidate genes for phylogenetic inference are
orthologs, single copy genes because those share a common ancestor during
their evolutionary history [@chiu2006] and can be considered homologous
structures useful for comparative systematics.
Gene duplication is a common phenomenon in animals and plants [@duarte2010]
producing paralog genes with a degree of similarity depending on the time of
divergence since duplication. Paralogs are problematic for phylogenetic inference
because they can obscure phylogenetic signals and true species common ancestry
[@sanderson2002; @fares2005].

@wahlberg2008 obtained candidate genes for Lepidoptera phylogenomics by identifying
single copy orthologous genes of *Bombyx mori* from EST libraries. They searched
for EST sequences in the *Bombyx mori* genome in order to identify suitable exons. These
exon sequences were compared against EST libraries of related Lepidoptera species in
order to obtain homologous sequences for primer design. However, this method depends
on the availability of a reference genome to discard small exons interrupted by long
introns and the access to other EST sequences which are single reads of cDNA that might
contain numerous errors and are prone to artefacts [@parkinson2002].

@regier2013 obtained nuclear gene sequences from mRNA by performing reverse
transcription and PCR amplification [@regier2007]. mRNAs are molecules transcribed
from genomic DNA that have had introns spliced and exons joined.  Therefore,
sequencing these genes from genomic DNA for other species would be
troublesome due to the likely appearance of introns. Introns are sequences present
in eukaryotic genes that are discarded during the process of protein synthesis 
[@page1998] and can vary widely in size among different species [@carvalho1999].
Thus, it might be difficult to amplify DNA fragments and assess homology for base
pair positions if the sequences vary significantly in length among the studied species.
However, introns have been useful in other phylogenetic studies of certain organisms
at lower taxonomical level due to the higher amount of character variation
[e.g. @prychitko1997; @fujita2004].

Nuclear protein coding loci (NPCL) are the preferred markers in phylogenetic
inference due to appropiate mutation rates, effortless alignment of sequences and
recognizable sequences of paralogs [@townsend2008].
Moreover, genomic DNA can be used for sequencing NPCL, which has several advantages:
(i) genomic DNA does not degrade so quickly as RNA; (ii) it is simpler to preserve
in the field; (iii) it can be sequenced even from dry material (for example museum
specimens); and (iv) it is the most commonly used DNA in molecular systematics 
[@wahlberg2008].

@townsend2008 found candidate protein coding genes by BLASTing the genomes of *Fugu
rubripes* (pufferfish) and *Homo sapiens*. The shared NPCL were compared to the
genomes of other species in order to assess exon limits, align homologous sequences
and design primers. Paralog genes were identified as those form the *Fugu* genome
that matched more than one *Homo* gene.
 

Accordingly, a high-throughput method is needed to find candidate genes that can be
easily sequenced from genomic DNA across several non-model organisms.
One strategy to fulfill this goal is to compare genomic sequences of model
species and identify conserved regions to identify suitable genes that can be
sequenced in novel species from simple extractions of genomic DNA. 

In this paper, we describe a protocol for finding genes from genomic DNA that are
suitable for phylogenomic studies. 
We describe the software package ``PyPhyloGenomics``, written in the Python
language, that includes bioinformatic tools useful for automated gene finding,
primer design and NGS data analysis. We have used this software to find homologous
exons across genomes from several model organisms.
Our software also includes tools to filter output reads from NGS and assembling
sequences for each specimen.


## The ``PyPhyloGenomics`` package
The stable release of ``PyPhyloGenomics`` is available from the Python Package Index
(<https://pypi.python.org/pypi/PyPhyloGenomics>) for direct installation of the most
recent version using ``pip`` (a Python package installer). 
This is an open source project and the development versions are available from
github (<https://github.com/carlosp420/PyPhyloGenomics>). The full documentation and
user guide are available from the github pages 
(<http://carlosp420.github.io/PyPhyloGenomics/>).
``PyPhyloGenomics`` is conceived as a workflow using its four modules. Selection of
orthologous genes using the module ``OrthoDB``; search of genes in a set of
predicted genes from a model organism, extraction of genomic sequences for candidate
genes from the model organisms, and validation of genes across genomes of other
model organisms using the module ``BLAST``; alignment and primer design from genomic
sequences for candidate genes using the module ``MUSCLE``; and analysis of raw data
from Next Generation Sequencing using the module ``NGS``.
Below, we describe a working example of a study from gene search for phylogenetic
studies through analysis of sequenced data and assembly of Ion Torrent reads.

## Finding candidate genes from *Bombyx mori*
We use the *Bombyx mori* genome as starting point to obtain candidate genes
suitable for sequencing across non-model species, although ``PyPhyloGenomics`` can
work with any genome. 
We looked for genes that fulfilled the following requirements: (i) the genes should
be orthologs; (ii) the genes should be single-copy genes; (iii) their sequences
need to be around 251 base pairs in length for easy sequencing in our in-house
Next Generation Sequencer, an Ion Torrent PGM sequencer from Life Technologies
(<http://www.iontorrent.com/>).

The OrthoDB database <ftp://cegg.unige.ch/OrthoDB6/> has a catalog of orthologous
protein-coding genes for vertebrates, arthropods and other living groups. We parsed
this list with the module OrthoDB from our package ``PyPhyloGenomics`` and obtained
a list of single-copy, orthologous gene IDs for *Bombyx mori* (12 167 genes in
total).

A function in our module BLAST extracted the sequences for the genes, found using
OrthoDB, from the CDS sequences of *Bombyx mori* [available at <http://silkdb.org>;
@duan2010]. We BLASTed the sequences against the *Bombyx mori* genome and discarded
those containing introns.
We kept genes with sequences longer than 300bp in length, and separated by at least
810kb within *Bombyx mori* chromosomes so that they can be considered independent
evolutionary entities. We obtained 574 exons.

We validated those exons by searching for these exons in published genomes of other
Lepidoptera species, such as *Danaus* [@zhan2011], *Heliconius* [@dasmahapatra2012]
and *Manduca* (<http://agripestbase.org/manduca/>).
This search is automated by using functions in our module BLAST that take as input
the list of genes from *Bombyx mori*, and the genomic sequences from the other model
species.
During validation, ``PyPhyloGenomics`` creates FASTA format files by appending
matching sequences from the tested genomes. It also automates the alignment of
sequences by using the software MUSCLE.

``PyPhyloGenomics`` contains functions to automatically design degenerate primers
from the homologous sequences by delivering the sequences to *primer4clades*
[@contreras2009]. 
*primer4clades* is a web service based on the CODEHOP strategy for primer design
[@rose1998]. It is recomended that automated alignments and primers are analyzed
carefully to ensure good quality.  After this step, one can have numerous candidate
genes ready to be sequenced across non-model Lepidoptera species using NGS techniques.

## Sample preparation for Next Generation Sequencing in the Ion Torrent PGM
We ordered the primers designed by ``PyPhyloGenomics`` from the company TAG Copenhagen
A/S (Denmark) and used them to amplify the selected regions for 16 specimens in Lepidoptera using multiplexed PCR reactions.
We also sequenced one specimen of *Bombyx mori* (voucher code NW149-2)
as control sample to validate our ``PyPhyloGenomics`` software.

We followed the library preparation protocol for Next Generation Sequencing by 
@meyer2010 with minor modifications for Ion Torrent.  This method
consists in attaching an index (or barcode of 8 base pairs) to the amplified PCR products of each
specimen before sequencing.
Therefore, it will be possible to sequence in one single run many genes for a number
of specimens. During data analysis, the reads are separated from the NGS data
according to index sequence.


## Next Generation Sequencing output analysis
After the sequencing run in an Ion Torrent PGM using the 314 chip, we obtained a
FASTQ file of 61 Mb, including more than 146,000 short reads of around 250bp.
The ``PyPhyloGenomics`` module ``NGS`` has the function ``prepare_data`` that
converts the Ion Torrent FASTQ file to Solexa quality format (input for the
``fastx-toolkit``), and it created a FASTA file with the indexes trimmed and ready
to be used in a BLAST against the exon sequences found during the validation of
Lepidoptera genes.
All reads were separated in bins according to the matched candidate genes.

We separated reads from each bin according to specimen index (or barcode) by using
the function ``separate_by_index`` in the module ``NGS``. It is common that the
sequencing process outputs reads with errors in the index section.
Thus, we measured the Levenshtein distance among our indexes in order to find out
the number of nucleotide changes needed to convert one index into another 
[although other methods have been proposed recently; @buschmann2013]. 
We assumed indexes to be the same if the Levenshtein distance was smaller than 2
units (as our indexes differ in two or more nucleotides). Our module ``NGS`` is able
to do the separation according to indexes (taking as parameter the user defined
Levenshtein distance value) and to compare the forward and reverse complement of the
index sequences.

We performed quality control of the reads using the function ``quality_control``
that employs the software ``fastx-toolkit`` to keep reads with high quality values and
trim low quality ends and indexes from these.  The function ``assembly`` uses the
*velvet* assembler [@zerbino2008] to perform *de novo* assembly of the reads into
consensus sequences for each bin with reads of each specimen. 
Parameters such as minimum quality scores, sequence length and coverage cut-off 
can be defined by users during the process of quality control and assembly.
The output file is a FASTA format file
containing the assembled sequences per specimen and per gene.  Although this proccess is
automated, it is recommended to manually check the assembled sequences to discard
errors and spurious sequences.

# Conclusions and future directions
After comparing the genomes of model species in Lepidoptera, we were able to
identify 219 orthologous genes with conserved exons of at least 300bp that can be
used for sequencing in non-model butterfly and moths for phylogenetic inference.

We used our software ``PyPhyloGenomics`` to automate gene search prodecures, align
sequences and design primers. Although we used the genomes of only 4 model species,
it will be feasible to include additional genomes in the future for refining the
validation of the candidate genes and design more specific primers.

We applied stringent parameters for quality control and assembly of consensus
sequences from the Ion Torrent reads and validated our protocols by obtaining
sequences of *Bombyx mori* for our candidate genes that match those in its published
genome.

Therefore, we belive that our toolkit ``PyPhyloGenomics`` in combination with the
Next Generation Sequencing technologies is a step forward in the advancement of phylogenetic
inference by obtaining and sequencing a large amount of genes. In the case of Lepidoptera,
we substantially increased the number of candidate genes for phylogenomics from \~20
to 219.


# Acknowledgments
We acknowledge CSC--IT Center for Science Ltd. (Finland) for the allocation of 
computational resources.
We are grateful with Olaf Thalmann, Eero Vesterinen and Meri Lindqvist for help with
the laboratory protocols and running the Ion Torrent PGM.  The study was supported
by a Kone Foundation grant (awarded to Niklas Wahlberg), Finland (C. Peña). P. Matos
acknowledges the funds from the Institute of Entomology (Czech Biology Centre) and
the University of South Bohemia. and XXXXXXX- yyyyyyyyyy-zzzzzzzzzz.


# References

