"""
Problem: Locating Restriction Sites
Version: Sept. 16, 2024
"""

from Bio.Seq import Seq
from Bio import SeqIO
# Load sequences from a FASTA file
def sequence_from_fasta(file_path):
    for record in SeqIO.parse(file_path, "fasta"):
        sequence = Seq(str(record.seq))
    return sequence
# Check if subsequence is a reverse palindrome
def palindrome(sequence):
    return sequence == str(Seq(sequence).reverse_complement())
# Return positions and lengths of reverse palindromes in DNA sequence
def find_reverse_palindromes(sequence, min_len=4, max_len=12):
    palindromes = []
    seq_len = len(sequence)
    # Find palindromes
    for i in range(seq_len):
        for length in range(min_len, max_len + 1):
            if i + length <= seq_len:
                subseq = sequence[i:i+length]
                if palindrome(subseq):
                    palindromes.append((i + 1, length))
    return palindromes

if __name__ == "__main__":
    # Load DNA sequences
    file_path = input("Enter the path: ")
    sequence = sequence_from_fasta(file_path)
    palindromes = find_reverse_palindromes(sequence)
    for position, length in palindromes:
        print(f"{position} {length}")
