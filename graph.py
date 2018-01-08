import math
import turtle

turtle.bgcolor("black")
myTurt = turtle.Pen()
myTurt2 = turtle.Pen()

myTurt.screen.setworldcoordinates(0,-1,360, 1)

myTurt.color("white")
myTurt2.color("red")
for ang in range(360):
	y1 = math.tan(math.radians(ang))
	y2 = math.cos(math.radians(ang))
	myTurt.setpos(ang, (y1)*-1+100)
	myTurt2.setpos(ang, y2)



input()