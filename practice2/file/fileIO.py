import os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, './hello.txt')

f_ptr = open(file_path, 'r')

while True:
	str = f_ptr.readline()
	if (str == ''):
		break
	print(str)
f_ptr.close()
