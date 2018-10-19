#!/usr/bin/env python3



def reverse_comp(dna):

	replaceA = dna.replace('A', 't')
	replaceT = replaceA.replace('T', 'A')
	replaceC = replaceT.replace('C', 'g')
	replaceG = replaceC.replace('G', 'C')

#This will read the dna string backwards.
	reverse_dna = replaceG[::-1]
#make everything the same case
	reverse_comp = reverse_dna.upper()
	return reverse_comp	

dna_string= 'CGTGCTTTCCACGACGGTGACACGCTTCCCTGGA'
Comp = reverse_comp(dna_string)

print('revComp_sequence:', Comp)
