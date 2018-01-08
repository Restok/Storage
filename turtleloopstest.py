import random
import turtle
t = turtle.Pen()
turtle.bgcolor("black")
t.color("red")
t.speed("fastest")
turtle.colormode(255)
for x in range(360):
	for y in range(60):
		t.forward(y)
		t.right(y)
		t.backward(y)
		t.right(y)
	t.right(x*4)
	t.forward(x*4)
	t.left(x*4)
	t.backward(x*4)
	t.forward(x*4)
	t.right(x*4)
	t.backward(x*4)

input()

something()