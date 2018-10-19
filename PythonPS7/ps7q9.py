#!/usr/bin/env python3

#I commented out the header and the very last blank line of the file. If you don't comment out the last line, the .split function will not work.

RE={}
remove_header = []
count =0
enzyme_file = open('bionet.py', 'r')

for line in enzyme_file:	
	line=line.rstrip()
	if not line.startswith('#'):	#remove header
	#	print(line)	
		line= line.replace(' (', '_(') #replace spaces in first column
	#	print(line)	
		enzyme,cut_site= line.split() #make into dict
		RE[enzyme]=cut_site
print(RE)		

	
#	count += 1
#	line=line.replace(' (', '_(')
#	if count>11:
#		remove_header.append(line)
#		print(remove_header)			
#with open('bionet.txt', 'r') as enzyme_file:










#for line in enzyme_file:	
#	line=line.rstrip()
#	count += 1
#	line=line.replace(' (', '_(')
#	if count>11:
#		remove_header.append(line)
#		print(remove_header)			
	#	enzyme,cut_site = line.split()
	#	RE[enzyme]= cut_site
	#	print(RE)		
#print(remove_header)	



#	enzyme, cut_site = line.split()
#	RE[enzyme] = cut_site
#print(RE)	

#remove_header=  re.sub(r'>seq1\n', r'', fasta)
#print('no header:', remove_header)
