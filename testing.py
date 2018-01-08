import turtle
import random
def starThing():
	num = random.randint(1,360)
	num1 = random.randint(0,6)
	colors = ["black","red","orange","brown"]
	t = turtle.Pen()
	t.speed("fastest")
	t.width("2")
	turtle.bgcolor('black')
	for x in range(1000):
		t.color(colors[x%4])
		t.forward(x)
		t.right(20)
		t.backward(x)
		t.right(20)
	input("Press any key to close window")

def experimentation():
	num = random.randint(1,360)
	num1 = random.randint(0,6)
	colors = ["black","red","orange","brown"]
	t = turtle.Pen()
	t.speed("fastest")
	t.width("4")
	turtle.bgcolor('black')
	for x in range(360):
		t.color(colors[x%4])
		t.forward(x)
		t.right(20)
		t.backward(x)
		t.right(20)
		t.forward(x)
		t.left(90)
		t.backward(x)
		t.left(90)

	input("Press any key to close window")
def experimentation2():
	num = random.randint(1,360)
	num1 = random.randint(0,6)
	colors = ["purple", "blue", "black", "violet"]
	t = turtle.Pen()
	t.speed("fastest")
	t.width("4")
	turtle.bgcolor('black')
	for x in range(360):
		t.color(colors[x%4])
		t.forward(x)
		t.right(30)
		t.backward(x)
		t.right(30)
		t.forward(x+20)
		t.left(60)
		t.backward(x+20)
		t.left(60)

	input("Press any key to close window")
def experimentation3():
	num = random.randint(1,360)
	num1 = random.randint(0,6)
	colors = ["purple", "blue", "black", "violet"]
	t = turtle.Pen()
	t.speed("fastest")
	t.width("4")
	turtle.bgcolor('black')
	for x in range(360):
		t.color(colors[x%4])
		t.forward(x)
		t.right(30)
		t.backward(x)
		t.right(30)
		t.forward(x+100)
		t.left(60)
		t.backward(x-50)
		t.left(60)

	input("Press any key to close window")
def experimentation4():
	num = random.randint(1,360)
	num1 = random.randint(0,6)
	colors = ["purple", "blue", "black", "violet"]
	t = turtle.Pen()
	t.speed("fastest")
	t.width("4")
	t.setpos(-125,-37.5)
	turtle.bgcolor('black')
	for x in range(270):
		t.color(colors[x%4])
		t.forward(x)
		t.right(30)
		t.backward(x)
		t.right(30)
		t.forward(x+100)
		t.left(60)
		t.backward(x-50)
		t.left(60)
	colors = ["black","red","orange","brown"]
	t.setpos(0,0)
	t.width("3")
	for x in range(120):
		t.color(colors[x%4])
		t.forward(x)
		t.left(60)
		t.backward(x)
		t.penup()
		t.right(30)
		t.forward(x)
		t.pendown()
		t.left(60)
		t.backward(x)
		t.right(30)
	t.penup()
	t.setpos(0,0)
	t.pendown()
	t.dot(50,"black")
	turtle.hide()
	input("Press any key to close the window.")
experimentation4()
def experiment5():
	t = turtle.Pen()
	t.speed("fastest")
	t.width("2")
	turtle.bgcolor('black')
	return
