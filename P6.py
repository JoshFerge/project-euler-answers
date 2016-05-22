#PROBLEM 6
primes = [2]
i = 3

while len(primes) != 10001:
	print len(primes)
	isprime = True
	for p in primes:
		if i % p == 0:
			isprime = False

	if isprime == True:
		primes.append(i)
	i+=1

print primes[-1]