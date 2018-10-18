#!/usr/bin/env python3

import sys
start = int(sys.argv[1])
end = int(sys.argv[2])

#num = start

while start <= end:
	if start%2==0:
		print(start)	
	start += 1	

#this way is not fully working.
#numbers= range(start,end)

#for number in numbers:
#	print(number)
#	num += 1
#(num[number1:number2])
