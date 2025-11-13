#!/localdisk/home/s2837739/Exercises/Lecture17/playtime/bin/python

import os, sys
import numpy as np
import pandas as pd

df = pd.read_csv('eukaryotes.txt', sep = '\t', na_values = ['-'])


# 1) fungi with >100Mb bases? 

# use below code to look for fungi identifier in column 'group'
#print(df.columns)
#print(df['Group'])

# stores the entries in the original df that are of group fungi and are of size (Mb)
#   greater than 100 Mb in a new df
#big_fungi = df[df.apply(lambda x : x['Group'] in ['Fungi'] and x['Size (Mb)'] > 100, axis = 1)] 

# reports the amount of entries of the original dataframe that fulfil the
#   above criteria
#print('There are ',len(big_fungi), 'fungi with genomes of 100Mb or greater.')

# grabs the names of the new df made above and prints a list of them
#big_f_names = big_fungi['#Organism/Name']
#print(list(big_f_names))



# 2) sequenced entries in each kingdom?

# gets the (redundant) number of entries in the df that are of group plants, 
#   animals, fungi and protists, stores those values in seperate variables, and 
#   reports the values in a print statement
#plant = len(df[df['Group'] == 'Plants']) 
#fungi = len(df[df['Group'] == 'Fungi'])
#animal = len(df[df['Group'] == 'Animals'])
#protist = len(df[df['Group'] == 'Protists'])

#print('Of plants, animals, fungi and protists in the dataframe, ', plant, ',', animal,',', fungi,'and', protist, 'have been sequenced, respectively.')



# 3) Heliconius have been sequenced?

# grabs all of the lines in the original df that start with heliconius and puts it in a var called Hbutts :)
#Hbutts = df[df.apply(lambda x : x['#Organism/Name'].startswith('Heliconius'), axis = 1)]

# prints the name and scaffold contents of the var made above
#print(Hbutts[ ['#Organism/Name', 'Scaffolds'] ])



# 4) center with most plant seqs? most insect seqs?

# stores all of the plant entries in a var and prints the amount of entries from each center
#Ps = df[df['Group'] == 'Plants']
#print(Ps['Center'].value_counts())

# stores all of the insects entries in a var and prints the amount of entries from each center
#Is = df[df['SubGroup'] == 'Insects']
#print(Is['Center'].value_counts())



# 5) make a column with proteins/genes. Which entries have at least 10% more proteins than genes?

df['Prots/Gene'] = df['Proteins'] / df['Genes']

df5 = df[df['Prots/Gene'] >= 1.1]
print(df5)

