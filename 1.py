#!/usr/bin/python3
try:
	n = int(input("n: "))
	s = 0
	for i in range(1, n):
		if i % 3 == 0 or i % 5 == 0:
			s += i
	print("sum: " + str(s))
except:
	print("Wrong format")	
