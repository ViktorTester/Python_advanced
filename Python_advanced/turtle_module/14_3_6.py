import turtle as t

t.title("moon")
t.hideturtle()
t.speed('fast')

t.goto(-200, -200)

t.fillcolor('darkblue')
t.begin_fill()
for i in range(4):
    t.forward(350)
    t.left(90)
t.end_fill()

t.penup()
t.goto(-25, -25)
t.color('orange')
t.dot(250)
t.goto(10, -25)
t.color('darkblue')
t.dot(250)


t.exitonclick()

# The program draws the moon.