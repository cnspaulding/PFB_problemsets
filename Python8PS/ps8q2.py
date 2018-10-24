#!/usr/bin/env python3

from Bio import SeqIO

fasta_lib ={}
codon= ''

for seq_record in SeqIO.parse('Python_08.fasta', 'fasta'):
	ID =  seq_record.id
	Seq =  str(seq_record.seq)

	for cod in range(0, len(Seq), 3):
		codon += Seq[cod:cod+3] + ' '  

	fasta_lib[ID] = codon
	
	codon = ''
	print(fasta_lib)



