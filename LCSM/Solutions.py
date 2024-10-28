"""
Problem: Finding a Shared Motif
Version: Sept. 15, 2024
"""

from Bio import SeqIO
# Load sequences from a FASTA file
def sequences_from_fasta(file_path):
    sequences = [str(record.seq) for record in SeqIO.parse(file_path, "fasta")]
    return sequences
# Find the shortest sequences
def shortest_string(sequences):
    min_length = min(len(s) for s in sequences)
    for s in sequences:
        if len(s) == min_length:
            return s
# Find a longest common motif (substring)
def longest_common_motif(sequences):
    # Take the shortest sequence as the reference
    reference_seq = shortest_string(sequences)
    n = len(reference_seq)
    longest_motif = ""
    # Check all possible motif of the reference sequence
    for i in range(n):
        for j in range(i + 1, n + 1):
            candidate = reference_seq[i:j]
            # Check if the candidate motif is the longest common motif
            if all(candidate in str(seq) for seq in sequences):
                if len(candidate) > len(longest_motif):
                    longest_motif = candidate
    return longest_motif
if __name__ == "__main__":
    file_path = input("Enter the path: ")
    sequences = sequences_from_fasta(file_path)
    longest_motif = longest_common_motif(sequences)
    print(f"The longest common motif is: {longest_motif}")
