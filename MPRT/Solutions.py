"""
Problem: Finding a Protein Motif
Version: Sept. 15, 2024
"""

import re
import requests
# Define the N-glycosylation motif
nglyco_motif = re.compile(r'N[^P][ST][^P]')
#Get protein sequence from UniProt using the given UniProt ID
def protein_sequence(uniprot_id):
    url = f"https://www.uniprot.org/uniprot/{uniprot_id}.fasta"
    response = requests.get(url)
    if response.status_code == 200: #A status code that means the request was successful
        fasta_data = response.text
        sequence = ''.join(fasta_data.split('\n')[1:])
        return sequence
#Find and print all N-glycosylation motif positions in the given sequence
def nglyco_sites(sequence):
    positions = []
    for i in range(len(sequence)-3):
        matche = nglyco_motif.finditer(sequence[i:i+4])
        position = [m.start() for m in matche]  
        if position:
            positions.append(i+1)
    return(' '.join(map(str, positions)))
# Read UniProt IDs from a text file and process each ID to find N-glycosylation motif positions
def process_uniprot_ids(file_path):
    with open(file_path, 'r') as file:
        uniprot_ids = file.read().strip().split()   
    for uniprot_id in uniprot_ids:
        sequence = protein_sequence(uniprot_id[:6]) #Process by only 6 characters
        positions = nglyco_sites(sequence)
        if positions:
            print(f"{uniprot_id}")
            print(positions)
if __name__ == "__main__":
    file_path = input("Enter the path: ")
    process_uniprot_ids(file_path)
