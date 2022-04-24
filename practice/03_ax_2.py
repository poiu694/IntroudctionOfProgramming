s = input('문자열을 입력 ==> ')

rs = s[::-1]
print(rs)

for i in range(len(s) - 1, -1, -1):
	print(s[i], end='')
