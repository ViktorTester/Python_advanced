import turtle

def star(side):
    turtle.shape('turtle')
    turtle.color("blue", "green")
    turtle.bgcolor("lightblue")
    turtle.pensize(5)
    for _ in range(2):
        turtle.penup()
        turtle.forward(side - 25)
        turtle.pendown()
        turtle.forward(25)
        turtle.penup()
        turtle.forward(20)
        turtle.stamp()
        turtle.left(180)
        turtle.forward(side)



def count(side):
    for _ in range(6):
        star(side)
        turtle.left(360 / 12)

count(211)
turtle.shape('turtle')
turtle.left(180)
turtle.stamp()
turtle.exitonclick()

# The program draws a watch dial on which instead of numbers there are turtles.