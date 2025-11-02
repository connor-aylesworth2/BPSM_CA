#!/bin/python

#storing the list of seqs in a variable, makes a duplicate variable, and makes an empty list that'll be used in the following loops
OG_seqs = ['ATTGTACGG', 'AATGAACCG', 'AATGAACCC', 'AATGGGAAT']
seqs = OG_seqs
comps = []

#first for loop that iterates through each sequence in the original list
for seq in OG_seqs:

    #sets an index for the seq in the duplicate list that pertains to the seq in the duplicate
    #   list that the current iteration (of the above for loop) is being compared to 
    seq_index = 1
    
    #while loop that changes the index of the duplicate list so that the current iteration seq
    #   is compared to all other sequences in the duplicate list
    while seq_index <= (len(seqs) - 1):
        
        #setting variables for the index of each base to be compared and a given seq's similarity score
        index = 0
        sim_count = 0
        
        #for loop that calculates a similarity score for the current iteration and a given dupliate seq
        #   that it is being compared to. Iterates through each base of the current iteration and compares
        #   it to the corresponding base position in a seq from the dup seq list
        for base in seq:
            if base == (seqs[seq_index])[index]:
                sim_count += 1
        
            index += 1
        
        #calculates % similarity
        sim = (sim_count / len(seq)) * 100
        comparison = (seq + '-' + seqs[seq_index] + ': ', str(int(sim)) + '%')
        
        #adds comparison generated to list of comps
        comps.append(comparison)
        
        #changes index of dup list
        seq_index += 1
        #print(seqs)
        #print(seq)
        #seqs.remove(seq)


#comps = set(comps)
for comp in comps:
    print(comp)




#seq = seqs[0]
#seq_index = 1
#while seq_index <= (len(seqs) - 1):
#    index = 0
#    sim_count = 0
#    for base in seq:
#        if base == (seqs[seq_index])[index]:
#            sim_count += 1
#
#        index += 1
#
#    sim = (sim_count / len(seq)) * 100
#    print(str(int(sim)) + '%')
#
#    seq_index += 1




#seq_index = 1
#
#index = 0
#sim_count = 0
#seq = seqs[0]
#
#for base in seq:
#    if base == (seqs[seq_index])[index]:
#        sim_count += 1
#
#    index += 1
#
#sim = (sim_count / len(seq)) * 100
#print(str(int(sim)) + '%')
