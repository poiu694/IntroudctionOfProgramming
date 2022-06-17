from classMethod import Info

info1 = Info('print Hello')
info2 = Info('Hi')

print(f"#repr {info1}")
print(f"#repr {info2}")

print(f"#add : {info1 + info2}")

if info1 > info2:
	print("#ls info1 > info2")
elif info1 == info2:
	print("#eq info1 == info2")
else:
	print("lt info1 < info2")
del(info1)
del(info2)
