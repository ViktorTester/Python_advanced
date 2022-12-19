import turtle as t


def hexagon(side):
    t.shape('turtle')
    t.speed('slowest')
    t.color("blue", "green")
    t.pensize(5)
    for _ in range(6):
        t.forward(side)
        t.left(60)


hexagon(100)

# # The program draws a hexagon using turtle module.