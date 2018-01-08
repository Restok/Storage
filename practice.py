import turtle

t = turtle.Pen()
turtle.bgcolor("black")
t.pencolor("white")
t.pendown()
t.shape("turtle")
t.write("Hello World!", font=("Times", 20, "normal"))
t.setpos(100,0)


input("Press any key to close the turtle!")