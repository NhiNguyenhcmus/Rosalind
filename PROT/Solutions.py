"""
Problem: Translating RNA into Protein
Version: Jan. 4, 2023
"""

ip = open('rosalind_prot.txt','r')
RNA = ip.read()
fi = open('codon.txt','r')
lines = fi.readlines()
protein = []
for i in range(0,len(RNA)-1):
	if i == 0 or i % 3 == 0:
		for j in range(0,len(lines)):
			if RNA[i:i+3] == lines[j][0:3]: protein.append(lines[j][4])
print(''.join(protein))
