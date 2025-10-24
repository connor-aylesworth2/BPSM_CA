#!/usr/bin/python3

#1
#stores the given sequence in a variable for manipulation
sequence = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

#individually counts the amount of As and Ts in the stored sequence and stores those
#values in seperate variables
As = sequence.count("A")
Ts = sequence.count("T")

#counts the length of the stored sequence and stores the result in another variable
seq_len = len(sequence)

#calculated the percentage of ATs by summing the total As and Ts, dividing that
#sum by the sequence length, and multiplying that output by 100
AT = str(int(((As+Ts)/seq_len)*100)) + "%"

#prints a sentence that lists the AT content of the sequence
print("#1) The AT content of the given sequnece is\n",AT,".\n\n\n")



#2
#stores the given sequence in a variable for manipulation and also stores the same value in
#another variable that logs the unchanged sequence
sequence = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
old_seq = sequence

#replaces all As, Ts, Cs, and Gs with Ws, Xs, Ys, and Zs, respectively
sequence = sequence.replace("A", "W")
sequence = sequence.replace("T", "X")
sequence = sequence.replace("C", "Y")
sequence = sequence.replace("G", "Z")

#replaces all Ws, Xs, Ys, and Zs with Ts, As, Gs, and Cs, respectively
sequence = sequence.replace("W", "T")
sequence = sequence.replace("X", "A")
sequence = sequence.replace("Y", "G")
sequence = sequence.replace("Z", "C")

#prints a sentence that lists the original given sequence and its complement
print("#2) The complement of the sequence\n\n", old_seq, "is\n", sequence, "\n\n\n")



#3
#stores the given sequence and the motif that the restriction enzyme ECORI cuts at in
#two seperate variables
seq = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
motif = "GAATTC"

#finds the index of the cutsite sequence
#adds one to account for the cutsite being between the first and the second NTs
cutsite = int(seq.find(motif)) + 1  

#calculates the length of the two theoretically resulting fragments of DNA from
#an interaction between ECORI and the given DNA sequence and stores those two
# values in two different variables
frag1 = len(seq[:(cutsite)])
frag2 = len(seq[cutsite:])

#reports the fragment lengths calculated in the previous code
print("#3) The size of the two resulting fragments of the restriction enzyme interaction are\n", frag1, "and\n", frag2, "nucleotides.\n\n\n")



#4
seq = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"

#a 
ex1 = seq[:64]
ex2 = seq[91:]
coding = ex1 + ex2

print("#4a) The coding region (sequence post-splicing) of the given DNA sequence is\n", coding, "\n")

#b
seq_len = len(seq)
coding_len = len(coding)

percent_coding = str(int((coding_len / seq_len)*100)) + "%"

print("#4b) The given DNA sequence is\n", percent_coding,"% coding.\n")

#c
intron = seq[64:91].lower()
OG_seq = ex1 + intron + ex2

print("#4c) The original sequence with coding regions denoted by uppercase bases is\n", OG_seq, "\n\n\n")

