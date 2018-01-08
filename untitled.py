import turtle
colors = ["black","white","blue", "purple", "green", "white", "orange"]
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(1000):
	t.color(colors[x%6])
	t.forward(1)
	t.right(x)
	t.speed(20000)
input("Press any key to close window")