#!/usr/bin/env python3

#script for question 8

import sys

count = int(sys.argv[1])

if count >0:
	print('positive')
	if count < 50:
		print('count is smaller than 50')
	if count%2 < 1:
		print('count is even')

elif count < 0:
	print('negative')

elif count is 0:
	print('count equals 0')

