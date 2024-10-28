"""
Problem: Counting Point Mutations
Version: Jan. 2, 2023
"""

fi = open('rosalind_hamm.txt','r')
lines = fi.readlines()
print([ a!=b for (a, b) in zip(lines[0], lines[1])].count(True))
