#!/usr/bin/env python3
# use sys to add a count from the command line.  When entered on command line, comes in as a string, so you have to make it an int or float first.
import sys

count = int(sys.argv[1])

if count > 100:
	print('True')

else:
	print('False')
