import os

script_path = os.path.dirname(__file__)
file_path = os.path.join(script_path, 'output.txt')

fp = open(file_path, 'w')
while True:
	str = input('입력해 주세요 : ')
	if (str == ''):
		break
	fp.writelines(str + '\n')
