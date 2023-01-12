import turtle as t
import random as r

t.title("night sky")
t.bgcolor('black')
t.hideturtle()
t.Screen().colormode(255)
t.tracer(2)


def star(side):
    a, b, c = r.randrange(255), r.randrange(255), r.randrange(255)
    t.fillcolor(a, b, c)
    t.pencolor(a, b, c)
    t.begin_fill()
    for i in range(5):
        t.forward(side)
        t.right(144)
        t.forward(side)
        t.left(72)
    t.end_fill()


def count(side):
    while True:
        t.penup()

        n = r.randint(1, 3)
        pos_x = r.randint(-350.00, 300.00)
        pos_y = r.randint(-280.00, 260.00)

        t.goto(pos_x, pos_y)

        t.pendown()

        t.left(r.randint(1, 360))
        star(side / n)


count(20)

t.exitonclick()

# The program draws an infinite number of multi-colored stars in the black sky.