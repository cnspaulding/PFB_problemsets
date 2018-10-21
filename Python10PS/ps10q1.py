#!/usr/bin/env python3

class DNAsequence(object):

	def __init__(self, sequence, gene_name, species_name):
		self.sequence = sequence
		self.gene_name = gene_name
		self.species_name = species_name

	def length(self):
		length = len(self.sequence)
		return length

	def nt_composition(self):
		a_count = self.sequence.count('A')
		t_count = self.sequence.count('C')
		g_count = self.sequence.count('G')
		c_count = self.sequence.count('C')
		nt_count = {'A': a_count, 'C': c_count, 'G': g_count, 'T:': t_count}
		return nt_count


	def GC_content(self):
		GC_content = (self.nt_composition()['G'] + self.nt_composition()['C']) / self.length()
		return GC_content
	
	def fasta_format(self):
		fasta_format = '>'+self.gene_name+'\n'+ self.sequence
		return fasta_format 		

	def same_seq(self, dna_obj):
		if self.sequence == dna_obj.sequence & self.gene_name == self.gene_name &self.species_name == self.species_name: 
			return true
			

dna_rec_obj_1 = DNAsequence('AAAA', 'ABC1', 'Escherichia coli')
dna_rec_obj_2 = DNAsequence('CGCG', 'FimH', 'Escherichia coli')

for d in [ dna_rec_obj_1, dna_rec_obj_2 ]:
	print('name:' , d.gene_name, ' ', 'seq:', d.sequence)
	print('seq length:',d.length())
	print('nt content:',d.nt_composition())
	print('GC content:', d.GC_content())
	print(d.fasta_format())
	print(d.same_seq())
