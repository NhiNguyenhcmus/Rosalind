"""
Problem: Open Reading Frames
Version: Sept. 15, 2024
"""

from Bio.Seq import Seq
from Bio import SeqIO
# Load sequences from a FASTA file and reverse comlement sequence
def sequences_from_fasta(file_path):
    for record in SeqIO.parse(file_path, "fasta"):
        sequence = Seq(str(record.seq))
        reverse_sequence = sequence.reverse_complement()
        sequences = [sequence,reverse_sequence]
    return sequences
# Find ORFs in DNA sequence
def orfs_in_sequence(sequence):
    orfs = []
    for i in range(len(sequence)-5): # Eliminate cases where start codon (ATG) appears at the end of the sequence and there is no stop codon (TAA, TAG, TGA) behind it.
        codon = sequence[i:i+3]
        if codon == "ATG":
            start = i
            for j in range(i+3, len(sequence)-2, 3):
                codon = sequence[j:j+3]
                if codon in ["TAA","TGA","TAG"]:
                    end = j+3
                    orfs.append(sequence[start:end])
                    break
    return orfs
  
if __name__ == "__main__":
    file_path = input("Enter the path: ")
    sequences = sequences_from_fasta(file_path)
    # Translate to candidate protein string from ORFs
    proteins = []
    for s in sequences:
        orfs = orfs_in_sequence(s)
        for orf in orfs:
            proteins.append(Seq(orf).translate())
    proteins = list(set(proteins)) # Remove the similar candidate protein strings
    for p in proteins:
        print(p[:-1]) # Remove "*" in the end
