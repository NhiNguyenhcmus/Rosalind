"""
Problem: Genome Assembly as Shortest Superstring
Version: Sept. 16, 2024
"""

from Bio import SeqIO
# Load sequences from a FASTA file
def sequences_from_fasta(file_path):
    sequences = [str(record.seq) for record in SeqIO.parse(file_path, "fasta")]
    return sequences
# Find the maximum overlap
def find_overlap(s1, s2):
    max_overlap_len = min(len(s1), len(s2))
    for i in range(max_overlap_len, 0, -1):
        if s1[-i:] == s2[:i]:
            return i
    return 0
# Merge two strings with the largest overlap
def merged_strings(s1, s2):
    overlap_len = find_overlap(s1, s2)
    return s1 + s2[overlap_len:]
# Find the shortest superstring
def superstring(dna_strings):
    while len(dna_strings) > 1:
        max_overlap = 0
        # Find the pair of strings with the maximum overlap
        for i in range(len(dna_strings)):
            for j in range(i + 1, len(dna_strings)):
                overlap = find_overlap(dna_strings[i], dna_strings[j])
                if overlap > max_overlap:
                    max_overlap = overlap
                    seq1, seq2 = dna_strings[i], dna_strings[j]
        # Merge the pair with the largest overlap
        merged_string = merged_strings(seq1, seq2)
        dna_strings.remove(seq1)
        dna_strings.remove(seq2)
        dna_strings.append(merged_string)
    return dna_strings[0]

if __name__ == "__main__":
    file_path = input("Enter the path to the text file: ")
    sequences = sequences_from_fasta(file_path)
    shortest_superstring = superstring(sequences)
    print(f"The shortest superstring is: {shortest_superstring}")
