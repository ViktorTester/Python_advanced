import turtle


def spiral():
    turtle.shape('turtle')
    turtle.speed('fastest')
    turtle.color("red", "black")
    turtle.bgcolor("lightgreen")
    turtle.pensize(8)
    for i in range(36):
        turtle.stamp()
        turtle.penup()
        turtle.right(22)
        turtle.forward(i * 3)


spiral()
turtle.exitonclick()

# The program draws a turtle spiral.