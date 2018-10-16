#!/usr/bin/env python3

#script for question 8

import sys

count = int(sys.argv[1])

if count >0:
	print('positive')
#	if count%2 < 1:
#		print('count is even')
	if count < 50:
		print('count is less than 50')
		if count%2 < 1:
			print('count is less than 50 and even')
	elif count == 50:
		print('equals 50')

	else: 
		print('count is > 50')
		if count%3 == 0:
			print('it is larger than 50 and divisible by 3')
		
#	elif count < 50 and count%2 <1:
#		print('count is even and smaller than 50')
#	elif count > 50 and count/3==1:
#		print('it is larger than 50 and divisible by 3')

elif count < 0:
	print('negative')

else:
	print('count equals 0')

