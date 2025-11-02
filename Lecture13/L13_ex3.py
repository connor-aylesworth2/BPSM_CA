#!/bin/python

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


