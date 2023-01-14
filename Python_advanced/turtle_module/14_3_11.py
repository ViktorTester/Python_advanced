import turtle as t

t.hideturtle()
t.pensize(2)


def cardinal(x, y):
    t.write(x, move=False, align=y, font=('Arial', 17, 'bold'))


t.circle(40)
t.penup()
t.goto(0, 40)
t.pendown()

t.forward(150)
t.penup()
t.goto(167, 27)
cardinal('East', 'left')
t.left(180)
t.goto(150, 40)
t.pendown()

t.forward(300)
t.penup()
t.goto(-195, 28)
cardinal('West', 'center')
t.goto(-150, 40)
t.left(180)
t.pendown()

t.forward(150)
t.left(90)
t.forward(150)
t.penup()
t.forward(15)
cardinal('North', 'center')
t.left(180)
t.forward(15)
t.pendown()

t.forward(300)
t.penup()
t.forward(35)
cardinal('South', 'center')

t.exitonclick()

# The program draws the cardinal directions.