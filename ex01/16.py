num = input('글자 입력: ')

bin_flag, oct_flag, dec_flag, hex_flag = [False] * 4

if '0' <= num < '2':
	bin_flag = True
if '0' <= num < '8':
	oct_flag = True
if '0' <= num <= '9':
	dec_flag = True
if '0' <= num <= '9' or'A' <= num <= 'F':
	hex_flag = True
if (bin_flag):
	print('2진수', end = ' ')
if (oct_flag):
	if (bin_flag):
		print('또는', end = ' ')
	print('8진수', end = ' ')
if (dec_flag):
	if (bin_flag or oct_flag):
		print('또는', end = ' ')
	print('10진수', end = ' ')
if (hex_flag):
	if (bin_flag or oct_flag or dec_flag):
		print('또는', end = ' ')
	print('16진수', end = ' ')
if (bin_flag or oct_flag or dec_flag or hex_flag):
	print('입니다')
else:
	print('숫자가 아닙니다.')


