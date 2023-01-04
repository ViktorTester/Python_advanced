import turtle as t

t.shape('arrow')
t.shapesize(0.5)
t.speed('fastest')
t.pensize(8)

t.penup()
t.goto(-200, 0)

t.pendown()
t.color('light sea green', 'black')
t.circle(80)
t.penup()
t.goto(55, -90)

t.pendown()
t.color('limegreen', 'black')
t.circle(80)
t.penup()
t.goto(-32, 0)

t.pendown()
t.color('black', 'black')
t.circle(80)
t.penup()
t.forward(168)

t.pendown()
t.color('red', 'black')
t.circle(80)
t.penup()
t.goto(-113, -90)

t.pendown()
t.color('yellow', 'black')
t.circle(80)

t.exitonclick()

# The program draws the Olympic rings.
