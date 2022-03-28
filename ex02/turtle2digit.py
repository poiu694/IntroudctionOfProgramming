import turtle

## global ##
num = 0
swidth, sheight = 1000, 300
cur_x, cur_y = 0, 0

## main ##
if __name__ == "__main__":
	turtle.title('거북이로 2진수 표현하기')
	turtle.shape('turtle')
	turtle.setup(width = swidth + 50, height = sheight + 50)
	turtle.screensize(swidth, sheight)
	turtle.penup()
	turtle.left(90)

	num = int(input('숫자를 입력하세요'))
	binary = bin(num)
	cur_x = swidth / 2
	cur_y = 0
	for i in range(len(binary) - 2):
		turtle.goto(cur_x, cur_y)
		if num & 1:
			turtle.color('red')
			turtle.turtlesize(2)
		else:
			turtle.color('blue')
			turtle.turtlesize(1)
		turtle.stamp()
		cur_x -= 50
		num >>= 1
	turtle.done()
