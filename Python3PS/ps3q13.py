#!/usr/bin/env python3
#generate the reverse compliment of the follow dna

dna = 'GATGGGATTggggttttccccTCCCATGTGCTCAAGACTGGCGCTaaaaGttttGAGCTTCTCaaaaGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCggggACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGccccCTCTGAGTCAGGAAACAttttCAGACCTATGGAAACTACTTCCTGaaaaCAACGTTCTGTccccCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTccccGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTccccCCGTGGccccTGCACCAGCAGCTCCTACACCGGCGGccccTGCACCAGccccCTCCTGGccccTGTCATCTTCTGTCCCTTCCCAGaaaaCCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTccccTGCCCTCAACAAGATGttttGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACAccccCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGccccCACCATGAGCGCT'

#dna = 'CCCGAATTCGGG'

#this is replacing all the bases with the opposite base (for the compliment). Because you are feeding the replaced dna seq into each new replace, then you have to change the case of the letters. For ex: if you do replaceA, you replace all teh A with T. But then the next command is to replace all teh T with A. So you will just replace all the A you made T with A. So instead, you can replace with a lowercase t, then change all teh T to A.
replaceA = dna.replace('A', 't')
replaceT = replaceA.replace('T', 'A')
replaceC = replaceT.replace('C', 'g')
replaceG = replaceC.replace('G', 'C')

#This will read the dna string backwards.
reverse_dna = replaceG[::-1]
#make everything the same case
reverse_comp = reverse_dna.upper()
print('dna:', dna)
print('reverse:', reverse_comp)




