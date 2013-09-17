### Article

## PyPhyloGenomics: toolkit and protocol for developing phylogenetic markers in novel species for Next Generation Sequence data
Carlos Peña^*,1^; Victor Solis^2^; Pável Matos^3^; Chris Wheat^4^

^1^Laboratory of Genetics, Department of Biology, University of Turku, Turku, Finland

^2^

^3^Biology Centre AS CR, v.v.i., Institute of Entomology, Ceske Budejovice, Czech Republic

^4^Population Genetics, Department of Zoology, Stockholm University, Stockholm, Sweden

***Corresponding author:** Carlos Peña, E-mail: <mycalesis@gmail.com>

# Abstract


# Introduction
Next Generation Sequencing (NGS) is considered a quantum leap in improvement
in techniques for DNA sequencing [@loman2012].
The sequencing output of NGS technology is around 30 gigabases of DNA in one
single run [@reis2009] while the traditional Sanger method [@sanger1977] allows
sequencing only \~1,000 bp per specimen in the old capillary-based technology.
This higher yield is achieved by using massive parallel sequencing of PCR
products based on DNA synthesis using micron-scale beads on planar substrates
(a microchip) [@shendure2008].
As a result, millions of copies of sequences (reads) are produced from the DNA
templates. 
One application of NGS is targeted sequencing of numerous loci of interest in
one run [@ekblom2010], which is quicker and cheaper than using the Sanger
method.

Research in phylogenomics can be accelerated by using NGS due to the ease
to obtain DNA data at massive scale. It would be very easy  to sequence many
more than the 12 to 19 loci that so far have been used in phylogenomic studies 
[@wahlberg2008; @regier2013].
However, researchers have been relying on the Sanger method for sequencing a
handful of genes to be used in phylogenetic inference in several Lepidoptera
groups [@matos2013; @regier2013; @pena2011].

Some studies have used NGS techniques to sequence miRNAs in phylogenomic analyses 
of the high level relationships in Panarthropoda [@campbell2011].
miRNAs are nonprotein coding RNAs of small length involved in
DNA transcription and gene regulation. Using miRNAs for phylogenetics has the
drawback that these molecules are not easy to sequence from genomic DNA as miRNAs
are processed in the cell and shortened to \~22 base pair sequences
[@wienholds2005].

One issue to develop is a strategy to develop molecular markers or 
candidate genes suitable for phylogenetic inference, i.e. orthologs,
single copy genes, lack of introns, etc.
Ortholog genes are those that share a common ancestor during their evolutionary 
history [@chiu2006] and can be considered as homologous structures useful for 
comparative systematics.
Gene duplication is a common phenomenon in animals and plants [@duarte2010]
producing paralog genes with a degree of similarity depending on the time of
divergence since duplication. Paralogs are problematic for phylogenetic
inference and these are not normally used because they can cause error and
artifacts [@sanderson2002; @fares2005].

@wahlberg2008 obtained candidate genes for phylogenomics by identifying single
copy and orthologous genes of *Bombyx mori* from EST libraries. They searched for
EST sequences in the *Bombyx mori* genome in order to identify suitable exons.
These exon sequences were compared against EST libraries of related Lepidoptera
species in order to obtain homologous sequences for primer design. This
method depends on the availability of EST sequences which are single reads of
cDNA that might contain numerous errors and are prone to artefacts 
[@parkinson2002].

@regier2013 obtained nuclear gene sequences from mRNA by performing reverse 
transcription and PCR amplification [@regier2007]. mRNAs are molecules 
transcribed from genomic DNA that have had introns spliced and exons joined.
Therefore, attempting to sequence these genes from genomic DNA for other 
species will be troublesome due to the likely appearance of introns. 
Introns are sequences present in eukaryotic genes that are discarded during the 
process of protein synthesis [@page1998] and can vary widely in size among 
different species [@carvalho1999].
Thus, it might be difficult to assess homology for 
base pair positions if the sequences vary in length among the studied novel
species.
However, introns have been useful in phylogenetic studies of certain organisms
[e.g. @prychitko1997; @fujita2004].

Nuclear protein coding loci (NPCL) are the preferred markers in phylogenetic 
inference due to appropiate mutation rates, effortless alignment of sequences
and detection of paralogs [@townsend2008].
Moreover, genomic DNA can be used for sequencing NPCL, which has 
several advantages: (i) genomic DNA does not degrade so quickly as
RNA; (ii) it is simpler to preserve in the field; (iii) it can be sequenced even
from dry material (for example museum specimens); and (iv) it is the most
commonly used DNA in molecular systematics [@wahlberg2008].

@townsend2008 found candidate protein coding genes by BLASTing the genomes
*Fugu rubripes* (pufferfish) and *Homo sapiens*. The shared NPCL were compared
to the genomes of other species in order to assess exon limits, align homologous
sequences and design primers. Paralog genes were identified as those form the 
*Fugu* genome that matched more than one *Homo* gene.
 

Thus, a method is needed to find candidate genes that can be easily sequenced
from genomic DNA across several lineages.
One strategy to fulfill this goal could be comparing genomic sequences of model
species and identify conserved regions to extract suitable genes that can be
sequenced in novel species from simple extractions of genomic DNA. 

In this paper, we describe a protocol for finding genes from genomic DNA that 
are suitable for phylogenomic studies. 
We describe the software package ``PyPhyloGenomics``, written in the Python language,
that includes bioinformatic tools useful for automated gene finding, primer 
design and NGS data analysis. We have used this software to find homologous 
exons across genomes from several model organisms.
Our software also includes tools to filter output reads from NGS and assembling
sequences for each specimen.


## The ``PyPhyloGenomics`` package
The stable release of ``PyPhyloGenomics`` is available from the Python Package
Index (<https://pypi.python.org/pypi/PyPhyloGenomics>) for direct installation
of the most recent version using ``pip`` (a Python package installer). 
The development versions are available from github 
(<https://github.com/carlosp420/PyPhyloGenomics>). The full 
documentation and user guide are available from the github pages 
(<http://carlosp420.github.io/PyPhyloGenomics/>).
``PyPhyloGenomics`` is conceived as a workflow using its four modules. Selection 
of orthologous genes using the module ``OrthoDB``; search of genes in a set of
predicted genes from a model organism, extraction of genomic sequences for 
candidate genes from the model organisms, and validation of genes across genomes of
other model organisms using the module ``BLAST``; alignment and primer design from
genomic sequences for candidate genes using the module ``MUSCLE``; and 
analysis of raw data from Next Generation Sequencing in the Ion Torrent PGM using
the module ``NGS``.
Below, we describe a working example of a study from gene search for phylogenetic
studies through analysis of sequenced data and assembly of Ion Torrent reads.

## Finding candidate genes from *Bombyx mori*
We are interested in studing the phylogenetic relationships of lineages in the 
Lepidoptera. Hence, we decided to use the *Bombyx mori* genome as starting point 
(although any genome can be used) to obtain candidate genes suitable for
sequencing across non-model species.
As explained in the introduction, genes to be used in phylogenetic inference
have to fulfill the following requirements: (i) the genes should be orthologs;
(ii) the genes should be single-copy genes; (iii) their sequence need to be
around 251 DNA base pairs in length for easy sequencing in our in-house Next
Generation Sequencer, an Ion Torrent PGM sequencer from Life Technologies
(<http://www.iontorrent.com/>).

The OrthoDB database <ftp://cegg.unige.ch/OrthoDB6/> has a catalog of orthologous
protein-coding genes for vertebrates, arthropods and other living groups.
We parsed this list with the module OrthoDB from our package ``PyPhyloGenomics`` and 
obtained a list of single-copy, orthologous gene IDs for *Bombyx mori* (12 167
genes in total).

A function in our module BLAST extracted the sequences for those genes from
the *Bombyx mori* CDS sequences [available at <http://silkdb.org>; @duan2010]. We BLASTed
the sequences against the *Bombyx mori* genome and discarded those containing
introns.
We kept genes with sequences longer than 300bp in length, and separated by
at least 810kb so that they can be considered independent evolutionary entities
and obtained 575 exons.

We validated those exons by searching for these exons in published 
genomes of other Lepidoptera species, such as *Danaus* [@zhan2011],
*Heliconius* [@dasmahapatra2012] and *Manduca* (<http://agripestbase.org/manduca/>).
This search is automated by using functions in our module BLAST that take as
input the list of genes from *Bombyx mori*, and the genomic sequences
from the other model species.
During validation, ``PyPhyloGenomics`` creates FASTA format files by appending
matching sequences from the tested genomes. It also automates the alignment of
sequences by using the software MUSCLE.

``PyPhyloGenomics`` contains functions to automatically design degenerate primers
from the homologous sequences by delivering the sequences to *primer4clades*
[@contreras2009] and receiving the designed primers. 
*primer4clades* is a web service based on the
CODEHOP strategy for primer design [@rose1998]. It is recomended that
automated alignments and primers are analyzed carefully to ensure good quality.
After this step, one can have numerous candidate genes ready to be sequenced
across novel Lepidoptera species using NGS techniques.

## Sample preparation for Next Generation Sequencing in the Ion Torrent PGM
We ordered the primers designed by ``PyPhyloGenomics`` for the candidate genes 
from the company TAG Copenhagen A/S (Denmark) and used them to amplify
these regions for many specimens in Lepidoptera species using multiplexed
PCR reactions.
We sequenced several individuals of a wide range of non-model species in the
Lepidoptera.
We also sequenced specimens of the model taxon *Bombyx mori* (voucher code NW149-2)
as control sample in order to validate our ``PyPhyloGenomics`` software.

We followed the library preparation protocol for Next Generation Sequencing
by @meyer2010 with minor modifications for the Ion Torrent technology.
This method consists in attaching and index
(or barcode) to the amplified PCR products of each specimen previous to 
sequencing.
Therefore, it will be possible to sequence in one single run many genes for
a number of specimens. During data analysis, the reads are separated 
from the NGS data according to index.


## Next Generation Sequencing output analysis
After the sequencing run, we downloaded a FASTQ file from the Ion Server 
of 61 Mb, including more than 146,000 short reads of around 250bp in length from an
Ion Torrent PGM run using the 314 chip. 
The ``PyPhyloGenomics`` module ``NGS`` has the function ``prepare_data`` that
converted the Ion Torrent FASTQ file to Solexa quality format (suitable for
the ``fastx-toolkit``), created a FASTA file with indexes trimmed to be used in a BLAST
against the exon sequences of the expected genes that were found
during the validation of *Bombyx mori* genes across the genomes of the model
Lepidoptera species.
After blasting the NGS reads against this expected genes, all reads were separated
in bins according to the match against candidate genes.

We separated reads from each bin according to specimen index (or barcode) 
by using the function ``separate_by_index`` in the module ``NGS``.
It is common that the sequencing process outputs reads with errors in the index
section.
Thus, we measured the Levenshtein distance among our indexes in order to 
find out the number of nucleotide changes needed to
convert one index into another [although other methods have been proposed
recently; @buschmann2013]. 
We assumed indexes to be the same if the Levenshtein distance was smaller than
2 units (as our indexes differ in two or more nucleotides). Our module ``NGS``
is able to do the separation according to indexes (taking as parameter 
the user defined Levenshtein distance value) and compare the forward and reverse
complement of the index sequences.

We performed quality control of the reads using the function 
``quality_control`` that employs the software ``fastx-toolkit`` 
to keep reads with high quality values, trim low quality ends and indexes.
The function ``assembly`` uses the *velvet* assembler [@zerbino2008]to guess
optimal parameters to perform *de novo* assembly of the reads into consensus
sequences for each bin containing reads of each specimen.

Our function ``NGS.assembly`` in ``PyPhyloGenomics`` automates this process
and requires as input parameters for triming low quality reads, triming of 
indexes and coverage threshold for assembly in *velvet*. The output file is 
a FASTA format file containing the assembled sequences per specimen and gene.
Although this proccess is automated, it is recommended to manually check the
assembled sequences to discard errors and spurious sequences.

# Conclusions and future directions
After comparing the genomes of model species in Lepidoptera, we were able to
identify 219 orthologous genes with conserved exons of at least 300bp that
can be used for sequencing in non-model butterfly and moths for phylogenetic
inference.

We used our software ``PyPhyloGenomics`` to automate gene search prodecures,
align sequences and design primers. Although we used the genomes of only
4 model species, it will be trivial to include additional genomes in the future
for refining the validation of the candidate genes and design more specific
primers.

We applied stringent parameters for quality control and assembly of consensus
sequences from the Ion Torrent reads and validated our protocols by obtaining
sequences of *Bombyx mori* for our candidate genes that match those in its
published genome.

Therefore, we belive that our toolkit ``PyPhyloGenomics`` in combination with
the Next Generation Sequencing technology can help obtainig and sequencing many
genes for phylogenetic inference, many more than the 20 or so currently being
used in the field of Lepidoptera phylogenetics.


# Acknowledgments
We acknowledge CSC--IT Center for Science Ltd. (Finland) for the allocation of 
computational resources.
We are grateful with Olaf Thalmann, Eero Vesterinen and Meri Lindqvist for help
with the laboratory protocols and running the Ion Torrent PGM.
The study was supported by a Kone Foundation grant (awarded to Niklas Wahlberg), 
Finland (C. Peña) and XXXXXXX- yyyyyyyyyy-zzzzzzzzzz.


# References

