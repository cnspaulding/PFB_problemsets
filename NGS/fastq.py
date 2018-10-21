#!/usr/bin/env python3

from Bio import SeqIO

trimmed_qual= ''
trimmed_seq= ''
trimmed_ID = ''
QC30 = 0
for seq_record in SeqIO.parse('four_reads.fastq', 'fastq'):
	qual = seq_record.letter_annotations['phred_quality']
	ID = seq_record.id
	seq = seq_record.seq

#	print(ID)
	trimmed_qual = qual[5:]
	trimmed_seq = seq[5:]
	trimmed_ID = ID[5:]

#	print(seq)
#	print(trimmed_seq)
	for value in qual:
		if value >= 30: 
			QC30 += 1

	print(QC30)	
	QC30 = 0
