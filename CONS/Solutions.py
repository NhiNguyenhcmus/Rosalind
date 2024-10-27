"""
Problem: Consensus and Profile (https://rosalind.info/problems/cons/)
Version: Jan. 12, 2023
"""

fi = open('rosalind_cons.txt','r')
ip = fi.read()
dive0 = ip.split("\n>")
dna = []
for i in range(len(dive0)):
	dive1 = dive0[i].split("\n")
	del dive1[0]
	dive1 = ''.join(dive1)
	dna.append(dive1)
def count(a,b,c):
	if a == b: c = 1
	return c
def med(lis1,lis2,a,b):
	for i in range(len(lis1)):
		if a == lis1[i]: b = lis2[i]
	return b
nu = ["A","C","G","T"]
res = str()
A = []
G = []
C = []
T = []
seq = []
c = 0
for i in range(len(dna[0])):
	cA = cC = cG = cT = 0
	for j in range(len(dna)):
		cA+=count(dna[j][i],"A",c)
		cC+=count(dna[j][i],"C",c)
		cG+=count(dna[j][i],"G",c)
		cT+=count(dna[j][i],"T",c)
	cov = [cA, cC, cG, cT]
	seq.append(med(cov,nu,max(cA,cC,cG,cT),res))
	A.append(str(cA))
	C.append(str(cC))
	G.append(str(cG))
	T.append(str(cT))
print(len(A))
print(len(dna[0]))
A = ' '.join(A)
C = ' '.join(C)
G = ' '.join(G)
T = ' '.join(T)
seq = ''.join(seq)
print(seq)
print("A:", A)
print("C:", C)
print("G:", G)
print("T:", T)

"""
Problem: Consensus and Profile (https://rosalind.info/problems/cons/)
Version: Sept. 16, 2024
"""
from Bio import SeqIO
import numpy as np

# Read sequences from the FASTA file
def profile_and_consensus(fasta_file):
    sequences = [str(record.seq) for record in SeqIO.parse(fasta_file, "fasta")]
    
    seq_len = len(sequences[0])

    # Initialize profile matrix (4 rows for 'A', 'C', 'G', 'T' and columns based on sequence length)
    profile = np.zeros((4, seq_len), dtype = int)

    # Map nucleotides to row indices
    nucleotide_index = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

    # Fill the profile matrix by counting occurrences of each nucleotide
    for seq in sequences:
        for idx, nucleotide in enumerate(seq):
            if nucleotide in nucleotide_index:
                profile[nucleotide_index[nucleotide], idx] += 1

    # Generate the consensus string
    consensus = []
    for i in range(seq_len):
        max_nuc = np.argmax(profile[:, i])
        consensus.append("ACGT"[max_nuc])
    
    # Return the consensus string and the profile matrix
    return ''.join(consensus), profile

def profile_matrix(profile):
    # Nucleotide labels
    nucleotides = ["A", "C", "G", "T"]
    
    # Construct a readable string for the profile matrix
    profile_matrix = ""
    for i, nucleotide in enumerate(nucleotides):
        profile_matrix += f"{nucleotide}: " + ' '.join(map(str, profile[i])) + "\n"
    
    return profile_matrix

if __name__ == "__main__":
    fasta_file = input("Enter the path to the text file: ")
    consensus, profile = profile_and_consensus(fasta_file)
    
    print(consensus)
    
    # Display the profile matrix
    print(profile_matrix(profile))
