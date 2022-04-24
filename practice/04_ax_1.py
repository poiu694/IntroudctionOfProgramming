a = int(input())

if a % 4 == 0 and a % 100 != 0:
	print("%d 년은 윤년입니다." % a)
elif a % 400 == 0:
	print("%d 년은 윤년입니다." % a)
else:
	print("윤년이 아닙니다.")
	
