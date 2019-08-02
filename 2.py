#!/usr/bin/python3
try:
	n = int(input("n: "))
	
	first = 1
	second = 2
	s = 0

	while second <= n:
		if second % 2 == 0:
			s += second
		second += first
		first = second - first 
	print("sum: " + str(s))
except:
	print("Wrong format")
