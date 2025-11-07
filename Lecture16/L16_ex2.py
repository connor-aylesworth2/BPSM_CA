#!/usr/bin/python



# define a function that takes a sequence of DNA and returns a string that is 
#   the reverse complement of that sequence
def reverse_complement(seq):
    
    # sets the seq variable to the reverse sequence of the original seq
    seq = seq[::-1]

    #replaces all As, Ts, Cs, and Gs with Ws, Xs, Ys, and Zs, respectively
    seq = seq.replace("A", "W").replace("T", "X").replace("C", "Y").replace("G", "Z")

    #replaces all Ws, Xs, Ys, and Zs with Ts, As, Gs, and Cs, respectively
    seq = seq.replace("W", "T").replace("X", "A").replace("Y", "G").replace("Z", "C")
    
    return seq



# define a function that takes a sequence of dna and returns a list of the codons of 
#   that sequence
def get_codons(seq, frame = 1):
    
    # defines an empty list to store the codons generated from the sequence
    codons = []
    
    if frame < 0:
        seq = reverse_complement(seq)
    # sets the start and end of the codon window based on the frame that the function
    #   is called with
    if frame == 1 or frame == -1:
        win_s = 0
        win_e = 3
    elif frame == 2 or frame == -2:
        win_s = 1
        win_e = 4
    elif frame == 3 or frame == -3:
        win_s = 2
        win_e = 5

    # generates codons and stores them in the empty list made above
    while win_s <= (len(seq) - 1):
        codons.append(seq[win_s:win_e])
        win_s += 3
        win_e += 3
    
    # returns the list of codons generated
    return codons



# defines a function that takes a list of codons and returns a string of aas
def translate(seq, frame = 1):
    
    codons = get_codons(seq, frame)

    # define a translation table as a dict
    gencode = {
            'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
            'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
            'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
            'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
            'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
            'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
            'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
            'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
            'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
            'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
            'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
            'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
            'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
            'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
            'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
            'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}
    
    # define an empty list to store translated aas
    pp = []
    
    # translates each codon in the inputted list of codons into an aa and 
    #   stores the generated aas in the list made above
    for codon in codons:
        if gencode.get(codon) is not None:
            pp.append(gencode.get(codon))
    
    #returns the resulting string of concatenated aas from the pp list
    return ''.join(pp)
    


# sets a sequence to translate in a var called seq, translates it and stores
#   the translation in a var called pp (polypeptide), and prints the pp
seq = 'ATGTTCGGT'
pp = translate(seq, -2)

print(pp)



