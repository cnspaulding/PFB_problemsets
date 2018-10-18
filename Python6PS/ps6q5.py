#!/usr/bin/env python3

 
alpaca_genes = open('alpaca_all_genes.tsv', 'r')
alpaca_stem = open('alpaca_stemcellproliferation_genes.tsv', 'r')
alpaca_pigment = open('alpaca_pigmentation_genes.tsv', 'r')

all_genes= set()
for line in alpaca_genes:
	line = line.strip()
	all_genes.add(line)

	print(all_genes)


pig_list_set = set()

for line in alpaca_pigment:
	line= line.strip()
	pig_list.append(line)
	pig_list.add(line)

print(pig_list)
stem_list = set()
for line in alpaca_stem:
	line= line.strip()
	stem_list.add(line)

	
