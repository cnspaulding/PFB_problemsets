#!/usr/bin/env python3

file_object = open('Python_06.txt', 'r')
seq_write = open('Python_06_uc.txt', 'w')


#file_object = open('Python_06.txt', 'r')
for line in file_object:
	line= line.rstrip()
	line= line.upper()
	print(line)
	new_line= line + '\n'	
	seq_write.write(new_line)

file_object.close()
seq_write.close()
