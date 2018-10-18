#!/usr/bin/env python3

species= 'sapiens, erectus, neanderthalensis'

print(species)

species_list = species.split(',')
print(species_list)

sorted_species_list= sorted(species_list)
print(sorted_species_list)

sorted_len_species_list = sorted(species_list, key=len)
print(sorted_len_species_list)


