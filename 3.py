import math

primes = set()

def isPrime(n):

	if (n == 2):
		return True

	if (n in primes):
		return True

	m = int(math.sqrt(n))
	ok = True
	for i in range(2, m + 1):
		if (n % i == 0):
			ok = False
			break

	return ok

n = int(input())
m = int(math.sqrt(n))

for i in range(2, m):
	if (n % i == 0 and isPrime(i)):
		primes.add(i)
		primeFactor = i

print(primeFactor)
