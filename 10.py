import math

def isPrime(n):
	if (n == 1):
		return False
	if (n == 2):
		return True

	m = int(math.sqrt(n))

	ok = True
	for i in range(2, m + 1):
		if (n % i == 0):
			ok = False
			break

	return ok

s = 2
i = 3

while (True):

		if (isPrime(i)):
			if (i < 2000000):
				s += i	
			else:
				break
		i += 2

print(s)