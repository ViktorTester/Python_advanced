import turtle as t

t.hideturtle()
t.pensize(2)

for i in range(3):
    t.forward(200)
    t.left(120)

t.color('white')

t.penup()
t.goto(100, -60)

t.pendown()
t.left(60)

for i in range(3):
    t.penup()
    t.forward(200)
    t.dot(70, 'black')
    t.left(120)

t.fillcolor('white')

t.begin_fill()
for i in range(3):
    t.forward(200)
    t.left(120)
t.end_fill()

t.exitonclick()

# The program draws an optical illusion.