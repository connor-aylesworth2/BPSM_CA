#!/bin/python

#2
import sys

#ask the user for the name of the file containing the DNA that they want to use
#   for the analysis, what they want the length of the kmers to be, and what they
#   want n to be, and stores all three of those inputs in seperate variables
dna = input('What is the file name containing the DNA you wish to run this k-mer analysis on? ')
k = int(input('What length do you want the k-mers to be? '))
n = int(input('What do you want n to be? '))

#reads in the file that the user wants and stores it in a variable
with open(dna) as seq_connect:
    seqs = seq_connect.read().rstrip('\n').replace('\n', '')

#defines 3 variables that will be used in the follwing for loop
start = 0
end = k
kmers = []

#makes a list of all of the possible kmers of length k by
while end <= (len(seqs)) and start <= (len(seqs) - (k + 1)):
    win = seqs[start:end]
    #print(win)
    kmers.append(win)
    start += 1
    end += 1

#makes an empty list to store the kmers that occur more than n times from the previous loop
gud_kmers = []


for kmer in kmers:
    #sets a counter for every possible kmer
    kmer_count = 0

    #for each kmer in the list filled by the first for loop in this code, it checks the
    #   whole list of original kmers for how many times each kmer occurs
    for seq in kmers:
        if seq == kmer:
            kmer_count += 1

    #adds the kmers that occur more than n times to the list of kmers that we 
    #   want for output per the exercise's request
    if kmer_count > n:
        gud_kmers.append(kmer)

#removes the redundancies in the output list and prints each kmer that occurs in the given sequence
#   more than n times
gud_kmers = list(set(gud_kmers))
for kmer in gud_kmers:
    print(kmer)
