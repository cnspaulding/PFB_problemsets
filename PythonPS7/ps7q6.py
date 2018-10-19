#!/usr/bin/env python3

import re

seq_file = open('Python_07_Apol.fasta', 'r')
fasta = seq_file.read()

remove_header=  re.sub(r'>seq1\n', r'', fasta)
print('no header:', remove_header)

#for line in seq_file:
#	line=line.strip()
#	if '>' not in line:
#		headerless.append(line)	
#		print(headerless)
	

for (ApoI) in re.findall(r'[GA]AATT[CT]', remove_header):
	print(ApoI)

#insert cut site into the string
cut_sites =re.sub(r'([AG])(AATT[CT])', r'\1^\2', remove_header)
print(cut_sites)

cut_file = cut_sites.replace('\n','')
print(cut_file)

cut_frags = cut_sites.split('^')
print('cut_frags:', cut_frags)
 
gel_frags = sorted(cut_frags, key=len)
final_gel_frags= gel_frags[::-1]

print(final_gel_frags)
