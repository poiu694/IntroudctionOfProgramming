heart = '\u2665'

s = input()
i = 0
while True:
	ch = s[i]
	for k in range(0, int(ch)):
		print(heart, end = '')
	print()
	i += 1
	if i == len(s):
		break
