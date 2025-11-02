#!/bin/python



### Exercise 1 ###



#read in and format the input file content and store contents in a variable
input_connect = open('/localdisk/home/data/BPSM/Lecture13/input.txt')
seq_list = input_connect.read().rstrip('\n').upper().split()

#stores the seq adapter in a variable, sets a counter at 0, iterates through
#each item of the seq list, removes ALL occurences of the adapter seq from
#said items, and prints the length of each trimmed seq
adapter = "ATTCGATTATAAGC"
counter = 0

for seq in seq_list:
    seq = seq.replace(adapter, "")
    seq_list[counter] = seq
    print(len(seq_list[counter]))
    counter += 1

#reverts the list of seqs back into srings seperated by new lines and stores
#said seqs in a variable
trimmed_seqs = "\n".join(seq_list)

#stores the trimmed seqs in a new file called E1_output.txt
output_connect = open('E1_output.txt', 'w')
output_connect.write(trimmed_seqs)
output_connect.close()



### Exercise 2 ###



#gets the genomic_dna and exons files, stores exon coords as a list
gen_dna_connect = open('/localdisk/home/data/BPSM/Lecture13/genomic_dna2.txt')
gen_dna = gen_dna_connect.read().upper().rstrip('\n')

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



### Exercise 3 ###



#import necessary libarries
import os, shutil

#gets the NCBI seq from last lecture
rem_seq_connect = open('/localdisk/home/s2837739/Exercises/Lecture12/remote_genomic_seq.txt')
rem_seq = rem_seq_connect.read().replace('\n', '')
rem_seq_connect.close()

#
win_start = 0
win_end = 30
seq_end = len(rem_seq) - 1


#3c
#shutil.rmtree('ex3_FASTAs')
#os.mkdir('ex3_FASTAs')
#counter = 0
#os.chdir('ex3_FASTAs')

#3d
#winOut_connect = open('ex3d_output.fasta', 'w')

#3e
winOut_connect = open('ex3e_output.fasta', 'w')

#3a-d
#while win_end <= seq_end and win_start <= (seq_end - 30):

#3e
while win_end <= (seq_end + 30) and win_start <= seq_end:
    win = rem_seq[win_start:win_end]
    #3a
    #print(win)

    #3b
    #GC_win = str(int((len(win.replace('A', '').replace('T','')) / 30) * 100)) + '%'
    #print('GC% = ',GC_win)

    #3c
    #fasta_header = 'remote_seq_' + str(win_start) + '_' + str(win_end)
    #winOut_connect = open((fasta_header + '.fasta'), 'w')
    #winOut_connect.write(('>' + fasta_header + '\n'))
    #winOut_connect.write(win)
    #winOut_connect.close()

    #3d-e
    fasta_header = 'remote_seq_' + str(win_start) + '_' + str(win_end)
    winOut_connect.write(('>' + fasta_header + '\n'))
    winOut_connect.write(win + '\n\n')

    win_start += 3
    win_end += 3

#3d-e
winOut_connect.close()



### Exercise 4 ###




