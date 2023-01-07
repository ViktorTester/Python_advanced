import turtle as t

t.speed('fastest')
t.pensize(1.5)
t.ht()
t.penup()
t.goto(-200, 0)

t.pendown()
t.circle(36)
t.penup()
t.forward(200)
t.pendown()
t.circle(36)

t.penup()
t.goto(-100, -200)
t.pendown()
t.circle(117.5)
t.circle(65)

t.penup()
t.goto(-100, -175)
t.pendown()
t.goto(-100, -105)
t.circle(10)

t.penup()
t.goto(-160, -85)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.forward(120)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()

t.exitonclick()

# The program draws a bear.