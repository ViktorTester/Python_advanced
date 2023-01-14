import turtle as t

t.hideturtle()
counter = -200
counter2 = 200


def square(side):
    for _ in range(4):
        t.right(90)
        t.forward(side)


for i in range(1, 26):
    t.penup()
    t.goto(counter, counter2)
    t.pendown()
    if i % 2 == 1:
        t.fillcolor("black")
        t.begin_fill()
        square(70)
        t.end_fill()
    else:
        square(70)

    if i % 5 != 0:
        counter += 70
    elif i % 5 == 0:
        counter2 -= 70
        counter = -200

t.exitonclick()

# The program draws a chessboard.