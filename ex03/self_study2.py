# variable #
num, isPrime = 0, True

# main #
num = int(input(' *** 숫자를 입력하세요 : '))
for i in range(2, num):
	if (num % i == 0):
		isPrime = False

if (isPrime):
	print(" %d 는 소수입니다." %(num))
else:
	print(" %d 는 소수가 아닙니다." %(num))
