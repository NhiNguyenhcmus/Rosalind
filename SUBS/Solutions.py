"""
Problem: Finding a Motif in DNA
Version: Feb. 04, 2023
"""

s1,s2 = open('rosalind_subs.txt').readlines()
for i in range(len(s1)):
    if s1[i:].startswith(s2):
        print (i+1)
