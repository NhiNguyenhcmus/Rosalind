"""
Problem: Rabbits and Recurrence Relations
Version: Jan. 2, 2023
"""

n = int(input("Nhap so thang "))
k = int(input("Nhap so cap moi lua "))
if n <= 0:
	print ("Nhap so thang lon hon 0!")
elif n == 1 or n == 2:
	print ("Tong so cap tho = 1")
else:
	num = [1 for j in range(0,n)]
for i in range(2,n):	
		num[i] = num[i-1] + k*num[i-2]
print(num[-1])

"""
Problem: Rabbits and Recurrence Relations
Version: 
"""

