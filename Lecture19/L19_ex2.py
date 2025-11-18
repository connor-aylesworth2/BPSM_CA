#!/usr/bin/python

# import necessary packages
import numpy as np
import matplotlib.pyplot as plt

# read in whole E. coli genome, make all of the bases uppercase, remove all of the
#   newline characters, and store the data in a var called 'ecoli'
ecoli = open('/localdisk/data/BPSM/Lecture19/ecoli.txt').read().replace('\n', '').upper()

#
#genome_in = input('What genome do you want to run this analysis on?\nThe default is the E. coli genome.\n') 

segment_in = input('What range of the given genome do you want to run this analysis on?\nThe default is the first 50000 bases of the given genome.\n')

print(type(segment_in))

content_in = str(input('AT or GC content?\nThe default is GC.\n'))

window_in = int(input('Define the size of the window (in bases) that you want to use for this analysis.\nThe default is 1000 bases.\n'))

def GA_temp(window = 1000, segment = 50000, content = 'GC', genome = ecoli):
    print(segment)
    # stores the range that the user of the function wants of the genome they
    #   want in a var called 'seg'
    seg = genome[0:segment]

GA_temp(window_in, segment_in, content_in, genome_in)

# define a function
def Genome_Analysis(window = 1000, segment = 50000, content = 'GC', genome = ecoli):
    print(segment)
    # stores the range that the user of the function wants of the genome they
    #   want in a var called 'seg'
    seg = genome[0:segment]

    # creates two empty lists to store the AT content and GC content 
    #   data that are generated in the follwing for loop
    AT = []
    GC = []

    # iterates through the a range of values from 0 to the user's input
    for start in range(len(seg) - window):
        
        # stores the sequence of the current window iteration in a var called win,
        #   calculates the AT content of the window iteration, and stores the AT
        #   content value in the list called 'AT' made above
        win = seg[start : start + window]
        at = ((win.count('A') + win.count('T')) / window) * 100
        gc = 100 - at
        AT.append(at)
        GC.append(gc)
        
        #
        if content == 'GC':
            cont = GC
        elif content == 'AT':
            cont = AT
        label = cont + 'Content'

        # makes an empty figure of size 20 inches long by 10 inches high, and plots
        #   the content that the user asks for in the newly made figure
        plt.figure(figsize = (20,10))
        plt.plot(cont, label = label, linewidth = 1)

        # sets the x-axis, y-axis, figure title and subtitle, and figure legend
        plt.ylabel('%' + label)
        plt.xlabel('Genomic Position')
        plt.suptitle(label + ' in Given Genome (defualt = E. coli')
        plt.title('First' + str(segment) + 'bases, Window Size of' + str(window))
        plt.legend()

        # saves the resulting plot in a png file to the current working directory
        #   and displays the plot to the screen
        plt.savefig('L19_ex2_out.png', transparent = True)
        plt.show()

#Genome_Analysis(window_in, segment_in, content_in, genome_in)
