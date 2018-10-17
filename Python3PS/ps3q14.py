#!/usr/bin/env python3

#here I want to look to see if/where there is an ecoR1 cut site in this DNA string.

#dna = 'CCCGAATTCGGG'
dna = 'GATGGGATTggggttttccccTCCCATGTGCTCAAGACTGGCGCTaaaaGttttGAGCTTCTCaaaaGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCggggACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGccccCTCTGAGTCAGGAAACAttttCAGACCTATGGAAACTACTTCCTGaaaaCAACGTTCTGTccccCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTccccGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTccccCCGTGGccccTGCACCAGCAGCTCCTACACCGGCGGccccTGCACCAGccccCTCCTGGccccTGTCATCTTCTGTCCCTTCCCAGaaaaCCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTccccTGCCCTCAACAAGATGttttGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACAccccCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGccccCACCATGAGCGCT'

#EcoR1 string is -GAATTC
#here look to see if this exact sequence is in the DNA
#identify the exact location (bp) in the sequence it is. Becasue python starts counting with 0, the first bp is actually 0 here but I would start with 1. So to get the actual bp it starts with, you have to add 1. Then I added 5 more bases to account for the 5 bases following that complete the site
ecoR1 = dna.find('GAATTC')

ecoR1_start = ecoR1 + 1
ecoR1_end = ecoR1_start + 5


#here I want to pull out the exact sequence from the above. 
ecoR1_site = dna[ecoR1:ecoR1_end]


print('ecoR1 start site:', ecoR1_start)
print('ecoR1 end site:', ecoR1_end)
print('ecoR1 site:', ecoR1_site)

#identify the bp up and down stream of the REsite

up_downstream = dna[390:407]
print(up_downstream)

