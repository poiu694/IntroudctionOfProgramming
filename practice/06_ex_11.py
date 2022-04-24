for i in range (3, 101):
	f = True
	for j in range(2, i):
		if i % j == 0:
			f = False
			break
	if f:
	 	print(i, end = ' ')
