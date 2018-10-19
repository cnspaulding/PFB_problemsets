#!/usr/bin/env python3

import re

poem_file = open('Python_07_nobody.txt', 'r')
poem= poem_file.read()

found = re.findall(r'Nobody', poem)
#print(found)

for found in re.finditer(r'Nobody', poem):
	occur = found.group(0)
	position = found.start(0)+1
	print(occur, position)
		

	


