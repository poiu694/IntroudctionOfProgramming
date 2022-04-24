import random

list = [random.randint(1, 20) for i in range(0, 20)]
print(list)
for i in range(1, 21):
	if i in list:
		print("O %d" % i)
