#!/bin/python

#import necessary packages
import os, shutil

#removes previously made directory if it already exists, creates a directory and sub-
#directories for size bins, and changes the cwd to the new ex4_bins directory
shutil.rmtree('ex4_bins')
os.makedirs('ex4_bins/100_199_seqs')
os.chdir('ex4_bins')

#set values for the below for loop that makes size bins
binStart = 200
binEnd = 299
counter = 1

#for loop that makes 9 size bins for the output files that the rest of the scrip generates
while counter <= 8:
    fold_name = str(binStart) + '_' + str(binEnd)
    os.mkdir(fold_name)
    binStart += 100
    binEnd += 100
    counter += 1

to_work_with = []
os.chdir('/localdisk/home/s2837739/Exercises/Lecture13')

for names in os.listdir('dna_files/'):
    if names.endswith('.dna'):
        print('foop')
        to_work_with = to_work_with.append(names)
print(to_work_with)
