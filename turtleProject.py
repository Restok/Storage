#turtleProject.py
#Brandon Liu
#11/27/17
#Period 6
import turtle
from PIL import Image
def saveDrawing(drawName):
	print(f"saving drawing to {drawName}.eps/pnf")
	canvas = turtle.getcanvas()
	canvas.postscript(file = drawName+ '.eps')
	img = Image.open(drawName + '.eps')
	img.save(drawName + '.png', 'png')
t = turtle.Pen()
t.speed("fastest")
t.penup()
input()
screenWidth = t.screen.window_width()
screenHeight = t.screen.window_height()
t.color("black", "black")
t.setpos(-screenWidth//2 - 2, screenHeight//2 + 2)
t.pendown()
t.begin_fill()
t.setpos(screenWidth//2 + 2, screenHeight//2 + 2)
t.setpos(screenWidth//2 + 2, -screenHeight// 2 - 2)
t.setpos(-screenWidth//2 - 2, -screenHeight// 2 - 2)
t.setpos(-screenWidth//2 - 2, screenHeight// 2 + 2)
t.end_fill()
turtle.bgcolor("black")
turtle1 = turtle.Pen()
turtle2 = turtle.Pen()
turtle1.color("red")
turtle2.color("white")
turtle1.penup()
turtle2.penup()
turtle1.setpos(-100, 100)
turtle2.setpos(100, -100)
turtle1.pendown()
turtle1.speed("fastest")
turtle2.speed("fastest")
colors = ["green", "blue", "yellow", "white", "red", "orange"]
for counter in range(200):
	turtle1.forward(counter)
	turtle1.left(25)
	turtle1.color(colors[counter%6])
turtle2.setpos(-90, 100)
turtle2.pendown()
counter = 0	
for counter in range(200):

	turtle2.forward(counter)
	turtle2.left(25)
	turtle2.color(colors[counter%6])
choice = input("Press s to save your drawing:")
if choice == "s":
	name = input("What do you want to call your drawing?")
	saveDrawing(name)
input()