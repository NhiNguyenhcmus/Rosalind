"""
Problem: Mendel's First Law
Version: Jan. 4, 2023
"""

k = int(input("Nhap so ca the dong troi: "))
m = int(input("Nhap so ca the di hop: "))
n = int(input("Nhao so ca the dong lan: "))
def GT(n):
	gt = 1
	if n > 1:
		for i in range(2,n+1): gt = gt*i
	return gt
inv = k + m + n
SUM = GT(inv)/(GT(2)*GT(inv-2))
if k > 1:
	AAAA = GT(k)/(GT(2)*GT(k-2))
else: AAAA = 0
if m > 1:
	AaAa = GT(m)/(GT(2)*GT(m-2)) * 3/4
else: AaAa = 0
AAAa = k*m
AAaa = k*n
Aaaa = m*n*0.5
A_gen = AAAA + AAAa + AaAa + AAaa + Aaaa
result = A_gen/SUM
print(result)
