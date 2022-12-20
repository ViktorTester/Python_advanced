import turtle


def hexagon(side):
    for _ in '1' * 6:
        turtle.forward(side)
        turtle.right(60)


def count(size, num):
    turtle.shape('turtle')
    turtle.speed('slowest')
    turtle.color("blue", "green")
    turtle.pensize(5)
    for _ in range(num):
        hexagon(size)
        turtle.right(120)
        turtle.forward(size)
        turtle.left(60)


count(60, 6)

# The program draws honeycombs using turtle module.