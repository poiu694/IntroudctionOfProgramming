inStr = 'IT_CookBook_Python'
outStr = ''

for i in range(0, len(inStr)):
	if i % 2 == 0:
		outStr += inStr[len(inStr) - i - 1]
	else:
		outStr += '#'
print(outStr)
