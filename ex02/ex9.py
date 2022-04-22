coin500, coin100, coin50, coin10 = 0, 0, 0, 0

coin500 = int(input('500원짜리 개수 --> '))
coin100 = int(input('100원짜리 개수 --> '))
coin50 = int(input('50원짜리 개수 --> '))
coin10 = int(input('10원짜리 개수 --> '))

print('##동전의 합계 ==> %d원' % (500 * coin500 + 100 * coin100 + 50 * coin50 + 10 * coin10))
