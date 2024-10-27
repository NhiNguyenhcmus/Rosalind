"""
Problem: Complementing a Strand of DNA
Version: Dec. 28, 2022
"""

fi = open('rosalind_revc.txt','r')
DNAb = fi.read()
sc = DNAb.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()[::-1]
print(sc)
