#!/usr/bin/python

#defines the function with two parameters; the proportion defaults to 50%
def b_count(seq, prop = 50):
    
    # formats the inputted sequence, makes a variabel that is the string
    #   of bases that aren't T, C, G, or A, and calculates the non-DNA 
    #   content of the given seq
    seq = seq.upper()
    nonDNA_seq = seq.replace('A','').replace('T','').replace('C','').replace('G','')
    nonDNA_cont = (len(nonDNA_seq) / len(seq)) * 100
    
    # checks if the non-dna content is greater or less than the proportion
    #   that the user inputted
    if nonDNA_cont < prop:
        return False
    else:
        return True

# some asserts to test the function
assert b_count('ATGCCCGCXX', 20) == True
assert b_count('ATGCCCGCXX', 21) == False
assert b_count('ATGCCCGCXX') == False
assert b_count('ATGCCXXXXX') == True

