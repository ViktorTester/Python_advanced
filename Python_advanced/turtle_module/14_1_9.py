import turtle


def snowflake(side):
    turtle.shape('turtle')
    turtle.color("blue", "green")
    turtle.pensize(5)
    for _ in range(2):
        turtle.forward(side)
        turtle.left(60)
        turtle.forward(side)
        turtle.left(120)


def count(side):
    for _ in range(10):
        snowflake(side)
        turtle.left(35)


count(121)
turtle.exitonclick()

# The program draws a snowflake using turtle module.
