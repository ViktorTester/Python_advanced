import turtle as t

def rectangle(side):
    t.shape('turtle')
    t.color("blue", "green")
    t.speed('fastest')
    t.pensize(4)
    side2 = side
    while side > side2 // 100:
        side -= 5
        t.right(90)
        t.forward(side)


rectangle(200)


t.exitonclick()

# The program draws a spiral using turtle module.