#!/usr/bin/env python3

numbers = [101,2,15,22,95,33,2,27,72,15,52]
sorted_numbers = sorted(numbers)

even_numbers=[]
odd_numbers=[]

for num in sorted_numbers:
	if num%2 == 0:
		even_numbers.append(num)
	
	else:
		odd_numbers.append(num)
	
print(sorted_numbers)
print(sum(even_numbers))
print(sum(odd_numbers))
