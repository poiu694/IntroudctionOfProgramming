# variable #
i, k = 0, 0
star = '\u2605'

# main #
i = 0
while i < 9:
	if i < 5:
		k = 0
		while k < 4 - i:
			print(' ', end='')
			k += 1
		k = 0
		while k < i * 2 + 1:
			print(star, end='')
			k+=1
	else:
		k = 0
		while k < i - 4:
			print(' ', end='')
			k += 1
		k = 0
		while k < (9 - i) * 2 - 1:
			print(star, end='')
			k += 1
	print()
	i += 1
