#!/usr/bin/env python3


sequences=['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
#seq_position labeles the position in the list.:wq

seq_position = 0
#for each seq, print the length, a tab, then the seq.
for seq in sequences:
	seq_position += 1
	print(seq_position, len(seq),'\t', seq)


#here using a list-comprehension tuple:

#[(f, len(f)) for f in ('1', '2', '3')]
tuples = [(len(seq), seq) for seq in sequences]
#print(tuples)

for tuple in tuples:
	print(tuple[0], '\t', tuple[1])
