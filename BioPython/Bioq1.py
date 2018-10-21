#!/usr/bin/env python3

from Bio import SeqIO

for seq_record in SeqIO.parse('Python_08.fasta', 'fasta'):
	print('ID', seq_record.id)
	print('Sequence', str(seq_record.seq))
	print('Length', len(seq_record))
	#Cant get num of seqs
#	print('num of seqs:',(seq_record.seq).count('>'))
	A_count = str(seq_record.seq).count('A')
	C_count = str(seq_record.seq).count('C')
	G_count = str(seq_record.seq).count('G')
	T_count = str(seq_record.seq).count('T')
	nt_count = A_count + C_count + G_count + T_count
	print('nt count', nt_count)
	
avg_length = nt_count/len(seq_record)
print('avg length:', avg_length)
