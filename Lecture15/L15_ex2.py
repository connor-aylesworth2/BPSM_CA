#!/usr/bin/python

# 2)

# define the function for AA contents such that it takes two parameters,
#   a seq and a single AA
def AA_content(seq, AAs = ['A', 'I', 'L', 'M', 'F', 'W', 'Y', 'V']):
    
    # checks if the AA input is a list and throughs an error if it's not
    if type(AAs) != list:
        print('AA parameter must be a list')
        return
    
    # formats the inputted seq and sets a total content variable to 0
    seq = str(seq).upper()
    total_cont = 0

    # checks the content of each AA from the given list of AAs in 
    #   the given sequence and adds each content to the total content var
    for AA in AAs:
        AA = str(AA).upper()
        ocs = seq.count(AA)
        content = round((ocs / len(seq)) * 100)
        total_cont += content
    
    #returns the total content
    return total_cont

# tests the function against a series of inputs
assert round(AA_content("MSRSLLLRFLLFLLLLPPLP", ["M"])) == 5
assert round(AA_content("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L'])) == 70
assert round(AA_content("MSRSLLLRFLLFLLLLPPLP")) == 65
