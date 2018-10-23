#!/usr/bin/env python3

from Bio import SeqIO

fasta_dict = {}

for seq_record in SeqIO.parse('ecoliPB.fasta', 'fasta'):
	fasta_dict[seq_record.id]=seq_record.seq

length =[]

for key in fasta_dict:
	length.append(len(fasta_dict[key]))

min_length = min(length)
max_length = max(length)


print(len(fasta_dict))
print('min:', min_length, 'max:', max_length)





	

