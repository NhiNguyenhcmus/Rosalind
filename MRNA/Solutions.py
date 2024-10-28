"""
Problem: Inferring mRNA from Protein
Version: Sept. 16, 2024
"""

from Bio.Data import CodonTable

def count_rna_strings(protein_sequence):
    # Get the standard codon table
    codon_table = CodonTable.unambiguous_dna_by_name["Standard"]   
    # Create a dictionary to map amino acids to the number of codons that code for them
    codon_usage = {}
    for codon,amino_acid in codon_table.forward_table.items():
        if amino_acid not in codon_usage:
            codon_usage[amino_acid] = 0
        codon_usage[amino_acid] += 1
    codon_usage['Stop'] = len(codon_table.stop_codons)   
    # Count the total number of different RNA strings from which the protein could have been translated, take modulo 1,000,000 at each step
    total_rna_strings = 1   
    for amino_acid in protein_sequence[:-1]:
        total_rna_strings *= codon_usage[amino_acid]
        total_rna_strings %= 1000000   
    total_rna_strings *= codon_usage['Stop']
    total_rna_strings %= 1000000   
    return total_rna_strings

if __name__ == "__main__":
    file_path = input("Enter the path: ")
    with open(f"{file_path}",'r') as file:
        protein_sequence = file.read()
    result = count_rna_strings(protein_sequence)
    print(result)
