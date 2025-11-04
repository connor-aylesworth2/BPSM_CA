#!/usr/bin/python

# import necessary packages
import sys

# define the function with three parameters: sequence (dna), length of kmers (k), 
#   and the threshold of kmers that occur more than n times (n)
def kmer_count(dna, k, n):
    
    #format the inputted sequence
    dna = dna.replace('\n', '').upper()

    # defines 3 variables that will be used in the follwing for loop
    start = 0
    end = k
    kmers = []

    # makes a list of all of the possible kmers of length k by
    while end <= (len(dna)) and start <= (len(dna) - (k + 1)):
        win = dna[start:end]
        #print(win)
        kmers.append(win)
        start += 1
        end += 1

    # makes an empty list to store the kmers that occur more than n times
    #   from the previous loop
    gud_kmers = []

    for kmer in kmers:
        # sets a counter for every possible kmer
        kmer_count = 0

        # for each kmer in the list filled by the first for loop in this
        #   code, it checks the whole list of original kmers for how many
        #   times each kmer occurs
        for seq in kmers:
            if seq == kmer:
                kmer_count += 1

        # adds the kmers that occur more than n times to the list of kmers that we
        #   want for output per the exercise's request
        if kmer_count > n:
            gud_kmers.append(kmer)

    # removes the redundancies in the output list and prints each kmer
    #   that occurs in the given sequence more than n times
    gud_kmers = list(set(gud_kmers))
    for kmer in gud_kmers:
        return kmer

test = kmer_count('ATGCATCATG', 2, 2 )

print(test)

