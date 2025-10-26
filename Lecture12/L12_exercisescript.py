#!/usr/bin/python3

#imports the necessary python libraries to run the code below
import os, sys, subprocess

#grab the two files
#subprocess.call("cp /localdisk/data/BPSM/Lecture12/plain_genomic_seq.txt plain_genomic_seq.txt", shell = True)

#subprocess.call("esearch -db nucleotide -query \"AJ223353[accession]\" | efetch -format fasta | grep -v \">\" > remote_genomic_seq.txt, shell=True")

#store the contents of the local and remote seqs in seperate variables in proper
#formats (all uppercase, no "\n"s, all DNA)
local_connection = open("plain_genomic_seq.txt")
local_seq = local_connection.read().upper().rstrip("\n")

remote_connection = open("remote_genomic_seq.txt")
rem_seq = remote_connection.read().upper().replace("\n", "")

#from IUPAC, acceptible codes for nns are (G A T C R Y M K S W H B V D N)
ambiguity = list("GTACRYMKSWHBVDN")

#find characters in local seq that aren't IUPAC accepted

#for base in list(local_seq):
#    if base not in ambiguity:
#        print(base)

#output: 
#X
#L
#X
#X
#X
#X
#X


#L and X are not IUPAC, so we remove them from the local seq
local_seq = local_seq.replace("L","").replace("X","")

#do the same for the remote seq
#for base in list(rem_seq):
#    if base not in ambiguity:
#        print(base)

#output:""
#remote seq is good

#find the coding region of the remote sequence
#subprocess.call("esearch -db nucleotide -query \"AJ223353[accession]\" | efetch -format gb | grep \"CDS\" > remote_CDS.txt", shell=True)
#29..409

#given that the local_seq has an intron from position 63 to 91:
#store the coding and non-coding sequences in two seperate variables
cds = local_seq[:63] + local_seq[91:]
non_cds = local_seq[63:90]

#get lengths of cds and non_cds and make fasta headers for their output files
cds_len = str(len(cds))
non_cds_len = str(len(non_cds))

cds_fasta_header = ">local_seq_cds_" + cds_len
non_cds_fasta_header = ">local_seq_non_cds_" + non_cds_len

#output the cds and non_cds of the local seq into two seperate fasta files
cds_contents = cds_fasta_header + "\n" + cds
cds_subseq = open(cds_fasta_header.replace(">","") + ".fasta", "w")
cds_subseq.write(cds_contents)
cds_subseq.close

non_cds_contents = non_cds_fasta_header + "\n" + non_cds
non_cds_subseq = open(non_cds_fasta_header.replace(">","") + ".fasta", "w")
non_cds_subseq.write(non_cds_contents)
non_cds_subseq.close

#repeat the above process with the remote sec

#find the coding region of the remote sequence
#subprocess.call("esearch -db nucleotide -query \"AJ223353[accession]\" | efetch -format gb | grep \"CDS\" > remote_CDS.txt", shell=True)
#29..409

cds = rem_seq[29:409]
non_cds = rem_seq[:29] + rem_seq[409:]

#get lengths of cds and non_cds and make fasta headers for their output files
cds_len = str(len(cds))
non_cds_len = str(len(non_cds))

cds_fasta_header = ">remote_seq_cds_" + cds_len
non_cds_fasta_header = ">remote_seq_non_cds_" + non_cds_len

#output the cds and non_cds of the local seq into two seperate fasta files
cds_contents = cds_fasta_header + "\n" + cds
cds_subseq = open(cds_fasta_header.replace(">","") + ".fasta", "w")
cds_subseq.write(cds_contents)
cds_subseq.close

non_cds_contents = non_cds_fasta_header + "\n" + non_cds
non_cds_subseq = open(non_cds_fasta_header.replace(">","") + ".fasta", "w")
non_cds_subseq.write(non_cds_contents)
non_cds_subseq.close
