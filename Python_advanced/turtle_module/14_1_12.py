import turtle as t


def rectangle(side):
    t.shape('turtle')
    t.color("blue", "green")
    t.speed('fastest')
    t.pensize(4)
    side2 = side
    while side > side2 // 10:
        side -= 10
        for i in range(4):
            t.left(90)
            t.forward(side)


rectangle(200)

t.exitonclick()

# The program draws a pattern of nested squares using turtle module.
