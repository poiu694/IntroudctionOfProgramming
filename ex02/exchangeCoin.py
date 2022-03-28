coin, five_hundred_cnt, one_hundred_cnt, five_ten_cnt, one_ten_cnt = 0, 0, 0, 0, 0

coin = int(input('교환할 돈은 얼마? '))

five_hundred_cnt = coin // 500;
coin %= 500;
print(f'500원 짜리 ==> {five_hundred_cnt}개')
one_hundred_cnt = coin // 100;
coin %= 100;
print(f'100원 짜리 ==> {one_hundred_cnt}개')
five_ten_cnt = coin // 50;
coin %= 50;
print(f'50원 짜리 ==> {five_ten_cnt}개')
one_ten_cnt = coin // 10;
coin %= 10;
print(f'10원 짜리 ==> {one_ten_cnt}개')
print(f'바꾸지 못한 잔돈 ==> {coin}원')
