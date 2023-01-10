import turtle as t

t.title("circles")
t.hideturtle()
t.speed('fast')
colors = ['pink', 'purple', 'deepskyblue', 'dodgerblue', 'royalblue', 'limegreen', 'green', 'yellow', 'orange', 'red']
counter = 9

t.penup()
t.goto(0, -220)
t.pendown()

for i in range(200, 19, -20):
    t.fillcolor(colors[counter])
    counter -= 1
    t.begin_fill()
    t.circle(i)
    t.end_fill()
    t.penup()
    t.goto(0, -i)
    t.pendown()

t.exitonclick()

# The program draws a spherical rainbow.