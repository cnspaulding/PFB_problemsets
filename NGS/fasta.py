#!/usr/bin/env python3

#from Bio import SeqIO

#filename = 'human_cds.fasta' 

#id_dict = SeqIO.to_dict(SeqIO.parse('human_cds.fasta', 'fasta'))

#print(id_dict)

#for 
#A_count = str(seq_record.seq).count('A')
#C_count = str(seq_record.seq).count('C')
#G_count = str(seq_record.seq).count('G')
#T_count = str(seq_record.seq).count('T')
#nt_count = A_count + C_count + G_count + T_count
#print('nt count', nt_count)

import re

seqs={}
seq = ''
finalstring = ''

with open ('human_cds.fasta', 'r') as dna:	
	for line in dna:
		line = line.rstrip()
		if line.startswith('>'):
			ID = line[1::]
			seqs[ID] = ''

	
	else:
		line = line.rstrip()
		seq.append(line)
		finalstring= ''.join(seq)

		seqs[ID] = finalstring

print(seqs)
