# variable #
num1, num2, added, sum = 0, 0, 0, 0

# main #
num1 = int(input('*** 첫 번째 숫자를 입력하세요 : '))
num2 = int(input('*** 두 번째 숫자를 입력하세요 : '))
added = int(input('*** 더할 숫자를 입력하세요 : '))

for num in range(num1, num2 + 1, added):
	sum += num

print(" %d+%d+...%d는 %d입니다. " %(num1, num1 + added, num2, sum))
