import os

script_dir = os.path.dirname(__file__)

file_name = input('복사할 파일명을 입력해 주세요.: ')
file_path = os.path.join(script_dir, file_name)
if os.path.exists(file_path):
	fp = open(file_path, 'r')
	strs = fp.readlines()

	wfp = open('copy.txt', 'w')
	for str in strs:
		wfp.writelines(str)
	fp.close()
else:
	print('파일명이 존재하지 않습니다.')
