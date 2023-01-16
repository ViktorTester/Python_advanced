import turtle as t

t.title("stop")

t.pensize(5)
t.hideturtle()
t.penup()
t.goto(-70, -170)
t.pendown()
t.speed('fast')


def octagon(side):
    for i in range(8):
        t.forward(side)
        t.left(45)


t.fillcolor('white')
t.begin_fill()
octagon(180)
t.end_fill()

t.left(90)
t.penup()
t.forward(12)
t.right(90)
t.forward(5)
t.pendown()

t.color('red')
t.fillcolor('red')
t.begin_fill()
octagon(170)
t.end_fill()

t.color('white')
t.penup()
t.goto(18, -30)
t.write('STOP', move=True, align='center', font=('Arial Cyr Bold', 105, 'normal'))

t.exitonclick()

# The program draws a STOP sign.