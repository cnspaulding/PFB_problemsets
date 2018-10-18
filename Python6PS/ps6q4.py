#!/usr/bin/env python3

file_object = open('Python_06.fastq', 'r')

total_char= 0
line_num=[]
for line in file_object:
	line = line.strip()
	line_num.append(line)
	char_line = len(line)
	total_char += char_line
	
Avg_lineLength = (total_char/(len(line_num)))


print('Total characters:',total_char, 'Number of lines:', len(line_num), 'Avg line length:', Avg_lineLength)


