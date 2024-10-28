"""
Problem: Independent Alleles
Version: Sep. 16, 2024
"""

import math
# Get user inputs
k = int(input("Enter k_value:")) # k-th generation of Tom's family tree
N = int(input("Enter N_value:")) # AaBb organisms
result = 0
organims_k_th = 2**k
if k == 0: print(result = 1) # Only Tom (AaBb)
if N > organims_k_th: print(result) # No such case
"""
    AaBb = 1/4
    Other gentypes = 3/4
"""
if N == organims_k_th: # All of organisms in k-th generation of Tom's family tree is AbBb
    result = (1/4)**organims_k_th
elif N == 1:
    result = 1 - ((3/4)**organims_k_th) # Exclude the case which have no organisms in k_th generation
else:
    m = ((3/4)**organims_k_th)
    for i in range (1, N):
        m = m + math.comb(organims_k_th,i)*((1/4)**i)*((3/4)**(organims_k_th-i))
        # Exclude the cases which have (0,1,...,N-1) organisms in k_th generation
    result = 1 - m   
print(round(result,3))
