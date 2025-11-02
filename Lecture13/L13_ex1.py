#!/usr/bin/python3



### Exercise 1 ###



#read in and format the input file content and store contents in a variable
input_connect = open('/localdisk/home/data/BPSM/Lecture13/input.txt')
seq_list = input_connect.read().rstrip('\n').upper().split()
input_connect.close()

#stores the seq adapter in a variable, sets a counter at 0, iterates through
#each item of the seq list, removes ALL occurences of the adapter seq from
#said items, and prints the length of each trimmed seq
adapter = "ATTCGATTATAAGC"
counter = 0

for seq in seq_list:
    seq = seq.replace(adapter, "")
    seq_list[counter] = seq
    print(len(seq_list[counter]))
    counter += 1

#reverts the list of seqs back into srings seperated by new lines and stores 
#said seqs in a variable
trimmed_seqs = "\n".join(seq_list)

#stores the trimmed seqs in a new file called E1_output.txt
output_connect = open('E1_output.txt', 'w')
output_connect.write(trimmed_seqs)
output_connect.close()


