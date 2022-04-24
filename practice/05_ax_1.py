import random

sequential = 0
cnt = 0
while True:
	while True:
		cnt += 1
		d1, d2, d3, d4, d5, d6 = [random.randint(1, 6) for _ in range(0, 6)]
	
		if (d1 == d2 and d2 == d3 and d3 == d4 and d4 == d5 and d5 == d6):
			print("모두 같음")
			break
		if ((d1 == 1 or d2 == 1 or d3 == 1 or d4 == 1 or d5 == 1 or d6 == 1) and
			(d1 == 2 or d2 == 2 or d3 == 2 or d4 == 2 or d5 == 2 or d6 == 2) and
			(d1 == 3 or d2 == 3 or d3 == 3 or d4 == 3 or d5 == 3 or d6 == 3) and
			(d1 == 4 or d2 == 4 or d3 == 4 or d4 == 4 or d5 == 4 or d6 == 4) and
			(d1 == 5 or d2 == 5 or d3 == 5 or d4 == 5 or d5 == 5 or d6 == 5) and
			(d1 == 6 or d2 == 6 or d3 == 6 or d4 == 6 or d5 == 6 or d6 == 6)):
				sequential += 1
	if cnt == 1:
	   break
