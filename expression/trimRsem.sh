#!/bin/bash

#preparing reference
mkidr cds
cd cds

getLongestTranscript.py <ensemblBioMartOutput.fas> > species.longest.fas

rsem-prepare-reference --bowtie species.longest.fas species.longest.fas

cd ..

#dowlonading libraries
fastq-dump --gzip --split-files SRR924547 #replace with appropriate SRR#

#trimmomatic and rsem parameters
TRIMDIR=~/software/Trimmomatic-0.39
ADAPTERS=$TRIMDIR/adapters/allAdapters.fas
ID=${PWD##*/}
LEFT=clean.l.fastq.gz
RIGHT=clean.r.fastq.gz
REF=../cds/species.longest.fasta

java -jar $TRIMDIR/trimmomatic-0.39.jar \
        PE \
        -phred33 \
        -threads 10 \
        *_1.fastq.gz \
        *_2.fastq.gz \
        $LEFT \
        unpair.left.fastq.gz \
        $RIGHT \
        unpair.right.fastq.gz \
        ILLUMINACLIP:$ADAPTERS:2:30:10 \
        HEADCROP:5 \
        SLIDINGWINDOW:5:30 \
        MINLEN:50

rm unpair*

#rsem expression calculations
rsem-calculate-expression \
        --paired-end \
        -p 10 \
        --no-bam-output \
        $RIGHT \
        $LEFT \
        $REF \
        $ID.exp

