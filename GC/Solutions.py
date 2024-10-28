"""
Problem: Computing GC Content
Version: Jan. 2, 2023
"""

fi = open('rosalind_gc.txt','r')
seq0 = fi.read()
fi.close()
dive0 = seq0.split("\n>")
count = len(dive0)
GC = []
GC_num = 0
seq_num = 0
GC_con = 0
for i in range (0,count):
	dive1 = dive0[i].split("\n")
	for j in range (0,len(dive0[i])):
		if dive0[i][j] == "G" or dive0[i][j] == "C":
			GC_num +=1
	for t in range (1,len(dive1)):
		seq_num = seq_num + len(dive1[t])
	GC_con = GC_num*100/seq_num
	GC.append(GC_con)
	seq_num = 0
	GC_num = 0
for i in range (0, len(GC)):
	if GC[i] == max(GC):
		dive2 = dive0[i].split("\n",1)
		print(dive2[0])
print(max(GC))
