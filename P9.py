#PROBLEM 9

#USING SEIVE

g = range(2,2000000)

p = 0

while g[p] < 3000:
	print g[p]
	g = [x for x in g if x%g[p] !=0 or x == g[p] ]

	p+=1

print sum(g)