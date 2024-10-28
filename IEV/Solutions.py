"""
Problem: Calculating Expected Offspring
Version: Feb. 1, 2023
"""

fi = open("rosalind_iev.txt","r")
num = fi.read()
num = num.split(" ")
pht = ["AA-AA","AA-Aa","AA-aa","Aa-Aa","Aa-aa","aa-aa"]
for i in range(len(num)):
	num[i] = int(num[i])
	print("Number of",pht[i], num[i])
resA_ = 2 * ( num[0] + num[1] + num[2] + 0.75*num[3] + 0.5*num[4])
print(resA_)
