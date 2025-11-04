#!/usr/bin/python

# 1)

# define the function for AA contents such that it takes two parameters,
#   a seq and a single AA
def AA_content(seq, AA):
    
    # checks if AA parameter is one AA, and if not it throughs an error and stops
    if len(AA) > 1:
        print('this function only checks the AA content of a seq relative to one particular AA. Please try again with the AA parameter set to one AA.')
        return
    
    # stores the two inputs in variables, and formats the inputs for analysis
    seq = str(seq).upper()
    AA = str(AA).upper()

    # calculates the content of the given AA in the given sequence
    ocs = seq.count(AA)
    content = round((ocs / len(seq)) * 100)

    # stores an alternative string output with a % on it
    AA_con = str(content) + '%'

    # returns the integer of the percentage of the given AA in the given seq
    return content

# tests the function against a series of inputs
assert AA_content('MSRSLLLRFLLFLLLLPPLP', 'M') == round(5)
assert AA_content('MSRSLLLRFLLFLLLLPPLP', "r") == round(10)
assert AA_content('MSRSLLLRFLLFLLLLPPLP', "L") == round(50)
assert AA_content('MSRSLLLRFLLFLLLLPPLP', "Y") == round(0)
    



