import turtle
import random
num = random.randint(1,360)
num1 = random.randint(0,6)
colors = ["black","white","blue", "purple", "green", "white", "orange"]
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(1000):
	t.color(colors[x%6])
	t.forward(x)
	t.right(90)
	t.speed(20000)
input("Press any key to close window")