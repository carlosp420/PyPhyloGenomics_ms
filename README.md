## Requires
* BioPython
* velvetg_de
* velveth_de
* fastx-toolkit
* ncbi-blast+
* [PyPhyloGenomics](https://github.com/carlosp420/PyPhyloGenomics) > 0.3.4

## Sample data
* ``data/Bmori_run.fastq`` :: Raw reads from an Ion Torrent run
* ``data/genes_Bmori.fasta`` :: Expected genes to be found in the Ion Torrent run
* ``data/indexes.fasta`` :: Sample of indexes (barcodes) uses in the Ion Torrent run

## Reproduce analysis
Run the analysis on the sample data. Install dependencies and then:

    > make analysis

