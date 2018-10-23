#!/usr/bin/env python3

from Bio import SeqIO

fasta_dict = {}

for seq_record in SeqIO.parse('ecoliPB.fasta', 'fasta'):
	fasta_dict[seq_record.id]=seq_record.seq

length =[]
#put contigs into value of dict, sort by size then pull out the max and min
for key in fasta_dict:
	length.append(len(fasta_dict[key]))

#sort by size
length = sorted(length)
max_length = length[-1]
min_length = length[0]
reverse_length = length[::-1]
sum_allcontigs = sum(length)
half_sum = (sum_allcontigs)/2

#print(fasta_dict[key])
#min_length = min(length)
#max_length = max(length)

#print(len(fasta_dict))
#print('length:', length, 'min:', min_length, 'max:', max_length)
#print(sum_allcontigs, half_sum)

#The N50 value is calculated by first ordering every contig/scaffold by length from longest to shortest. Next, starting from the longest contig/scaffold, the lengths of each contig are summed, until this running sum equals one-half of the total length of all contigs/scaffolds in the assembly.

print(sum_allcontigs, half_sum, length)
contig_list = []
contig_sumcount = 0
L50 = []
N50= []

for contig in reverse_length:
	if contig_sumcount <  half_sum:
		contig_sumcount += contig
		contig_list.append(contig)

L50 = len(contig_list)
N50 = contig_list[-1]
		
print(N50, L50)

