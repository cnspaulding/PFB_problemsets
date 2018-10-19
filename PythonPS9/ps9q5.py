#!/usr/bin/env python3

def gc_content(dna):
	c_count = dna.count('C')
	g_count = dna.count('G')
	dna_len = len(dna)
	gc_content = (c_count + g_count) / dna_len
	return gc_content

dna_string = 'CGTGCTTTCCACGACGGTGACACGCTTCCCTGGA'
dna_gc = gc_content(dna_string)
pc_gc = '{:.2%}'.format(dna_gc)
print('This sequence is' , pc_gc, 'GC')




