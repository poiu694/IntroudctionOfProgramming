import random

hexs = []
i, k = 0, 0

if __name__ == "__main__":
	for i in range(0, 10):
		tmp = hex(random.randrange(0, 100000))
		hexs.append(tmp)
	print("정렬 전 데이터 :", end = " ")
	[print(num, end=' ') for num in hexs]
	
	for i in range(0, len(hexs) - 1):
		for k in range(i + 1, len(hexs)):
			if int(hexs[i], 16) > int(hexs[k], 16):
				tmp = hexs[i]
				hexs[i] = hexs[k]
				hexs[k] = tmp
	print("\n 정렬 후 데이터 :", end = " ")
	[print(num, end=' ') for num in hexs]
