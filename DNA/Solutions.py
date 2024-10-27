"""
Counting DNA Nucleotides
Version: Dec. 28, 2022
"""

f = open('rosalind_dna.txt', 'r')
nu = f.read()
def dna(s):
      return s.count("A"), s.count("G"), s.count("C"), s.count("T")
print(dna(nu))
