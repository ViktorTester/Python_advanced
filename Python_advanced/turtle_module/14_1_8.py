import turtle


def diamond(side):
    turtle.shape('turtle')
    turtle.speed('slowest')
    turtle.color("blue", "green")
    turtle.pensize(5)
    for _ in range(2):
        turtle.forward(side)
        turtle.left(120)
        turtle.forward(side)
        turtle.left(60)


diamond(111)

# The program draws a diamond with 60 and 120 degree angles using turtle module.