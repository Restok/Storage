import turtle
import random
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

t.color("red")
t.penup()
t.setpos(0,0)
t.pendown()
for z in range(180):
	for x in range(5):
		t.forward(9)
		t.right(60)
		t.forward(10)
		t.left(40)
		t.forward(7)
		t.right(60)
		t.forward(8)
		t.left(60)
		t.forward(7)
		t.left(30)
		t.forward(8)
		t.right(10)
		t.forward(random.randint(1, 10))
	t.penup()
	t.setpos(0,0)
	t.pendown()
	t.right(2)
choice = input("Press s to save your drawing:")
if choice == "s":
	name = input("What do you want to call your drawing?")
	saveDrawing(name)
