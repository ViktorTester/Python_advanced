import turtle


def star(side):
    turtle.shape('turtle')
    turtle.color("blue", "green")
    turtle.pensize(5)
    for _ in range(2):
        turtle.forward(side)
        turtle.left(180)
        turtle.forward(side)


def count(side):
    for _ in range(6):
        star(side)
        turtle.left(30)


count(121)
turtle.exitonclick()

# The program reads the number of rays of the web, the number n.
# The program draws a star with n rays using turtle module.

