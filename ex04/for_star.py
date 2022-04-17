mx = 101

for i in range(0, mx):
	if i <= mx // 2:
		for k in range(0, mx // 2 - i):
			print(' ', end='')
		for k in range(0, 2*i + 1):
			print('*', end='')
	else:
		for k in range(0, i - mx // 2):
			print(' ', end='')
		for k in range(0, -2*i + 2*mx - 1):
			print('*', end='')
	print()
		
