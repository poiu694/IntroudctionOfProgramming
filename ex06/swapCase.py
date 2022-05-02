inStr, outStr = "", ""
ch = ""
count, i = 0, 0

if __name__ == "__main__":
	inStr = input('문자열을 입력하세요: ')
	count = len(inStr)

	for i in range(0, count):
		ch = inStr[i]
		if ch.islower():
			newCh = ch.upper()
		elif ch.isupper():
			newCh = ch.lower()
		else:
			newCh = ch
		outStr += newCh

	print('대소문자 반환 결과 => ', outStr)
