#!/usr/bin/env python3

import re

seq_file = open('Python_07.fasta.txt', 'r')
fasta = seq_file.read()


for (id_name, description) in re.findall(r'>(\S+)(.+)' , fasta):
	print('ID:',id_name,'Desc:', description)

	



