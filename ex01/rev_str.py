## 변수 선언 ##
inStr = ''

## 메인 코드 ##
if __name__ == "__main__":
	inStr = input('문자열을 입력하세요 =>')
	
	for i in range(len(inStr) -1, -1, -1):
		print('%c' % inStr[i], end='')
