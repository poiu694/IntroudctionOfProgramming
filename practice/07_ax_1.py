import random

list = []

for _ in range(0, 10):
	tmp = hex(random.randint(0, 1000000))
	list.append(tmp)

print("DATA : %s" % list)
for i in range(0, len(list)):
	for j in range(i, len(list)):
		if int(list[i], 16) > int(list[j], 16):
			tmp = list[i]
			list[i] = list[j]
			list[j] = tmp
print("SORTED : %s" % list)
