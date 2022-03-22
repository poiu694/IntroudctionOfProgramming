import sys

## 변수 선언 ##
intVar, floatVar, boolVar, strVar, listVar, tupleVar, dictVar, setVar = [None] * 8

## 메인 코드 ##
if __name__ == "__main__":
	intVar = 0
	floatVar = 0.0
	boolVar = True
	strVar = ''
	listVar = []
	tupleVar = ()
	dictVar = {}
	setVar = set()

	print("Int형 기본 크기 => ", sys.getsizeof(intVar))
	print("Float형 기본 크기 => ", sys.getsizeof(floatVar))
	print("Bool형 기본 크기 => ", sys.getsizeof(boolVar))
	print("String형 기본 크기 => ", sys.getsizeof(strVar))
	print("List형 기본 크기 => ", sys.getsizeof(listVar))
	print("Tuple형 기본 크기 => ", sys.getsizeof(tupleVar))
	print("Dictionary형 기본 크기 => ", sys.getsizeof(dictVar))
	print("Set형 기본 크기 => ", sys.getsizeof(setVar))
