#!/usr/bin/bash

db="/localdisk/home/s2837739/Exercises/Lecture06/nem"

blastx -db ${db} -query all_CDSs.fasta -outfmt 7 > CDS_blasted.txt

blastx -db ${db} -query all_non_CDSs.fasta -outfmt 7 > non_CDS_blasted.txt

