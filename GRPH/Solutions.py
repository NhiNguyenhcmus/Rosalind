"""
Problem: Overlap Graphs
Version: Sep. 16, 2024
"""

from Bio import SeqIO

# Open DNA strings file
file_path = input("Enter the path to the text file containing DNA strings: ")

# Load sequences from a FASTA file
sequences = [str(record.seq) for record in SeqIO.parse(file_path, "fasta")]
names = [str(record.id) for record in SeqIO.parse(file_path, "fasta")]

# Collect 3 nuleotides at the beginning and end of the sequence
begin = []
end = []
for i in range(len(sequences)):
	end.append(sequences[i][-3:])
	begin.append(sequences[i][0:3])

# Find the pairs of strings with the 3 nucleotides overlap
for i in range(len(end)):
	for j in range(len(begin)):
		if end[i] == begin[j] and i != j:
				print(names[i],names[j])
