#!/usr/bin/env python3


sequences=['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
seq_iter= iter(sequences)

for seq in seq_iter:
	print(len(seq),'\t', seq)


tuples = [(seq, len(seq)) for seq in sequences]

for x in tuples:
	print(tup[1],\t,tup[2]\n)

