base = int(input("입력 진수를 결정하세요  (16/10/8/2) : "))
num = input("값 입력: ")

decimal_num = int(num, base)

print("16진수 ==> ", hex(decimal_num))
print("10진수 ==> ", decimal_num)
print("8진수 ==> ", oct(decimal_num))
print("2진수 ==> ", bin(decimal_num))
