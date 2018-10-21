#!/usr/bin/env python3

from Bio import SeqIO


seq_dict={}
for seq_record in SeqIO.parse('human_cds.fasta', 'fasta'):
	ID = seq_record.id
	Seq = str(seq_record.seq)
	Length = len(seq_record)	
	seq_dict[seq_record.id] = seq_record.seq

	A_count = str(seq_record.seq).count('A')
	C_count = str(seq_record.seq).count('C')
	G_count = str(seq_record.seq).count('G')
	T_count = str(seq_record.seq).count('T')
	
	
	#nt_count = A_count + C_count + G_count + T_count
	#print('nt count', nt_count)
	
#	print('A:', A_count, 'G:', G_count, 'C:', C_count, 'T:', T_count)
	
	percent_GC = (G_count + C_count) / Length
#	print(percent_GC)

	print(ID,'\t', percent_GC)
	
