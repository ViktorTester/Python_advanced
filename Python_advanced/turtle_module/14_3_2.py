import turtle as t

a = t.Turtle()
t.pensize(2)
t.hideturtle()

t.fillcolor('lightblue')
t.begin_fill()

for i in range(4):
    t.forward(100)
    t.left(90)

t.end_fill()

b = t.Turtle()
t.hideturtle()

t.fillcolor('brown')
t.penup()
t.begin_fill()
t.goto(-20, 100)
t.pendown()
t.forward(140)
t.goto(50, 200)
t.goto(-20, 100)
t.end_fill()

t.exitonclick()

# The program draws a house.
