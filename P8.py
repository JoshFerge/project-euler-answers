PROBLEM 8

k = 1
m = 1
n = 1

a = 0
b = 0
c = 0
foundTriplet = False

def isCoprime(a,b):
	adivs = []
	for i in range(2,a/2):
		if a % i == 0:
			adivs.append(i)

	for i in adivs:
		if b % i == 0:
			return False
	return True

def tripletGenerator(k,m,n):

	if n > m:
		return 0
	if (m - n) % 2 ==0:
		return 0
	if not isCoprime(m,n):
		return 0

	a = k*((m**2)-(n**2))
	b = k*(2*m*n)
	c = k*((m**2)+(n**2))
	# if a == 0:
	# 	return 0
	# print a*b*c
	if a+b+c < 1100:
		print a+b+c
	if a+b+c == 1000:
		print a*b*c
		return a+b+c

def helper():
	for i in range(1,100):
		for j in range(1,100):
			for k in range(1,100):
				if tripletGenerator(i,j,k) == 1000:
					return

helper()