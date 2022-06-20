def addNumber(n):
	if n == 0:
		return 0
	return n + addNumber(n - 1)
print(addNumber(100))
