star = '\u2605'

s = input()
for i in s:
	for j in range(0, int(i) * 2):
		print(star, end = '')
	print()
