# Code to find markov transistion matrix

import numpy as np
rows, cols = (4, 4)
# Creating a 2D array in form of a 4 x 4 matrix
markov = []
for i in range(rows):
    col = []
    for j in range(cols):
        col.append(0)
    markov.append(col)

# This is a DNA sequence of immunoglobulingene in micewhich consists of 372 bases
DNA ='tcttctttctggtagcaacagctacaggtgtgcactcccaggtccagctgcagcagtctgggcctgaggtggtgaggcctggggtctcagtgaagatttcctgcaagggttccggctacacattcactgattatgctatgcactgggtgaagcagagtcatgcaaagagtctagagtggattggagttattagtacttacaatggtaatacaaactacaaccagaagtttaagggcaaggccacaatgactgtagacaaatcctccagcacagcctatatggaacttgccagattgacatctgaggattctgccatctattactgtgcaagatactatggtaactactttgactactggggccaaggcacc'

# Creating our markov chain here
for i in range (len(DNA) - 1):
    x = DNA[i]
    y = DNA[i + 1]
    if x == 'a':
        if y == 'a':
            markov[0][0] += 1
        elif y == 'g':
            markov[0][1] +=1
        elif y == 'c':
            markov[0][2] += 1
        elif y == 't':
            markov[0][3] += 1
    elif x == 'c':
        if y == 'a':
            markov[1][0] += 1
        elif y == 'c':
            markov[1][1] += 1
        elif y == 'g':
            markov[1][2] += 1
        elif y == 't':
            markov[1][3] += 1
    elif x == 'g':
        if y == 'a':
            markov[2][0] += 1
        elif y == 'c':
            markov[2][1] += 1
        elif y == 'g':
            markov[2][2] += 1
        elif y == 't':
            markov[2][3] += 1
    elif x == 't':
        if y == 'a':
            markov[3][0] += 1
        elif y == 'c':
            markov[3][1] += 1
        elif y == 'g':
            markov[3][2] += 1
        elif y == 't':
            markov[3][3] += 1

total_pairs = len(DNA) - 1

# Making our transistion matrix here from the given DNA sequence 
for i in range(rows):
    for j in range(cols):
        markov[i][j] = markov[i][j]/total_pairs
        markov[i][j] = round(markov[i][j],2)


base = ['a','c','g','t']

print("DNA sequence: ")
print("\n")
print(DNA)
print("\n")
print("Transition matrix")
print("\n")
print('   ' + base[0] + '     ' + base[1] + '    ' + base[2] + '    ' + base[3])
for i in range(rows):
    print(base[i], end = " ")
    for j in range(cols):
        print(markov[i][j], end = " ")
    print('\n')
