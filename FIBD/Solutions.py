"""
Problem: Mortal Fibonacci Rabbits
Version: Sep. 16, 2024
"""

n = int(input("Number of months: "))
m = int(input("Number of months that rabbits live: "))

# For the 1st month (mean i = 0)
mature_rabbits = [0]
baby_rabbits = [1]
month = [m] # To determine the month that rabbits die. For the 1st month, baby rabbits will die in (m+1)-th month (means i = m)

for i in range(1,n):
	mature_rabbits.append(baby_rabbits[i-1] + mature_rabbits[i-1])
	baby_rabbits.append(mature_rabbits[i-1])
	if baby_rabbits[i] != 0:
		month.append(i+m)
	for j in range(0,len(month)):
		if i == month[j]:
			mature_rabbits[i] = mature_rabbits[i] - baby_rabbits[i-m] # Exclude the died rabbit(s)
			break

sum = mature_rabbits[-1] + baby_rabbits[-1]
print(sum)
