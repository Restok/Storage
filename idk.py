import turtle
from PIL import Image
input()
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
for x in range(3):
	for y in range(25):
		t.forward(y)
		t.left(y)
		t.forward(y)
		t.right(y)
		t.backward(y)
		t.left(y)
		for z in range(25):
			t.forward(z)
			t.left(z)
			t.forward(z)
			t.right(z)
			t.backward(z)
			t.left(z)
	t.setpos(x,0)
	t.forward(x)
	t.left(x)
	t.forward(x)
	t.right(x)
	t.backward(x)
	t.left(x)
choice = input("Press s to save your drawing:")
if choice == "s":
	name = input("What do you want to call your drawing?")
	saveDrawing(name)
