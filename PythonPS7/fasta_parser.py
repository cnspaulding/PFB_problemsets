#!/usr/bin/env python3

#make a fasta parser

import re

seqs={}

with open ('Python_07_Apol.fasta', 'r') as dna:	
	for line in dna:
		line = line.rstrip()
		if line.startswith('>'):
			ID = line[1::]
			seqs[ID] = ''

	
	else:
		line = line.rstrip()
		seq.append(line)
		finalstring= ''.join(seq)

		seq[ID] = finalstring

print(ID)
print(finalstring)
print(seqs)
