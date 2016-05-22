# PROBLEM 5

n = 1000000

smallest = 0

while n < 1000000000000000:
	isgood = True
	for i in range(10,21):
		if n%i != 0:
			isgood = False

	if isgood == True:
		smallest = n
		print smallest
		break
	n = n +1
	if n % 100000 == 0:
		print n
print smallest