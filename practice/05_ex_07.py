import random

a1, a2, b1, b2 = [random.randint(1, 6) for i in range(0, 4)]

print("A ", a1, a2)
print("B ", b1, b2)

if (a1 + a2 == b1 + b2):
	print("비김")
elif (a1 + a2 > b1 + b2):
	print("A Win")
else:
	print("B Win")
