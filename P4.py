# #PROBLEM 4
def reverse(s):
	new = ""
	for i in s:
		new = i+new
	return new


def isPalindrome(n):
	sn = str(n)
	if sn == reverse(sn):
		return True
	else:
		return False

largestPalindrome = 0

for i in range(100,1000):
	for j in range(100,1000):
		if isPalindrome(i*j) and i*j > largestPalindrome:
			largestPalindrome = i*j
print largestPalindrome
