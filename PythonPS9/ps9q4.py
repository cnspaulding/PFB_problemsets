#!/usr/bin/env python3

import sys

fasta_file = sys.argv[1]
width = sys.argv[2]


fasta_dict = {}

fasta_file = open(fasta_file, 'r')
for line in fasta_file:
	line=line.rstrip()
	if line.startswith('>'):
		header = line[1::].split()
		gene_ID = header[0]			
		fasta_dict[gene_ID]= ''

	else:
		fasta_dict[gene_ID] += line		

def dna_length(sequence, width):
	out_put= ''
	sequence= sequence.replace('\n', '')
	for i in range(0,len(sequence), width):
		out_put += sequence[i:i+width] + '\n' 
	return out_put		


fo = open('fastaoutput.txt', 'w')

out_put = ''

for key in fasta_dict:
	out_put=dna_length(fasta_dict[key], int(width))
#	print(fasta_dict[key])

	fo.write('>'+key+'\n'+out_put)








