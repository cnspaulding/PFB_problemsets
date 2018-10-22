#!/usr/bin/env python3


seq1 = 'agtctgtca'
seq2 = 'gatctctgc'


def compare_seqs(seq1, seq2):
	
	mismatch = 0
	match = 0
	seq1 = []
	seq2 = []
	for nt in seq1:
		seq1.append()
	for nt in seq2:
		seq2.append()

	for pos in range(len(seq1)):
		if seq1[pos] == seq2[pos]:
			match += 1
		else:
			mismatch += 1

	score = match - mismatch
	return print(score)

def reverse_comp(sequence):
	lower_seq = sequence.lower()
	lower_T = lower_seq.replace('a', 'T')
	lower_A = lower_T.replace('t', 'A')
	lower_G = lower_A.replace('c', 'G')
	lower_C = lower_G.replace('g', 'C')
	reverse_comp = lower_C[::-1]
	return reverse_comp 

compare_seqs(seq1, seq2)




#rev_comp = reverse_comp(seq1)
#print(seq1, rev_comp)

