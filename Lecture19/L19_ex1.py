#!/usr/bin/python

# import necessary packages
import os, sys
import numpy as np
import matplotlib.pyplot as plt

# read in whole E. coli genome, make all of the bases uppercase, remove all of the
#   newline characters, and store the data in a var called 'ecoli'
ecoli = open('/localdisk/data/BPSM/Lecture19/ecoli.txt').read().replace('\n', '').upper()



# a) AT content of first 50,000b?



# stores the first 50000 bases of the E. coli genome in a var called 'eco'
eco = ecoli[0:50000]

# creates an empty list to store the AT content data that is generated in the
#   follwing for loop, and sets the sliding window size to 1000 bases
AT = []
window = 1000

# iterates through a range of values between 0 and 49,000 (the 49,000 comes
#   from the first 50,000 bases of the E. coli genome minus thewindow size)
for start in range(len(eco) - window):
    
    # stores the sequence of the current window iteration in a var called win,
    #   calculates the AT content of the window iteration, and stores the AT 
    #   content value in the list called 'AT' made above
    win = eco[start : start + window]
    AT.append(((win.count('A') + win.count('T')) / window) * 100)

# makes an empty figure of size 20 inches long by 10 inches high, and plots
#   the AT content data generated in the previous code on the newly made figure
plt.figure(figsize = (20,10))
plt.plot(AT, label = 'AT content', linewidth = 1)

# sets the x-axis, y-axis, figure title and subtitle, and figure legend
plt.ylabel('% AT Content')
plt.xlabel('Genomic Position')
plt.suptitle('AT Content in E coli Genome')
plt.title('First 50,000 bases, Window Size of 1000')
plt.legend()

# saves the resulting plot in a png file to the current working directory
#   and displays the plot to the screen
plt.savefig('L19_ex1a_out.png', transparent = True)
plt.show()



# b) first 100,000b?



# stores the first 100000 bases of the E. coli genome in a var called 'eco'
eco = ecoli[0:100000]

# creates an empty list to store the AT content data that is generated in the
#   follwing for loop, and sets the sliding window size to 1000 bases
AT = []
window = 1000

# iterates through a range of values between 0 and 99,000 (the 99,000 comes
#   from the first 100,000 bases of the E. coli genome minus thewindow size)
for start in range(len(eco) - window):

    # stores the sequence of the current window iteration in a var called win,
    #   calculates the AT content of the window iteration, and stores the AT
    #   content value in the list called 'AT' made above
    win = eco[start : start + window]
    AT.append(((win.count('A') + win.count('T')) / window) * 100)

# makes an empty figure of size 20 inches long by 10 inches high, and plots
#   the AT content data generated in the previous code on the newly made figure
plt.figure(figsize = (20,10))
plt.plot(AT, label = 'AT content', linewidth = 1)

# sets the x-axis, y-axis, figure title and subtitle, and figure legend
plt.ylabel('% AT Content')
plt.xlabel('Genomic Position')
plt.suptitle('AT Content in E coli Genome')
plt.title('First 100,000 bases, Window Size of 1000')
plt.legend()

# saves the resulting plot in a png file to the current working directory
#   and displays the plot to the screen
plt.savefig('L19_ex1b_out.png', transparent = True)
plt.show()



# c) whole E. coli genome?



# stores the whole E. coli genome in a var called 'eco'
eco = ecoli

# creates an empty list to store the AT content data that is generated in the
#   follwing for loop, and sets the sliding window size to 1000 bases
AT = []
window = 1000

# iterates through a range of values between 0 and the length of the 
#   E. coli genome - 1000
for start in range(len(eco) - window):

    # stores the sequence of the current window iteration in a var called win,
    #   calculates the AT content of the window iteration, and stores the AT
    #   content value in the list called 'AT' made above
    win = eco[start : start + window]
    AT.append(((win.count('A') + win.count('T')) / window) * 100)

# makes an empty figure of size 20 inches long by 10 inches high, and plots
#   the AT content data generated in the previous code on the newly made figure
plt.figure(figsize = (20,10))
plt.plot(AT, label = 'AT content', linewidth = 0.5)

# sets the x-axis, y-axis, figure title and subtitle, and figure legend
plt.ylabel('% AT Content')
plt.xlabel('Genomic Position')
plt.suptitle('AT Content in E coli Genome')
plt.title('Window Size of 1000')
plt.legend()

# saves the resulting plot in a png file to the current working directory
#   and displays the plot to the screen
plt.savefig('L19_ex1c_out.png', transparent = True)
plt.show()
