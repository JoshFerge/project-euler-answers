#PROBLEM 2

numl2 = 1
num = 2
accum = 2
while num < 4000000:
	temp = num
	num = num+numl2

	if num > 4000000:
		break
	# print num
	if num % 2 == 0:
		accum +=num
	numl2 = temp
print accum