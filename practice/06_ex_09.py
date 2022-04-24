hap = 0
for i in range(3333, 10000):
	if i % 1234 != 0:
		hap += i
	if hap > 100000:
		hap -= i
		break
print(hap)
