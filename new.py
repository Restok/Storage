import turtle
import random
num = random.randint(1,360)
colors = ["orange","yellow","green", "blue", "purple"]
t = turtle.Pen()
turtle.bgcolor("black")
t.width(4)
t.speed(1000)
for x in range(360):
	t.color(colors[x%5])
	t.backward(30)
	num = random.randint(1,360)
	t.left(num)






