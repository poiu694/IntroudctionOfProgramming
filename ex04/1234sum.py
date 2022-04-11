# variable #
sum = 0

# main #
for num in range(3333, 10000):
	if num % 1234 == 0:
		if num + sum > 100000:
			break
		sum += num
	else:
		continue
print(sum)
