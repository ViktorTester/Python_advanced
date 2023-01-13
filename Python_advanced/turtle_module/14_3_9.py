import turtle as t
import random as r

t.hideturtle()
t.tracer(2)
t.pensize(1)
t.Screen().colormode(255)


def triangle(side):
    t.forward(side / 2)
    for _ in range(2):
        t.right(120)
        t.forward(side)
    t.right(120)
    t.forward(side / 2)


def square(side):
    t.forward(side / 2)
    for _ in range(3):
        t.right(90)
        t.forward(side)
    t.right(90)
    t.forward(side / 2)


def pentagon(side):
    t.forward(side / 2)
    for _ in range(4):
        t.right(72)
        t.forward(side)
    t.right(72)
    t.forward(side / 2)


def hexagon(side):
    t.forward(side / 2)
    for _ in range(5):
        t.right(60)
        t.forward(side)
    t.right(60)
    t.forward(side / 2)


def heptagon(side):
    t.forward(side / 2)
    for _ in range(6):
        t.right(51.428)
        t.forward(side)
    t.right(51.428)
    t.forward(side / 2)


counter = -200
counter2 = 200
for i in range(1, 26):
    x = r.choice([1, 2, 3, 4, 5])
    a, b, c = r.randrange(255), r.randrange(255), r.randrange(255)
    t.fillcolor(a, b, c)
    t.begin_fill()
    t.penup()
    t.goto(counter, counter2)
    t.pendown()
    if x == 1:
        triangle(60)
    elif x == 2:
        square(50)
    elif x == 3:
        pentagon(35)
    elif x == 4:
        hexagon(30)
    else:
        heptagon(25)
    t.end_fill()
    if i % 5 != 0:
        counter += 70
    elif i % 5 == 0:
        counter2 -= 70
        counter = -200

t.exitonclick()

# The program draws 5 rows of 5 random regular polygons in a random color.
# The figures are centered relative to each other.