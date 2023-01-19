import turtle as t
import random as r

t.title('clicking stars')
t.hideturtle()
t.colormode(255)
t.bgcolor('black')
t.tracer(0)

a = [5, 144, 72]
b = [6, 120, 60]
c = [7, 124, 72]

size = r.randrange(5, 15)


def random_color():
    return r.randrange(256), r.randrange(256), r.randrange(256)


def star(x, y, side):
    w = r.choice([a, b, c])
    color = random_color()

    t.penup()
    t.goto(x, y)
    t.pendown()

    t.fillcolor(color)
    t.pencolor(color)
    t.begin_fill()

    for i in range(w[0]):
        t.forward(side)
        t.right(w[1])
        t.forward(side)
        t.left(w[2])
    t.end_fill()


def left_mouse_click(x, y):
    star(x, y, size)


t.Screen().onclick(left_mouse_click)
t.Screen().listen()

t.done()

# By pressing the left mouse button, the program draws a star in the place of the click.
# In this case, the stars can have different sizes, colors and have a different number of sides.