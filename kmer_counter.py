#!/usr/bin/env python3

from Bio import SeqIO
import sys
#can type in the length of the kmer you want on the command lien
length = sys.argv[1]
kmer_len = int(length)
num_toprint = sys.argv[2]
num_toprint = int(num_toprint)
kmer_dict = {}

for seq_record in SeqIO.parse('reads.fq', 'fastq'):
	seq = str(seq_record.seq)
#	print(type(seq))
#print deq with every 8bp option:wq
	for kmer in range(0, len(seq)):
		key = seq[kmer:kmer+kmer_len]
#set so that you won't get any kmers shorter than your defined length, like those found at the end of the lines
		if len(key) == kmer_len:
			if key not in kmer_dict:
				kmer_dict[key] = 1
			else:		
				kmer_dict[key] += 1

sorted_kmers ={}
sorted_kmers = sorted(kmer_dict.keys(), key = lambda x: kmer_dict[x], reverse=True)		
counter = 0
for kmer in sorted_kmers:
	if counter <= num_toprint:
		count = kmer_dict[kmer]
		top_ten= '{}\t{}'.format(kmer, count)	
		counter += 1
		print(top_ten)
