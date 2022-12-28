import turtle

colors = ['yellow', 'green', 'purple', 'orange', 'red', 'blue']


def spiral():
    turtle.shape()
    turtle.speed('fastest')
    for i in range(44):
        turtle.left(45)
        turtle.forward(i * 3)
        turtle.pensize(i / 1.8)
        turtle.color(colors[i % 6])


spiral()
turtle.exitonclick()

# The program draws a colored spiral.
