% PyPhyloGenomics: toolkit and protocol for developing phylogenetic markers in novel species for Next Generation Sequence data
% Carlos Peña^*,1^; Victor Solis^2^; Pável Matos^3^; Chris Wheat^4^
% 2013-05-08

^1^Laboratory of Genetics, Department of Biology, University of Turku, Turku, Finland

^2^

^3^Biology Centre AS CR, v.v.i., Institute of Entomology, Ceske Budejovice, Czech Republic

^4^Population Genetics, Department of Zoology, Stockholm University, Stockholm, Sweden

***Corresponding author:** E-mail: <mycalesis@gmail.com>

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
groups [@matos2013; -@regier2013; @pena2011].

Some studies have used NSG techniques to sequence miRNAs in phylogenomic analyses 
of the high level relationships in Panarthropoda [@campbell2011].
miRNAs are nonprotein coding RNAs of small length involved in
DNA transcription and gene regulation. Using miRNAs for phylogenetics has the
drawback that these molecules are not easy to sequence from genomic DNA as miRNAs
are processed in the cell and shortened to \~ 22 base pair sequences
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

-@wahlberg2008 obtained candidate genes for phylogenomics by identifying single
copy and orthologus genes of *Bombyx mori* from EST libraries. They searched for
EST sequences in the *Bombyx mori* genome in order to identify suitable exons.
These exon sequences were compared against EST libraries of related Lepidoptera
species in order to obtain homologous sequences for primer design. This
method depends on the availability of EST sequences which are single reads of
cDNA that might contain numerous errors and are prone to artefacts 
[@parkinson2002].

-@regier2013 obtained nuclear gene sequences from mRNA by performing reverse 
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
commonly used DNA in molecular systematics [-@wahlberg2008].

-@townsend2008 found candidate protein coding genes by BLASTing the genomes
*Fugu rubripes* (pufferfish) and *Homo sapiens*. The shared NPCL were compared
to the genomes of other species in order to assess exon limits, align homologous
sequences and design primers. Paralog genes were identified as those form the 
*Fugu* genome that matched more than one *Homo* gene.
 

Thus, a method is needed to find candidate genes that can be easily sequenced
from genomic DNA across several lineages.
One strategy to fulfill this goal could be comparing genomic sequences of model
species and extract suitable genes that can be sequenced in novel species from 
simple extractions of genomic DNA. 

In this paper, we describe a protocol for finding genes from genomic DNA that 
are suitable for phylogenomic studies. 
We describe the software package PyPhyloGenomics, written in Python language,
that includes bioinformatic tools useful for automated gene finding, primer 
design and NGS data analysis. We have used this software to find homologous 
exons across genomes from several model organisms.
Our software also includes tools to filter output reads from NGS and assemble
the sequences for each specimen and their sequenced genes so that datasets can
be assembled for analysis in common software for phylogenetic inference.


# Methods

## Finding candidate genes from *Bombyx mori*

We are interested in studing the phylogenetic relationships of lineages in the 
Lepidoptera. Hence, we decided to use the *Bombyx mori* genome as starting point 
(although any genome can be used) to obtain candidate genes suitable fo
r sequencing across novel species.
As explained in the introduction, genes to be used in phylogenetic inference
have to fulfill the following requirements: (i) the genes should be orthologs;
(ii) the genes should be single-copy genes; (iii) their sequence need to be
around 251 DNA base pairs in length for easy sequencing in our in-house Next
Generation Sequencer, an Ion Torrent PGM sequencer from Life Technologies
(<http://www.iontorrent.com/>).

The OrthoDB database <ftp://cegg.unige.ch/OrthoDB6/> has a catalog of orthologous
protein-coding genes for vertebrates, arthropods and other living groups.
We parsed this list with the module OrthoDB from our package PyPhyloGenomics and 
obtained a list of single-copy, orthologous gene IDs for *Bombyx mori* (12 167
genes in total).

A function in our module BLAST extracted the sequences for those genes from
the *Bombyx mori* CDS sequences (available at <http://silkdb.org>). We BLASTed
the sequences against the *Bombyx mori* genome and discarded those containing
introns.
We kept genes with sequences longer than 300bp in length, and separated by
at least 810kb so that they can be considered independent evolutionary entities
and obtained 575 exons.

We validated those exons by automated search  of these exons in other genomes of
species in Lepidoptera, such as, *Danaus*, *Heliconius* and *Manduca*.
This search is automated by using functions in our module BLAST that take as
input the list of genes from *Bombyx mori*, and the file with genomic sequences
for the target species.
During validation, PyPhyloGenomics creates FASTA format files by appending
matching sequences from the tested genomes. It also automates the alignment of
sequences by using the software MUSCLE.

PyPhyloGenomics contains functions to automatically design degenerate primers
from the homologous sequences by delivering the sequences to primer4clades
and receiving the designed primers. primer4clades is a web service based on the
CODEHOP strategy for primer design [@contreras2009].

It is recomended that both alignment and designed primers to be analyzed
carefully to make sure that the are no problems. After this step, one can
have around XXX genes ready to be sequenced across novel species in 
Lepidoptera for many species if NGS techniques are used.

### Sample preparation for Next Generation Sequencing in Ion Torrent
We followed the library preparation protocol for NGS by @meyer2010 with minor
modifications  for the Ion Torrent technology.
This method consists in attaching and index
(or barcode) to the amplified PCR products of each specimen previous to 
sequencing.
Therefore, it will be possible to separate reads from the NGS data according
to index.

We sequenced several individuals of a wide range of species in the Lepidoptera.
We also sequenced specimens of the model species *Bombyx mori*, *Danaus?*,
(codes ``XXX``)  as control samples in order to validate our NGS
data assembly protocols.

The Ion Torrent platform 2 can sequence from 280 to 320bp per read. The Ion Torrent
adapter, index and primer sequences make around 119 base pairs in length, 
leaving around 201 bp as the maximum internal gene region that can be sequenced
(region within degenerate primers) (Table 1). This is the region per gene 
(or exon) that is potentially informative for phylogenetic inference.

**Table 1.** Adaptors and primers needed for sequencing in the NGS Ion Torrent
platform 2. 
The maximum length of sequenced amplicon is \~ 201 bp after discarding primer
regions.

  Primer                 Length (bp)
  --------------------  ------------
  Adapter A             30
  5' Index              8
  5' Degenerate Primer  25
  Exon                  **119**
  3' Degenerate Primer  25
  3' Index              8
  Adapter P             23
  --------------------  ------------



## Next Generation output analysis
The raw output data of the Ion Torrent was a FASTQ format file of XXX MB? and XXX
short reads up to XX bp in length. 
We created a BLAST database with the exon sequences  of candidate genes found
after the exon validation of *B. mori*  genes across the genomes of the model
Lepidoptera species.
We used blasted the find NGS reads against this database in order to find 
those matching the homologous regions of the candidate genes. 
All reads were separated in bins according to the match against
candidate genes.

We separated reads from each bin according to each specimen index (or barcode).
The sequencing process produced many reads with errors in the barcode section.
Thus, we measured the Levenshtein distance between the sequenced index region
and our indexes in order to measure the number of nucleotide changes needed to
convert one index into the other. 
We assumed indexes to be the same if the Levenshtein distance was smaller than
2 units (as our indexes differ in two or more nucleotides). Our module XXX in 
PyPhyloGenomics is able to do the separation according to indexes taking
into account Levenshtein distances and compare the forward and reverse
complement of the index sequences.

We performed quality control of the reads using the software fastx_tools
and assembled consensus sequences for each bin containing reads for specimen
using the *velvet* assembler [@zerbino2008]. 

Our functions in PyPhyloGenomics automate this process and require as input
the parameters needed for triming low quality reads, triming of indexes and 
coverage threshold for assembly in velvet.

The output file is a FASTA format file containing the assembled sequences per
specimen and gene.

It is recommended to manually check the assembled sequences to discard errors
and spurious sequences.

We uploaded all our sequences to our molecular database software 
VoSeq [@pena2012] for
creation of datasets to be used in phylogenetic analysis later on.


## Comparison with other methods
@regier2009, @regier2008, -@regier2013 use Reverse Transcription PCR from mRNAs to avoid sequencing introns, although the corresponing genomic DNA sequences are  likely to include introns. Therefore if one use their genes, it is not recommended to do "direct gene amplification" [-@regier2007].

## Other software
CEPiNS [@hasan2013] is a software pipeline that uses predicted gene sequences
from both model and novel species to predict and identify exons suitable for
sequencing useful for phylogenetic inference.

# Acknowledgments
We acknowledge CSC--IT Center for Science Ltd. (Finland) for the allocation of 
computational resources.

# References
Targeted sequencing [@godden2012]




