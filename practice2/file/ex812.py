str = input()

up, low, digit, kor, other = '', '', '', '', ''
for i in range(len(str)):
	if str[i].isupper():
		up += str[i]
	elif str[i].islower():
		low += str[i]
	elif str[i].isdigit():
		digit += str[i]
	elif str[i].isalpha():
		kor += str[i]
	else:
	 	other += str[i]

print(up)
print(low)
print(digit)
print(kor)
print(other)
