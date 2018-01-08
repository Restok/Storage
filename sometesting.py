import random
import turtle
t = turtle.Pen()
turtle.bgcolor("black")
t.color("red")
t.speed("fastest")
turtle.colormode(255)
def changeColorRGB():
	global r, g, b
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	t.color(r, g, b)
for x in range(100):
	changeColorRGB()
	for y in range(5):
		t.forward(10)
		t.right(y)
		t.backward(30)
		t.right(y*-1)
		t.setpos(0, 0)
	t.right(40)
	t.forward(15)
	t.left(60)
	t.backward(15)
	t.forward(x)
	t.right(x)
	t.backward(x)
t.setpos(0,0)
input()

something()