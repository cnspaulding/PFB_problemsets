#!/usr/bin/env python3

import re


A_count=0
T_count=0
G_count=0
C_count=0


fasta_dict = {}

fasta_file = open('Python_08.fasta', 'r')
#open file, save gene name in one list and seq in another.
for line in fasta_file:
	line=line.rstrip()
#sees lines that start with >, pulls then out, removes the >m and splits the name and description by white space. This gives you a list with [name, description]. You then use index to get the name only. Then assign the name to a dict and give that an empty value. For else, take line without > and add them together until you see another >.
	if line.startswith('>'):
		header = line[1::].split()
		gene_ID = header[0]			
		fasta_dict[gene_ID]= {'A':0, 'C':0, 'G':0, 'T':0}

	else:
	#	fasta_dict[gene_ID] += line		
		for nt in line:
			fasta_dict[gene_ID][nt] += 1
		 
	#	if char == 'T':
	#		count += 1
	#	elif char == 'G':
	#		G_count += 1
	#	elif char == 'C':
	#		C_count += 1
	#	elif char == 'A':
	#		A_count += 1
	#	print(A_count)
				
print(fasta_dict)							

		
#print(fasta_dict)
#ABOVE HERE IS A FASTA PARSER#
		
#for entry in fasta_dict:
	
#for key in fasta_dict:

#print(fasta_dict)




#for key in fasta_dict:
#	A_count = fasta_dict[key].count('A')
#	T_count = fasta_dict[key].count('T')
#	G_count = fasta_dict[key].count('G')
#	C_count = fasta_dict[key].count('C')
#	print(A_count, T_count, G_count, C_count)
#	print(len(fasta_dict[key]))



#for seq in fasta_dict:
			
