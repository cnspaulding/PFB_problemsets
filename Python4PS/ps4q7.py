#!/usr/bin/env python3

numbers = [101,2,15,22,95,33,2,27,72,15,52]
sorted_numbers = sorted(numbers)

even_sum=0
odd_sum=0

for num in sorted_numbers:
	if num%2 == 0:
		even_sum+=num
	
	else:
		odd_sum+=num
	
print(sorted_numbers)
print('Sum of evens:', even_sum)
print('Sum of odds:', odd_sum)
