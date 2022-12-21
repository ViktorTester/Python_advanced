import turtle


def soviet_star(side):
    turtle.shape('turtle')
    turtle.color("blue", "green")
    turtle.pensize(5)
    for _ in range(5):
        turtle.forward(side)
        turtle.right(144)


soviet_star(131)

turtle.exitonclick()

# The program draws the correct five-pointed star using turtle module.
