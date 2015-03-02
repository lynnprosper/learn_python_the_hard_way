i = 0
numbers = []

for i in range(0, 7):
	print("Ar the top i is %d" % i)
	numbers.append(i)
	i += 1
	print("Numbers now: ", numbers)
	print("At the bottom i is %d" % i)
	
print("The numbers: ")
for num in numbers:
	print(num)