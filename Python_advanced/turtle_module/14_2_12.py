import turtle as t

t.shape('circle')
t.speed('fast')
t.color('light sea green', 'blue')
t.pensize(4)

for i in range(10):
    t.goto(200 - (i * 46), -300)
    t.dot('blue')
    t.penup()
    t.goto(0, 0)
    t.pendown()

t.hideturtle()
t.dot(10, 'orange')
t.exitonclick()