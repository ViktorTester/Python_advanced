import turtle as t

t.hideturtle()
t.goto(0, -110)

t.fillcolor('black')
t.begin_fill()

for i in range(2):
    t.forward(120)
    t.left(90)
    t.forward(360)
    t.left(90)

t.end_fill()

t.goto(60, -40)
t.dot(80, "forestgreen")

t.penup()
t.goto(60, 70)
t.dot(80, "yellow")

t.goto(60, 180)
t.dot(80, "red")

t.exitonclick()

# The program draws a traffic light.