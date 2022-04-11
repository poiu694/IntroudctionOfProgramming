# variable #
is_prime, result = True, ''

# main #
for num in range(3, 101):
	is_prime = True
	for i in range (2, num):
		if num % i == 0:
			is_prime = False
			break
	if is_prime:
	 	result += str(f'{num} ')
print(result)
