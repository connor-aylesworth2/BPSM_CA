#!/bin/python

#1
#opens the fly data, takes the last new line character off the file, then stores the data in a list
with open('/localdisk/home/s2837739/Exercises/Lecture14/data.csv') as fly_connect:
    fly_seqs = fly_connect.read().rstrip('\n').split('\n')

#1a-e
#iterates through the list of gene entries, and makes a list for each line that contains
# four elements per line; species name, sequence, gene name, expression level;
#also makes the sequence of each entry uppercase
for line in fly_seqs:
    line = line.split(',')
    line[1] = line[1].upper()
    
    #1a
    #checks if the species name of each gene entry is melanogaster OR simulans, then if true
    #it prints the gene name of the entry
    #if line[0] is 'Drosophila melanogaster' or 'Drosophila simulans':
    #    print(line[2])
    
    #1b
    #checks if the length of the sequence of each gene entry is between 90 and 110 bases long;
    #if true, it prints the gene name
    #if len(line[1]) >= 90 and len(line[1]) <= 110:
    #    print(line[2])

    #1c
    #makes a variable for AT content, checks if the sequence of each gene entry has an AT content less
    #than 0.5 and if the expression value of that gene entry is greater than 200;
    #if true, it prints the gene name
    #AT = len(line[1].replace('G', '').replace('C', '')) / len(line[1])
    #if AT < 0.5 and int(line[3]) > 200:
    #    print(line[2])

    #1d
    #first checks if the gene name of each gene entry starts with h or k;
    #if that's true, it then checks that the species name isn't melanogaster;
    #if both of those conditions are true, it prints the gene name
    #if line[2].startswith('k') == True or line[2].startswith('h') == True:
    #    if line[0] != 'Drosophila melanogaster':
    #        print(line[2])

    #1e
    #calculates the AT content of the sequence of each entry, checks whether the AT content is high,
    #medium, or low, then prints the name of the gene of each entry and its AT content interpretation
    AT = len(line[1].replace('G', '').replace('C', '')) / len(line[1])
    if AT > 0.65:
        print(line[2] + ' has high AT content.')
    elif AT < 0.45:
        print(line[2] + ' has low AT content.')
    elif AT >= 0.45 and AT <= 0.65:
        print(line[2] + ' has medium AT content.')



