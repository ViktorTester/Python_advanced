import turtle
import random

colors = ['CadetBlue', 'CornFlowerBlue', 'DarkBlue', 'DeepSkyBlue', 'DodgerBlue', 'RoyalBlue', 'blue', 'SteelBlue']


def star(a, b):
    turtle.hideturtle()
    turtle.setup(1000, 700)
    turtle.bgcolor('lightblue')
    turtle.speed(0)

    turtle.forward(b)
    turtle.left(180)
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(a)
    turtle.left(180)
    turtle.forward(a)
    turtle.right(-90)
    turtle.forward(a)
    turtle.left(180)
    turtle.forward(a)
    turtle.left(45)
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(a)
    turtle.left(180)
    turtle.forward(a)
    turtle.right(-90)
    turtle.forward(a)
    turtle.left(180)
    turtle.forward(a)
    turtle.left(45)
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(a)
    turtle.left(180)
    turtle.forward(a)
    turtle.right(-90)
    turtle.forward(a)
    turtle.left(180)
    turtle.forward(a)
    turtle.left(45)
    turtle.forward(a)


def count(a, b):
    for i in range(100):
        turtle.color(random.choice(colors))
        turtle.pensize(random.randint(1, 3))
        turtle.penup()

        n = random.randint(1, 5)
        pos_x = random.randint(-350.00, 300.00)
        pos_y = random.randint(-280.00, 260.00)

        turtle.goto(pos_x, pos_y)

        turtle.pendown()
        for _ in range(8):
            star(a / n, b / n)
            turtle.left(45)


count(25, 100)
turtle.exitonclick()

# The program draws snowflakes in different places, different colors and sizes.