#1. Mouse Events
#2. Keypress Events
#3. Global and local varibales
import random
import turtle
t = turtle.Pen()
turtle.bgcolor("black")
t.color("red")
turtle.colormode(255)
currentColorval = 0

def changeColor():
	global currentColorval
	t.color(colors[currentColorval])

	if currentColorval == 5:
		currentColorVal = 0
	else:
		currentColorval += 1

def changeColorRGB():
	global r, g, b
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	t.color(r, g, b)
	




#turtle.onscreenclick(t.setpos)
#turtle.onkeypress(changeColorRGB, "Up")
#turtle.listen()

def something():
	import random
	import turtle
	t = turtle.Pen()
	turtle.bgcolor("black")
	t.color("red")
	turtle.colormode(255)
	currentColorval = 0
	for x in (-360,0):
		changeColorRGB()
		for y in (-60, 0):
			t.forward(10)
			t.right(y)
			t.backward(10)
			t.right(y*-1)
		t.right(x)
		t.forward(30)
		t.left(x*-1)
		t.backward(30)
input()

something()