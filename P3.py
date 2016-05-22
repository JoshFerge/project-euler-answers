# PROBLEM 3
facts = []
t = 2
n = 600851475143
while n != 1:
	if n%t == 0:
		facts.append(t)
		n = n/t
		print facts
	else:
		t=t+1