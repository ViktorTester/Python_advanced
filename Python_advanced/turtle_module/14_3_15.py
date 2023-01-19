import turtle as t
import math as m

t.title("heart")
t.hideturtle()

k = 0

t.color('red')
t.fillcolor('red')
t.begin_fill()
while k <= 2 * m.pi:
    x = 128 * m.sin(k) ** 3
    y = 8 * (13 * m.cos(k) - 5 * m.cos(2 * k) - 2 * m.cos(3 * k) - m.cos(4 * k) - 5)
    t.goto(x, y)
    k += 0.01
t.end_fill()

t.exitonclick()

# The program draws a heart.