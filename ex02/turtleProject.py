import turtle
import random

# define variable #
swidth, sheight, psize, exit_count = 300, 300, 3, 0
r, g, b, angle, dist, cur_x, cur_y = [0] * 7

# main #
turtle.title('거북이 마음대로 다니기')
turtle.shape('turtle')
turtle.pensize(psize)
turtle.setup(width = swidth + 30, height = sheight + 30)
turtle.screensize(swidth, sheight)

while True:
	r = random.random()
	g = random.random()
	b = random.random()
	turtle.pencolor((r, g, b))

	angle = random.randrange(0, 360)
	dist = random.randrange(1, 100)

	turtle.left(angle)
	turtle.forward(dist)
	cur_x = turtle.xcor()
	cur_y = turtle.ycor()

	if (-swidth / 2 <= cur_x and cur_x <= swidth / 2) and (-sheight / 2 <= cur_y and cur_y <= sheight / 2):
		pass
	else:
		turtle.penup()
		turtle.goto(0, 0)
		turtle.pendown()

		exit_count += 1
		if exit_count >= 5:
			break

turtle.done()
