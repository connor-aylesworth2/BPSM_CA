#!/bin/python

#gets the genomic_dna and exons files, stores exon coords as a list
gen_dna_connect = open('/localdisk/home/data/BPSM/Lecture13/genomic_dna2.txt')
gen_dna = gen_dna_connect.read().upper().rstrip('\n')
gen_dna_connect.close()

exons_connect = open('/localdisk/home/data/BPSM/Lecture13/exons.txt')
exons = exons_connect.read().rstrip().split()

# sets a counter at 0 and makes an empty list
counter = 0
cds = []

#for loop to extract the exon coords from the gen_seq and store them in the mad list
for coord in exons:
    start = int(coord.split(',')[0]) -1
    end = int(coord.split(',')[1])
    exon = gen_dna[start:end]
    cds.append(exon)

#turns the list of exons into one long cds
cds = ''.join(cds)

#stores the cds in an output file called E2_output.txt
output = open('E2_output.txt','w')
output.write(cds)
output.close()


