fi = open('rosalind_cons.txt','r')
ip = fi.read()
dive0 = ip.split("\n>")
dna = []
for i in range(len(dive0)):
	dive1 = dive0[i].split("\n")
	del dive1[0]
	dive1 = ''.join(dive1)
	dna.append(dive1)
def count(a,b,c):
	if a == b: c = 1
	return c
def med(lis1,lis2,a,b):
	for i in range(len(lis1)):
		if a == lis1[i]: b = lis2[i]
	return b
nu = ["A","C","G","T"]
res = str()
A = []
G = []
C = []
T = []
seq = []
c = 0
for i in range(len(dna[0])):
	cA = cC = cG = cT = 0
	for j in range(len(dna)):
		cA+=count(dna[j][i],"A",c)
		cC+=count(dna[j][i],"C",c)
		cG+=count(dna[j][i],"G",c)
		cT+=count(dna[j][i],"T",c)
	cov = [cA, cC, cG, cT]
	seq.append(med(cov,nu,max(cA,cC,cG,cT),res))
	A.append(str(cA))
	C.append(str(cC))
	G.append(str(cG))
	T.append(str(cT))
print(len(A))
print(len(dna[0]))
A = ' '.join(A)
C = ' '.join(C)
G = ' '.join(G)
T = ' '.join(T)
seq = ''.join(seq)
print(seq)
print("A:", A)
print("C:", C)
print("G:", G)
print("T:", T)


		