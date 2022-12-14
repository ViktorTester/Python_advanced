import turtle

def star(side):
    turtle.shape('arrow')
    turtle.color("blue", "green")
    turtle.pensize(5)
    for _ in range(2):
        turtle.forward(side)
        turtle.stamp()
        turtle.left(180)
        turtle.forward(side)


def count(side):
    n = int(input())
    for _ in range(180 // (360 // n)):
        star(side)
        turtle.left(360 / n)

count(121)
turtle.shape('circle')
turtle.stamp()
turtle.exitonclick()

# The program reads the number of rays of the web,
# the number n, and displays a star with a given number of rays.