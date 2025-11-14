#!/usr/bin/python

# import necessary libraries
import os, re

# read in the accessions as a string and turn it into a list
accStr = 'xkn59438, yhdck2, eihd39d9, chdsye847, hedle3455, xjhd53e, 45da, de37dp'
accs = re.split(r', ', accStr)


# a) all the accessions with '5' in them

# iterates through the list of accessions
#for acc in accs:

    # prints the accession iteration if it contains at least one '5'
#    if len(re.findall('[5]', acc)):
#        print(acc)



# b) all the accessions with 'e' or 'd' in them

#for acc in accs:

    # prints the accession iteration if it contains at least one 'd' or one 'e'
#    if len(re.findall('[de]', acc)):
#        print(acc)



# c) contains 'de'?

#for acc in accs:

    # prints the accession iteration if it contains 'de'
#    if len(re.findall(r'de', acc)):
#        print(acc)



# d) contains 'de' with ONE character between the d and e

#for acc in accs:

    # prints the accession iteration if it contains 'dXe'
#    if len(re.findall(r'd.e', acc)):
#        print(acc)



# e) has both 'd' and 'e' in any order

#for acc in accs:

    # prints the accession iteration if it contains 'd' and 'e' anywhere
#    if len(re.findall(r'e', acc)) and len(re.findall(r'd', acc)):
#        print(acc)



# f) starts with x or y

#for acc in accs:

    # prints the accession iteration if it starts with 'x' and 'y'
#    if len(re.findall(r'^[xy]', acc)):
#        print(acc)



# g) starts with x or y and ends with e

#for acc in accs:

    # prints the accession iteration if it starts with 'x' and 'y'
#    if len(re.findall(r'^[xy]', acc)) and len(re.findall(r'e$', acc)):
#        print(acc)

# h) any three numbers

#for acc in accs:

    # prints the accession iteration if it has any 3 numbers
#    if len(re.findall(r'[\d]', acc)) == 3:
#        print(acc)



# i) any three unique numbers

for acc in accs:

    # prints the accession iteration if it has any 3 numbers
    if len(set(re.findall(r'[\d]', acc))) == 3:
        print(acc)



# j)




# l)
