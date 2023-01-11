import turtle as t
from turtle import Screen

Screen().setup(480, 480)
t.title("moon animation")
t.hideturtle()
t.bgcolor('darkblue')
t.penup()

t.goto(0, 0)
t.color('orange')
t.dot(220)

shade = t.Turtle()
shade.hideturtle()
shade.penup()
shade.screen.tracer(0)
shade.goto(220, 0)

while True:
    for i in range(200, -221, -2):
        shade.home()
        shade.dot(220, 'orange')
        shade.penup()
        shade.goto(i, 0)
        shade.dot(220, 'darkblue')
        shade.screen.update()

t.exitonclick()

# The program draws an animated moon.