import turtle
import random
num = random.randint(1,360)
num1 = random.randint(0,6)
colors = ["red","yellow","blue", "purple", "green", "white", "orange"]
runn = True

for x in range(1,500):
	t = turtle.Pen()
	t.speed(5000)
	t.color(colors[num1])
	num1 = random.randint(0,3)
	t.getscreen().bgcolor("black")
	t.forward(100)
	t.right(num)
	num = random.randint(1,360)
	t.forward(100)
	t.left(num)
	num = random.randint(1,360)
	t.forward(200)
	t.backward(300)
	t.left(num)
	num = random.randint(1,360)
	t.forward(100)
#runn = True
#while runn:
#	t.forward(400)
#	if t.getX() > 500:
#		print("hey") 

input("Press a key to close the window")