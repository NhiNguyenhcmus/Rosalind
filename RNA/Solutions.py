"""
Problem: Transcribing DNA into RNA
Version: Dec. 28, 2022
"""

fi = open('rosalind_rna.txt','r')
RNA = fi.read()
print(RNA.replace("T", "U"))
